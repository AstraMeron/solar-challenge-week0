Unlocking Solar Potential in West Africa: A Data-Driven Strategy for MoonLight Energy Solutions
By Meron Tilahun Semu
Analytics Engineer, MoonLight Energy Solutions
Submission Date: November 12, 2025

Introduction: Shining a Light on Sustainable Energy
As the world races toward net-zero emissions, solar energy stands out as a beacon of hope—abundant, clean, and increasingly cost-effective. At MoonLight Energy Solutions, our mission is to harness this potential to drive operational efficiency and long-term sustainability. In this challenge, I dove into solar radiation datasets from three West African sites: Malanville in Benin, Bumbuna in Sierra Leone, and Dapaong in Togo. These datasets, spanning a full year of minute-level measurements, include key metrics like Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), ambient temperature (Tamb), relative humidity (RH), wind speed (WS), and module temperatures (TModA/B).

My analysis builds on the interim report submitted on November 9, 2025, where I outlined the setup and planning phases. Now, with the full workflow complete, this report synthesizes the findings into actionable insights. We'll explore how I set up a reproducible environment, profiled and cleaned the data, conducted exploratory data analysis (EDA), compared the sites, and built an interactive dashboard. The goal? To recommend the most promising site for utility-scale PV investments, backed by statistical evidence and visualizations.
Think of this as your roadmap to solar success—let's illuminate the path forward.

Task 1: Building a Solid Foundation – Git & Environment Setup
To ensure reproducibility and collaboration, I prioritized a professional development environment from the start.
Environment and Dependency Management

I created a dedicated Python virtual environment (venv) to isolate dependencies, avoiding conflicts with system-wide packages.
Key libraries like pandas, numpy, matplotlib, seaborn, scipy, and streamlit were pinned in requirements.txt for easy replication: pip install -r requirements.txt.
This setup guarantees that anyone cloning the repo can spin up the exact environment with a simple command.

Version Control and CI/CD

Initialized the repo as solar-challenge-week0 on GitHub, with branches like setup-task, eda-benin, eda-sierraleone, eda-togo, compare-countries, and dashboard-dev.
Enforced Git hygiene using Conventional Commits (e.g., init: add .gitignore, feat: implement Z-score cleaning, ci: add workflow for dependency checks).
Added a robust .gitignore to exclude data files (data/), notebooks checkpoints, and venv directories—keeping the repo lean and secure.
Implemented a basic CI workflow in .github/workflows/ci.yml that runs on every push: it installs dependencies and verifies the Python version, ensuring builds are reliable.

By merging these branches via pull requests, the main branch now holds a clean, versioned history. This foundation prevented issues downstream and aligns with best practices for data engineering workflows.


Task 2: Diving into the Data – Profiling, Cleaning, and EDA
With the environment ready, I tackled the raw datasets: benin-malanville.csv, sierraleone-bumbuna.csv, and togo-dapaong.csv. Each contains 525,600 entries (one year of minute-level data) across 18 columns.
Data Profiling and Cleaning Strategy
Profiling revealed high-quality data overall, but with anomalies:

Missing Values: Benin had ~1.5% nulls in some columns; Sierra Leone and Togo had 0% in key metrics but empty Comments and (for SL) Cleaning columns.
Descriptive Stats: Identified physical impossibilities like negative GHI/DNI/DHI (e.g., GHI min = -2 in Togo) and extreme outliers (e.g., ModA max >1400 W/m²).
Outlier Detection: Used Z-score (>3) to flag ~1-2% of rows per dataset; imputed with medians to preserve data volume.
Negative Fixes: Set ~250k negative irradiance values to 0 across sites, correcting sensor noise during nighttime.
Output: Exported cleaned CSVs (benin_clean.csv, etc.) to data/ (ignored in Git).

This process transformed raw data into reliable inputs, free of NaNs, duplicates, and impossibilities.
Exploratory Data Analysis (EDA)
EDA uncovered site-specific patterns. Here's a narrative walkthrough, with key visuals described (full notebooks in repo).
Temporal Trends

Annual Means: Benin and Togo show stable high GHI (>220 W/m² mean), with seasonal dips in wet months (Aug-Feb). Sierra Leone has a pronounced wet-season drop, averaging ~198 W/m².
Daily Cycles: Benin's peak GHI exceeds 800 W/m² at noon, with DNI > DHI (clear skies). Togo is similar (~700 W/m²). Sierra Leone peaks under 600 W/m², with DHI > DNI (cloudier).

Visual: Line plots of daily resampled GHI/DNI/DHI show Benin's superior stability.
Cleaning Impact

Benin: +32-34% irradiance gain post-cleaning (ModA: 232 → 307 W/m²).
Togo: Massive +137% delta when Cleaning=1 (likely optimal conditions).
Sierra Leone: No data (all nulls), highlighting a data gap.

Visual: Grouped bar charts emphasize the value of regular maintenance.
Correlations and Relationships

Heatmaps: Strong positive links between GHI and module temps (r~0.9), negative with RH (Benin: -0.35, Togo: -0.24, SL: -0.54—worst cloud impact).
Scatters: High GHI correlates with low RH and moderate winds.

Wind and Distributions

Wind Roses: Benin and Togo have good winds (>2 m/s from NE/SW), aiding cooling. Sierra Leone's are weak (~1.25 m/s max), risking thermal losses.
Histograms/Boxplots: GHI distributions are right-skewed and zero-inflated (nighttime); Benin's has the highest peaks.

Temperature and Humidity

Bubble Plots (GHI vs. Tamb, size=RH): High GHI in hot, dry conditions (low RH bubbles); low GHI in humid, cloudy periods.
Delta T (TMod - Tamb): Up to 30°C across sites, but SL's low winds amplify efficiency losses.

These insights reveal Benin and Togo as frontrunners, with Sierra Leone lagging due to clouds and poor cooling.

Task 3: Cross-Country Comparison – Ranking the Sites
Synthesizing the cleaned data, I compared metrics to rank sites for solar viability.
Metric Comparison

Boxplots: Benin's GHI 75th percentile (~750 W/m²) tops Togo (~700) and SL (~550), confirming higher peaks excluding non-irradiating hours.

GHI Ranking: Benin > Togo > SL.
Variability: Benin highest (more dynamic weather).

Statistical Testing

Kruskal-Wallis H-test on GHI: p < 0.05 (rejected null), confirming significant differences.

Key Observations

Benin offers the highest energy yield but with variability—ideal for maximum output.
Togo provides reliable direct beam (high DNI), least impacted by humidity—best for stability.
Sierra Leone has the lowest potential, dominated by diffuse light and thermal risks.

Interactive Dashboard – Visualizing Insights
To make insights accessible, I built a Streamlit app (app/main.py) deployed to Streamlit Community Cloud (link in README).

Features: Dropdowns to select metrics (GHI/DNI/DHI) and countries; dynamic boxplots and tables update on selection.
Usability: Intuitive sidebar controls, with interpretations like "Benin has the highest average solar resource."
Deployment: Fully functional at [app URL]; screenshots in dashboard_screenshots/.

This dashboard turns complex EDA into executive-friendly visuals, enhancing decision-making.

Strategic Recommendation: Prioritizing Benin for Solar Expansion
Based on the analysis, MoonLight should prioritize Benin (Malanville) for immediate investment:

Highest Yield: Superior GHI/DNI for maximum energy production.
Operational Edges: Quantifiable cleaning benefits and good winds mitigate risks.
Backup: Togo (Dapaong): For stable, low-variability sites.
De-prioritize Sierra Leone: High cloud cover and thermal losses make it riskier.

This data-driven strategy aligns with our sustainability goals, potentially boosting efficiency by 20-30% through targeted deployments. Next steps: Site visits and full feasibility studies.

Conclusion: From Data to Daylight
This Week 0 challenge transformed raw solar data into strategic gold. By mastering Git, EDA, and dashboards, I've laid a foundation for AI-driven innovation at MoonLight. The repo is live at [GitHub link], with all notebooks, cleans, and docs.
Let's keep pushing boundaries— the future is solar-powered.
References: Streamlit Docs, Python Guide.org, Atlassian Git Tutorials.