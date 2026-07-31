# 🎧 Spotify Music Data Analysis & Visualization

An exploratory data analysis project uncovering trends across 114,000 Spotify tracks using **Pandas** and **Matplotlib** — exploring artist popularity, genre distribution, danceability, loudness, explicit content, and top tracks.

## 📋 Overview

Using a large-scale Spotify tracks dataset, this project analyzes audio features and popularity metrics to answer questions like: Who are the most prolific and most popular artists on Spotify? Which genres score highest in popularity? Is there a relationship between how danceable a track is and how "happy" it sounds? How loud does music get as it becomes more danceable? What share of tracks contain explicit content?

## 📊 Dataset

The dataset (`spotify.csv`) contains **114,000 tracks** with **21 features**, including:

`track_id`, `artists`, `album_name`, `track_name`, `popularity`, `duration_ms`, `explicit`, `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `time_signature`, `track_genre`

## 📈 Visualizations

| Chart | Insight |
|---|---|
| **Top 10 Artists by Track Count & Top 10 Genres by Popularity** (side-by-side bar charts) | Compares the most prolific artists against the highest-scoring genres |
| **Danceability vs. Happiness (Valence)** (scatter plot, 700-track sample) | Explores whether more danceable tracks tend to sound happier |
| **Top 10 Popular Artists by Average Popularity Score** (horizontal bar) | Ranks artists by average track popularity rather than volume |
| **Explicit vs. Non-Explicit Content Distribution** (pie chart) | Shows the proportion of explicit content across the catalog |
| **Loudness Trend Across Danceability Levels** (line chart) | Tracks how average loudness shifts as danceability increases |
| **Top 10 Most Popular Tracks** (horizontal bar) | Highlights the single highest-scoring tracks by popularity |

All charts are automatically saved as high-resolution PNGs (300 DPI) to a `graphs/` folder.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-0ea5e9?style=flat-square&logo=plotly&logoColor=white)

## 📁 Files

| File | Purpose |
|---|---|
| `spotify.csv` | Raw Spotify tracks dataset |
| `spotify_analysis.py` | Main analysis & visualization script |
| `graphs/` | Auto-generated folder containing all output chart images |

## ▶️ How to Run

```bash
pip install pandas matplotlib
python spotify_analysis.py
```

Make sure a `graphs/` folder exists in the project directory before running, since each chart is saved there.

## 🔍 Key Steps

1. Load the dataset and inspect available columns
2. Identify the top 10 most prolific artists by track count
3. Identify the top 10 genres by average popularity
4. Sample the dataset to explore the danceability–valence (happiness) relationship
5. Rank artists by average popularity score
6. Analyze the explicit vs. non-explicit content split
7. Examine how loudness trends shift across danceability levels
8. Extract and rank the top 10 most popular individual tracks

## 🔮 Possible Improvements

- Add genre-level correlation analysis across multiple audio features (energy, tempo, acousticness)
- Build an interactive dashboard (e.g. with Plotly or Streamlit) for filterable exploration
- Add time-based trend analysis if release dates are available
- Cluster tracks by audio features to identify natural genre groupings

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
