%%writefile app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv("netflix.csv")

# Title
st.title("🎬 Netflix Data Storytelling App")

# -----------------------------
# Dataset Introduction
# -----------------------------
st.header("📖 Dataset Introduction")

movies = len(df[df["type"] == "Movie"])
tvshows = len(df[df["type"] == "TV Show"])
countries = df["country"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Movies", movies)
col2.metric("TV Shows", tvshows)
col3.metric("Countries", countries)

st.dataframe(df)

# -----------------------------
# EDA
# -----------------------------
st.header("📊 Exploratory Data Analysis")

# Content by Year
st.subheader("Content by Release Year")

year_count = df["release_year"].value_counts().sort_index()

fig1 = px.line(
    x=year_count.index,
    y=year_count.values,
    labels={"x":"Year","y":"Content Count"},
    title="Content Released by Year"
)

st.plotly_chart(fig1)

# Top Countries
st.subheader("Top Countries")

country_count = df["country"].value_counts().head(10)

fig2 = px.bar(
    x=country_count.index,
    y=country_count.values,
    labels={"x":"Country","y":"Titles"},
    title="Top Countries"
)

st.plotly_chart(fig2)

# Top Genres
st.subheader("Top Genres")

genre_count = df["listed_in"].value_counts().head(10)

fig3 = px.bar(
    x=genre_count.index,
    y=genre_count.values,
    labels={"x":"Genre","y":"Count"},
    title="Genre Popularity"
)

st.plotly_chart(fig3)

# Ratings Distribution
st.subheader("Ratings Distribution")

rating_count = df["rating"].value_counts()

fig4 = px.pie(
    values=rating_count.values,
    names=rating_count.index,
    title="Ratings Distribution"
)

st.plotly_chart(fig4)

# Movies vs TV Shows
st.subheader("Movies vs TV Shows")

type_count = df["type"].value_counts()

fig5 = px.pie(
    values=type_count.values,
    names=type_count.index,
    title="Movies vs TV Shows"
)

st.plotly_chart(fig5)

# -----------------------------
# Insights
# -----------------------------
st.header("🔍 Insights")

st.write("✅ Most content comes from the United States.")
st.write("✅ Netflix content increased significantly after 2018.")
st.write("✅ Drama and Action are among the most popular genres.")
st.write("✅ Movies are more common than TV Shows.")
st.write("✅ Netflix continues expanding its content library every year.")

# -----------------------------
# Recommendations
# -----------------------------
st.header("💡 Recommendations")

st.write("➡ Invest more in regional content.")
st.write("➡ Expand underrepresented genres.")
st.write("➡ Increase original TV Shows.")
st.write("➡ Target emerging international markets.")
