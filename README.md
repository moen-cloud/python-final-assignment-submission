# 🧬 CORD-19 Data Explorer

## Project Overview
This project explores COVID-19 research papers using the CORD-19 dataset. The analysis includes:

- Data loading and cleaning
- Basic exploratory data analysis (EDA)
- Visualization of publication trends, top journals, and title keywords
- An interactive Streamlit application to explore the dataset dynamically

The goal is to demonstrate key insights from COVID-19 research and provide an interactive interface for users to explore the data.

---

## Folder Structure


---

## Jupyter Notebook (`CORD19_analysis.ipynb`)

This notebook contains the full analysis workflow:

1. **Part 1: Data Loading and Exploration**
   - Loaded `metadata.csv` into a pandas DataFrame
   - Checked data structure, data types, and missing values

2. **Part 2: Data Cleaning**
   - Handled missing values in key columns
   - Converted `publish_time` to datetime format
   - Extracted `year` and calculated `abstract_word_count`

3. **Part 3: Analysis & Visualization**
   - Count of publications by year
   - Top journals publishing COVID-19 research
   - Most frequent words in titles
   - Word cloud of paper titles
   - Distribution of publications by source

4. **Part 4: Streamlit App**
   - Interactive year-range slider
   - Dynamic visualizations based on user selection

5. **Observations & Insights**
   - Summaries and interpretations of visualizations

**Note:** All cells have comments for clarity. Make sure to run **Kernel → Restart & Run All** before submission.

---

## Streamlit Application (`app.py`)

The Streamlit app provides an interactive exploration of the dataset.

### Features:

- Year range slider to filter papers
- Dynamic updates of statistics and visualizations
- Word cloud visualization for titles
- Count of publications by journals and sources

### How to Run:

1. Open a terminal/command prompt
2. Navigate to the project folder containing `app.py` and `metadata.csv`
3. Run the following command:

```bash
streamlit run app.py

Dataset

metadata.csv is a subset of the CORD-19 dataset

Columns used include: cord_uid, title, abstract, publish_time, year, journal, source_x, and abstract_word_count

Data cleaning handled missing values in publish_time, year, and journal

Requirements

Python 3.9+

Packages:
pandas
matplotlib
seaborn
streamlit
wordcloud
scikit-learn
