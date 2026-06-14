24JR1A05J5-S.ISAAC-WEEK-3_DATA_STORYTELLING_ASSIGNMENT

# Week 3 — Data Storytelling with Netflix Dataset

## 📌 Overview

This project is part of the AIML Internship Week 3 Assignment. It demonstrates Data Storytelling using the Netflix Dataset through an interactive Streamlit Dashboard. The project includes dataset exploration, visualizations, insights, and recommendations to understand Netflix content trends.

---

## 📁 Repository Structure

Data-Storytelling-App/

│

├── app.py → Streamlit Dashboard Application

├── netflix.csv → Netflix Dataset

├── README.md → Project Documentation

└── screenshots/

    ├── intro.png → Dataset Introduction

    ├── charts1.png → Content by Year & Top Countries

    ├── charts2.png → Ratings & Genre Analysis

    └── insights.png → Insights & Recommendations

---

## 📊 Dataset

**File:** netflix.csv

| Column       | Type    | Description          |
| ------------ | ------- | -------------------- |
| type         | String  | Movie or TV Show     |
| title        | String  | Title of the content |
| country      | String  | Country of origin    |
| release_year | Integer | Release year         |
| rating       | String  | Content rating       |
| listed_in    | String  | Genre category       |

### Dataset Summary

* Total Records: 10
* Content Types: Movies and TV Shows
* Features: 6 Columns
* Dataset Source: Netflix Content Sample Dataset

---

## 🎯 Assignment Parts Completed

| Part    | Topic                            | Status |
| ------- | -------------------------------- | ------ |
| Part 1  | Dataset Introduction             | ✅      |
| Part 2  | Data Loading & Cleaning          | ✅      |
| Part 3  | Exploratory Data Analysis        | ✅      |
| Part 4  | Content by Release Year Analysis | ✅      |
| Part 5  | Top Countries Analysis           | ✅      |
| Part 6  | Genre Analysis                   | ✅      |
| Part 7  | Rating Distribution Analysis     | ✅      |
| Part 8  | Movies vs TV Shows Comparison    | ✅      |
| Part 9  | Key Insights                     | ✅      |
| Part 10 | Recommendations                  | ✅      |
| Bonus   | Interactive Streamlit Dashboard  | ✅      |

---

## 📖 Dataset Introduction

The Netflix dataset contains information about Movies and TV Shows available on Netflix.

The dashboard provides:

* Number of Movies
* Number of TV Shows
* Number of Countries
* Content Growth Analysis
* Genre Distribution
* Rating Distribution
* Country-wise Content Analysis

---

## 📊 Exploratory Data Analysis (EDA)

### Visualization 1: Content by Release Year

Shows how Netflix content has grown over different years.

### Visualization 2: Top Countries

Displays countries producing the highest amount of Netflix content.

### Visualization 3: Top Genres

Shows the most popular genres available on Netflix.

### Visualization 4: Rating Distribution

Displays the distribution of content ratings.

### Visualization 5: Movies vs TV Shows

Compares the number of Movies and TV Shows.

---

## 🔍 Key Insights

* Most content comes from the United States.
* Netflix content increased significantly after 2015.
* Drama is one of the most common genres.
* Movies outnumber TV Shows in the dataset.
* Content production has shown continuous growth.

---

## 💡 Recommendations

* Increase regional language content.
* Expand underrepresented genres.
* Invest more in emerging markets.
* Produce additional original TV Shows.
* Improve content diversity across countries.

---

## 🚀 How to Run

### Step 1: Install Libraries

pip install streamlit plotly

### Step 2: Upload Dataset

Upload netflix.csv into Google Colab.

### Step 3: Create Streamlit Application

Run the app.py code provided in the notebook.

### Step 4: Launch Dashboard

streamlit run app.py

### Step 5: Create Public URL

Use LocalTunnel:

npx localtunnel --port 8501

### Step 6: Open Dashboard

Open the generated URL and explore the dashboard.

---

## 📸 Screenshots Required

### Screenshot 1

Dataset Introduction

* Movies Count
* TV Shows Count
* Countries Count

File Name:

intro.png

### Screenshot 2

Charts Section

* Content by Release Year
* Top Countries

File Name:

charts1.png

### Screenshot 3

Charts Section

* Rating Distribution
* Top Genres

File Name:

charts2.png

### Screenshot 4

Insights and Recommendations

File Name:

insights.png

---

## 📦 Libraries Used

| Library   | Purpose                   |
| --------- | ------------------------- |
| pandas    | Data loading and analysis |
| streamlit | Interactive dashboard     |
| plotly    | Data visualizations       |

---

## 👤 Author

Name: S. ISAAC

Roll Number: 24JR1A05J5

Internship: AIML Internship

Project: Data Storytelling with Netflix Dataset

Technology Used: Python, Pandas, Plotly, Streamlit
