import streamlit as st
import pandas as pd
import io
# NOTE: We keep imports from utils for charting/summary, and removed the old load_data dependency
from utils import plot_boxplot, get_summary_table, plot_kpi_ranking 

# --- Configuration ---
st.set_page_config(
    page_title="Solar Farm Site Comparison",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define which files are expected and map their names to the Country column value
EXPECTED_FILES = {
    'benin_clean.csv': 'Benin',
    'sierra_leone_clean.csv': 'Sierra Leone',
    'togo_clean.csv': 'Togo',
}

# --- Data Loading (Using Streamlit Multi-File Uploader) ---

@st.cache_data
def get_uploaded_data(uploaded_files):
    """
    Reads multiple uploaded files, adds the 'Country' column, and combines them.
    """
    if not uploaded_files:
        return None
        
    all_dfs = []
    found_countries = set()
    
    for file in uploaded_files:
        filename = file.name.lower()
        country = None

        # Determine country based on filename
        for expected_name, country_name in EXPECTED_FILES.items():
            if expected_name in filename:
                country = country_name
                break
        
        if country is None:
            # Skip or warn if the file name doesn't match an expected country
            st.warning(f"Skipping file '{file.name}'. Cannot determine country name from filename.")
            continue
            
        found_countries.add(country)
        
        try:
            # Read the file content and decode it
            df = pd.read_csv(io.StringIO(file.getvalue().decode("utf-8")), index_col=0, parse_dates=True)
            df['Country'] = country
            all_dfs.append(df[['GHI', 'DNI', 'DHI', 'Country']])

        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
            return None
            
    if len(all_dfs) == len(EXPECTED_FILES):
        st.success(f"Successfully loaded and combined data for: {', '.join(sorted(list(found_countries)))}")
        return pd.concat(all_dfs, ignore_index=True)
    elif all_dfs:
         st.warning(f"Data combined, but only {len(found_countries)} out of {len(EXPECTED_FILES)} countries were found. Upload all three for complete analysis.")
         return pd.concat(all_dfs, ignore_index=True)
    else:
        # If no valid files were processed
        return None


# --- Sidebar and Widgets ---
st.sidebar.title("Configuration")

# 1. ADD THE MULTI-FILE UPLOADER WIDGET
uploaded_files = st.sidebar.file_uploader(
    "1. Upload the Clean Country CSV Files",
    type=['csv'],
    accept_multiple_files=True, # Key change here!
    help="Please upload all three files: benin_clean.csv, sierra_leone_clean.csv, and togo_clean.csv."
)

df_combined = get_uploaded_data(uploaded_files)

# --- Stop Execution if Data is Missing ---
if df_combined is None or df_combined.empty:
    st.title("☀️ Cross-Country Solar Farm Site Comparison")
    st.markdown("### Strategic Recommendation for MoonLight Energy Solutions")
    st.info(f"""
        ⚠️ **Action Required:** Please upload the following three clean data CSV files in the sidebar to proceed with the analysis:
        - `benin_clean.csv`
        - `sierra_leone_clean.csv`
        - `togo_clean.csv`
        """)
    st.stop()
    
# --- Continue with Dashboard Logic (Only if df_combined exists) ---

# 2. Widget to select the visualization metric
metric_options = ['GHI', 'DNI', 'DHI']
selected_metric = st.sidebar.selectbox(
    "2. Select Irradiance Metric for Boxplot:",
    metric_options
)

# 3. Widget to select countries
countries = df_combined['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect(
    "3. Select Countries for Analysis:",
    countries,
    default=countries
)

# Filter the data based on selection
df_filtered = df_combined[df_combined['Country'].isin(selected_countries)]


# --- Main Dashboard Layout (No changes needed below this line) ---
st.title("☀️ Cross-Country Solar Farm Site Comparison")
st.markdown("### Strategic Recommendation for MoonLight Energy Solutions")

tab1, tab2, tab3 = st.tabs(["📊 KPI Dashboard", "📦 Distribution Analysis", "📝 Data Table"])

with tab1:
    st.header("Solar Resource Ranking & Summary")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Mean GHI Ranking")
        fig_kpi = plot_kpi_ranking(df_filtered)
        st.pyplot(fig_kpi, use_container_width=True)
        if not df_filtered.empty:
            best_site = df_filtered.groupby('Country')['GHI'].mean().idxmax()
            st.info(f"**Best Site:** {best_site} has the highest average solar resource.")
        else:
             st.info("**Best Site:** (No data selected)")

    with col2:
        st.subheader("Metric Comparison Summary (Mean, Median, Std Dev)")
        summary_df = get_summary_table(df_combined) 
        st.dataframe(summary_df)
        st.markdown("""
        **Interpretation:** - **Mean GHI** determines overall energy potential.
        - **Std Dev** indicates variability (higher = less stable/more clouds).
        """)

with tab2:
    st.header(f"Distribution of {selected_metric} (W/m²)")
    
    if not df_filtered.empty:
        fig_box = plot_boxplot(df_filtered, selected_metric)
        st.pyplot(fig_box, use_container_width=True)
        st.markdown(f"""
        This boxplot shows the distribution of **{selected_metric}** when non-irradiating hours are excluded.
        - The highest box top (75th percentile) and maximum values indicate the best **resource quality**.
        - Sierra Leone's low DNI distribution highlights its reliance on diffuse light (cloudiness).
        """)
    else:
        st.warning("Please select at least one country to view the distribution.")
        
with tab3:
    st.header("Raw Combined Data Preview")
    st.markdown("Preview of the cleaned, consolidated dataset.")
    st.dataframe(df_combined.head(100))
    st.markdown(f"**Total Records:** {len(df_combined):,}")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.markdown("Developed for the Solar Data Challenge")