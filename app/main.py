# app/main.py

import streamlit as st
import pandas as pd
from utils import load_data, plot_boxplot, get_summary_table, plot_kpi_ranking

# --- Configuration ---
st.set_page_config(
    page_title="Solar Farm Site Comparison",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Data Loading (Using Streamlit Caching) ---
# This decorator tells Streamlit to run the function only once and cache the result
@st.cache_data
def get_data():
    """Wrapper function to load data safely."""
    df, error = load_data()
    if error:
        st.error(error)
        st.stop() # Stop the app if data loading failed
    return df

df_combined = get_data()

# --- Sidebar and Widgets ---
st.sidebar.title("Configuration")

# 1. Widget to select the visualization metric
metric_options = ['GHI', 'DNI', 'DHI']
selected_metric = st.sidebar.selectbox(
    "1. Select Irradiance Metric for Boxplot:",
    metric_options
)

# 2. Widget to select countries (Optional but good practice)
countries = df_combined['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect(
    "2. Select Countries for Analysis:",
    countries,
    default=countries
)

# Filter the data based on selection
df_filtered = df_combined[df_combined['Country'].isin(selected_countries)]


# --- Main Dashboard Layout ---

st.title("☀️ Cross-Country Solar Farm Site Comparison")
st.markdown("### Strategic Recommendation for MoonLight Energy Solutions")

# --- Tabs for organized viewing ---
tab1, tab2, tab3 = st.tabs(["📊 KPI Dashboard", "📦 Distribution Analysis", "📝 Data Table"])

with tab1:
    st.header("Solar Resource Ranking & Summary")
    
    col1, col2 = st.columns([1, 2])
    
    # 1. Display the KPI Ranking Bar Chart
    with col1:
        st.subheader("Mean GHI Ranking")
        fig_kpi = plot_kpi_ranking(df_filtered)
        st.pyplot(fig_kpi, use_container_width=True)
        st.info(f"**Best Site:** {df_filtered.groupby('Country')['GHI'].mean().idxmax()} has the highest average solar resource.")

    # 2. Display the Summary Table
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
    
    # 3. Display the Boxplot based on the sidebar widget
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