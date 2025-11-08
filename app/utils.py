import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the data folder from the perspective of the 'app/' directory
DATA_PATH = 'notebooks/data/' 

# Function to load and combine all data
def load_data():
    """Loads, cleans, and combines solar data from all three countries."""
    
    try:
        # Files are accessed using the full path from the project root
        df_benin = pd.read_csv(f'{DATA_PATH}benin_clean.csv', index_col=0, parse_dates=True)
        df_sierra_leone = pd.read_csv(f'{DATA_PATH}sierra_leone_clean.csv', index_col=0, parse_dates=True)
        df_togo = pd.read_csv(f'{DATA_PATH}togo_clean.csv', index_col=0, parse_dates=True)
    except FileNotFoundError as e:
        # This error message should now clearly show the path being attempted
        return None, f"Error: Cleaned data files not found. Tried to access files in: {DATA_PATH}. Please verify the folder structure."

    # Add country identifier and concatenate
    df_benin['Country'] = 'Benin'
    df_sierra_leone['Country'] = 'Sierra Leone'
    df_togo['Country'] = 'Togo'
    
    df_combined = pd.concat([
        df_benin[['GHI', 'DNI', 'DHI', 'Country']], 
        df_sierra_leone[['GHI', 'DNI', 'DHI', 'Country']], 
        df_togo[['GHI', 'DNI', 'DHI', 'Country']]
    ], ignore_index=True)
    
    return df_combined, None

# Function to generate the boxplot figure
def plot_boxplot(df, metric):
    """Generates a boxplot for the selected metric across all countries."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Filter out zero values for better visualization of distribution
    df_filtered = df[df[metric] > 0] 
    
    sns.boxplot(x='Country', y=metric, data=df_filtered, ax=ax, palette='viridis')
    ax.set_title(f'{metric} Distribution Across Countries (W/m²)', fontsize=16)
    ax.set_xlabel('Country')
    ax.set_ylabel(f'{metric} (W/m²)')
    ax.grid(axis='y', linestyle='--')
    
    # Return the Matplotlib figure object
    return fig

# Function to generate the Top Regions Summary Table
def get_summary_table(df):
    """Calculates mean, median, and standard deviation for key metrics."""
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
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False).reset_index()
    avg_ghi.columns = ['Country', 'Mean GHI']

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Country', y='Mean GHI', data=avg_ghi, ax=ax, palette='plasma')
    ax.set_title('Country Ranking by Average GHI (W/m²)', fontsize=14)
    ax.set_ylabel('Mean GHI (W/m²)')
    ax.set_xlabel('Country')
    ax.set_ylim(150)
    
    return fig