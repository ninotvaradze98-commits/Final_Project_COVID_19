# Final Project: COVID-19 Case Dynamics Before and After Vaccination


## Project Goal
This project analyzes how COVID-19 case trends and mortality rates  changed before and after vaccination campaigns. The analysis compares three countries representing regional difference in Asia, Europe, United States.

The project demonstates:
- Data loading and cleaning
- Data analysis
- Visualization of trends
- Interpretation of results

---

## Core Research Question
How did COVID-19 case trends and mortality rates change after vaccination campaigns started in different countries?

---

## Data Sources
The analysis uses publicly available COVID-19 data from Our World in Data (https://ourworldindata.org/covid-cases)”

The dataset includes:
- COVID-19 case counts
- COVID-19 death counts
- Vaccination statistics
- Population data

The data is loaded directly from a public URL using pandas

---

## Project Structure
- main.py - runs the full analysis pipeline
- deta_loader.py - loads the dataset
- cleaing.py - cleans the data  and filters selected countries
- analysis.py - defines vaccination periods and creates summary tables
- visualization.py - creates charts and visualizations
- covid_data/ - stores generated CSV files
- visualizations/ - stores generated PNG files

---

## Data Loading & Preparation
The dataset is loaded using **pandas**.

Data preparation includes:
- Handling missing values
- Converting the `date` column to datetime format
- Filtering relevant columns:
  - `date`
  - `location` (country)
  - `new_cases`
  - `new_deaths`
  - `people_vaccinated`
  - `people_fully_vaccinated`
- Selecting three countries for analysis:
  - Japan
  - Germany
  - United States

---

## Define Analysis Periods
For each country, a vaccination start date is identified based on the first day with recorded vaccinations.

The dataset is then split into:
- **Pre-vaccination period**
- **Post-vaccination period**

This logic is applied independently for each country.

---

## Data Analysis
The analysis computes:
- Average daily new COVID-19 cases before and after vaccination
- Average daily new COVID-19 deaths before and after vaccination
- Percentage change between pre- and post-vaccination periods

The implementation uses pandas groupby operations and aggregation functions such as mean() and min() to summarize data by country and vaccination period. Reusable helper functions are implemented for data cleaning, analysis, and visualization to keep the code modular and easy to maintain.

---

## Visualization
The following charts are generated using **matplotlib**:


### Line Charts
- Daily new COVID-19 cases per country
- Weekly (7-day rolling average) new COVID-19 cases per country
- Vaccination start dates highlighted with vertical dashed lines


### Bar Charts
- Comparison of average daily new cases before vs after vaccination
- Comparison of average daily new deaths before vs after vaccination

All charts include:
- Titles
- Labeled axes
- Legends (where applicable)

Charts are saved in the `visualizations/` directory.

---

## Results
The analysis shows that for all selected countries:
- Average daily new COVID-19 cases increased after vaccination campaigns began
- The increase in reported cases varied by country
- Average daily new deaths showed smaller increases compared to case counts

These results suggest that while infections continued after vaccination campaigns started, vaccinations may have contributed to limiting severe outcomes.

The analysis only describes the data and does not prove cause-and-effect relationships.

