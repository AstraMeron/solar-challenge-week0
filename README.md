☀️ 10 Academy Solar Data Discovery: Week 0 Challenge - Interim Submission

Author: Meron Tilahun

This repository is dedicated to the 10 Academy Week 0 challenge focused on understanding, exploring, and analyzing solar farm data from Benin, Sierra Leone, and Togo. This interim submission focuses on the completion of the foundational setup (Task 1) and the data cleaning/EDA approach (Task 2).

⚙️ Task 1: Environment Setup & Repository Structure

The project established a professional, version-controlled environment to ensure reproducibility and collaboration.

A. File Structure

notebooks/: Contains the Jupyter notebooks used for data profiling, cleaning, and Exploratory Data Analysis (EDA) approach (Task 2).

data/: (Ignored by Git) This folder holds the raw and cleaned CSV files.

requirements.txt: Lists all project dependencies.

B. Local Setup Instructions

To reproduce the development environment locally, please follow these steps:

Clone the Repository:

bash 
git clone [https://github.com/AstraMeron/solar-challenge-week0.git](https://github.com/AstraMeron/solar-challenge-week0.git) 
cd solar-challenge-week0


Create and Activate Virtual Environment (using venv):

# Create
python -m venv venv
# Activate (Windows PowerShell)
.\venv\Scripts\activate


Install Dependencies:

pip install -r requirements.txt


📊 Task 2: Data Profiling, Cleaning & EDA Approach

This section outlines the methodology applied to the Benin, Sierra Leone, and Togo datasets to ensure data quality and guide the cross-country comparison.

A. Data Cleaning and Preprocessing Approach

Profiling: Initial analysis included generating summary statistics and a missing value report to assess data quality and completeness.

Outlier Handling: Outliers in key variables (GHI, DNI, DHI, WS) were managed using the Z-score method (threshold > 3).

Missing Data: Isolated missing values were handled through median imputation on a per-column basis.

Time Series Indexing: Data was correctly indexed by time for accurate temporal analysis.

B. Exploratory Data Analysis (EDA) Outline

The EDA plan includes:

Temporal Analysis: Plotting key solar irradiance metrics over time.

Correlation Analysis: Using heatmaps to study the relationships between GHI, DNI, DHI, and environmental factors (e.g., Temperature).

Distribution Analysis: Using box plots and histograms to visualize the spread and concentration of solar resources.
