
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ---- PAGE SETUP ----
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("🧬 CORD-19 Data Explorer")
st.write("Explore patterns and insights from COVID-19 research papers.")

# ---- LOAD CLEANED DATA ----
@st.cache_data
def load_data():
    df = pd.read_excel(r"C:\Users\moen\Documents\metadata.xlsx", engine='openpyxl')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))
    return df

df = load_data()
st.success("✅ Data loaded successfully!")
st.write(f"Total Papers: {len(df):,}")

# ---- INTERACTIVE YEAR RANGE SLIDER ----
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.slider("Select Year Range:", min_year, max_year, (2019, 2020))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
st.write(f"Showing papers from {year_range[0]} to {year_range[1]}")
