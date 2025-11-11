import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# NOTE: The original load_data() function has been removed. 
# Data is now loaded via file_uploader in app/main.py.

# Function to generate the boxplot figure
def plot_boxplot(df, metric):
    """Generates a boxplot for the selected metric across all countries."""
    
    if df.empty:
        # Return an empty figure or handle gracefully if the dataframe is empty
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_title("No data selected for boxplot.", fontsize=16)
        return fig
        
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Filter out zero values for better visualization of distribution
    df_filtered = df[df[metric] > 0] 
    
    # Check if df_filtered is empty after filtering
    if df_filtered.empty:
        ax.set_title(f"No non-zero data found for {metric}.", fontsize=16)
        return fig

    # Use 'tab10' palette for better contrast/color variety in Streamlit
    sns.boxplot(x='Country', y=metric, data=df_filtered, ax=ax, palette='tab10')
    ax.set_title(f'{metric} Distribution Across Countries (W/m²)', fontsize=16)
    ax.set_xlabel('Country')
    ax.set_ylabel(f'{metric} (W/m²)')
    ax.grid(axis='y', linestyle='--')
    
    plt.close(fig) # Prevent Matplotlib warnings by explicitly closing the figure
    return fig

# Function to generate the Top Regions Summary Table
def get_summary_table(df):
    """Calculates mean, median, and standard deviation for key metrics."""
    # Ensure the DataFrame is not empty before attempting calculation
    if df.empty:
        return pd.DataFrame() # Return empty DataFrame if no data

    summary_table = df.groupby('Country')[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
    # Flatten the columns for better display in Streamlit
    summary_table.columns = ['_'.join(col).strip() for col in summary_table.columns.values]
    
    return summary_table.rename(columns={
        'GHI_mean': 'GHI Mean (W/m²)', 'GHI_median': 'GHI Median (W/m²)', 'GHI_std': 'GHI Std Dev',
        'DNI_mean': 'DNI Mean (W/m²)', 'DNI_median': 'DNI Median (W/m²)', 'DNI_std': 'DNI Std Dev',
        'DHI_mean': 'DHI Mean (W/m²)', 'DHI_median': 'DHI Median (W/m²)', 'DHI_std': 'DHI Std Dev'
    })

# Function to generate the KPI Bar Chart
def plot_kpi_ranking(df):
    """Generates a bar chart ranking countries by average GHI."""
    fig, ax = plt.subplots(figsize=(8, 5))

    if df.empty:
        # Handle empty DataFrame gracefully
        ax.set_title('No data selected for ranking.', fontsize=14)
        return fig
        
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False).reset_index()
    avg_ghi.columns = ['Country', 'Mean GHI']

    # Use 'viridis' palette for consistency and adjust plot elements
    sns.barplot(x='Country', y='Mean GHI', data=avg_ghi, ax=ax, palette='viridis')
    ax.set_title('Country Ranking by Average GHI (W/m²)', fontsize=14)
    ax.set_ylabel('Mean GHI (W/m²)')
    ax.set_xlabel('Country')
    # Use a dynamic y-limit or remove it, as fixed limits can cut off bars
    # ax.set_ylim(150) 
    
    plt.close(fig) # Prevent Matplotlib warnings by explicitly closing the figure
    return fig