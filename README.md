# ☀️ Solar Data Discovery: Cross-Country Solar Farm Analysis (Final Submission)

## Project Overview

This repository contains the analysis and interactive dashboard developed for **MoonLight Energy Solutions**.  
The goal was to perform a **data-driven analysis** of solar irradiance data from three West African countries—**Benin, Sierra Leone, and Togo**—to identify high-potential regions for solar farm installation.

The final deliverable is an **interactive Streamlit dashboard**, successfully deployed to the cloud, that allows stakeholders to compare key solar metrics (**GHI, DNI, DHI**) across the three countries.

---

## 🚀 Live Application & Deployment Success

The interactive dashboard is fully deployed and accessible via the public **Streamlit Community Cloud** link.

**Live Dashboard URL:**  
🔗 [https://solar-challenge-dashboard.streamlit.app/](https://solar-challenge-dashboard.streamlit.app/)

### Deployment Instructions

The application is designed to be fully cloud-compatible, using Streamlit's **file uploader mechanism** instead of local file paths.

1. Click the **Live Dashboard URL** above.  
2. In the **Configuration sidebar**, use the file uploader to provide the three required cleaned CSV files:
   - `benin_clean.csv`
   - `sierra_leone_clean.csv`
   - `togo_clean.csv`  
3. Once uploaded, the analysis dashboard will load automatically.

---

## 🛠️ Environment Setup & Local Run

To run the analysis notebooks or the dashboard locally, follow these steps:

### Prerequisites

- Python 3.8+
- Git

---

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/AstraMeron/solar-challenge-week0.git
    cd solar-challenge-week0
    ```

2.  **Create and Activate Virtual Environment (using venv):**

    ```bash
    # Create the environment
    python -m venv venv

    # Activate (Windows PowerShell)
    .\venv\Scripts\activate

    # Activate (Linux/macOS)
    source venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit Dashboard Locally:**

    ```bash
    streamlit run app/main.py
    ```

    The app will open in your browser, and you can use the file uploader in the sidebar to load the data.

---

## 📝 Task Summaries (Completed Work)

1.  **Task 1: Git & Environment Setup**  
✅ Completed:  
Initialized repository, established a Python virtual environment, documented dependencies in `requirements.txt`, and implemented a basic CI pipeline using GitHub Actions (`.github/workflows/ci.yml`) to ensure code integrity.

2.  **Task 2 & 3: Data Analysis**  
✅ Completed:  
Comprehensive data cleaning (outlier and missing value handling), time series analysis, and correlation studies were performed across all three datasets.

**Strategic Comparison:**  
The analysis concluded with a cross-country comparison (Task 3), using statistical summaries (mean, median, standard deviation) and visualizations (Boxplots, KPI Ranking) to determine the highest-potential sites.

3.  **Bonus Task: Interactive Dashboard & Deployment**  
✅ Completed:  
Developed an interactive dashboard using **Streamlit** (`app/main.py`) to visualize the cross-country comparisons.

**Cloud-Ready:**  
The application was refactored to use Streamlit’s multi-file uploader for data input, successfully eliminating dependencies on local file paths.

**Deployment Success:**  
The dashboard was successfully deployed to the **Streamlit Community Cloud**.  

🔗 [https://solar-challenge-dashboard.streamlit.app/](https://solar-challenge-dashboard.streamlit.app/)
