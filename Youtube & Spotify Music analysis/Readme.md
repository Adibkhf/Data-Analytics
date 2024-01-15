# Analysis of Song Popularity on Spotify and YouTube

## Project Overview

This project involves a comprehensive analysis of song popularity on two major digital platforms: Spotify and YouTube. Utilizing a rich dataset from Kaggle, the project aims to decipher the correlation between various musical characteristics and the online engagement metrics of songs. The insights derived from this analysis are anticipated to be valuable for artists, producers, and marketers in the music industry.

## Objectives

1. **Understand the Relationship Between Spotify's Audio Features and Song Popularity**: Exploring how features like danceability, energy, and loudness correlate with a song's popularity on Spotify and YouTube.
2. **Identify Patterns and Trends in Music Consumption and Audience Preferences**: Analyzing audience consumption habits and preferences in musical characteristics.
3. **Provide Data-Driven Insights for Industry Stakeholders**: Assisting industry players in making informed decisions based on audience preferences and song characteristics.

## Dataset Description

The dataset includes the following variables for each song:

- **Track**: Name of the song as on Spotify.
- **Artist**: Name of the artist.
- **Url_spotify**: The URL of the song on Spotify.
- **Album**: The album containing the song on Spotify.
- **Album_type**: Whether the song is released as a single or in an album.
- **Uri**: Spotify link for the song.
- **Danceability, Energy, Key, Loudness, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, Duration_ms**: Various musical characteristics.
- **Stream**: Number of streams on Spotify.
- **Url_youtube, Title, Channel, Views, Likes, Comments, Description, Licensed, official_video**: Corresponding YouTube metrics.

## Tools and Technologies Used

- **Python**: For data cleaning, manipulation, and exploratory data analysis.
- **SQL**: For data querying and manipulation.
- **Jupyter Notebook**: For conducting and presenting data analysis.
- **Pandas & Matplotlib**: For data processing and visualization.

## Repository Structure

- `.ipynb_checkpoints`: Contains checkpoints of Jupyter notebooks.
- `advanced_pandas_queries.txt`: Advanced queries used in data analysis.
- `EDA Analysis pandas.py`: Python script for Exploratory Data Analysis using Pandas.
- `EDA Analysis SQL.sql`: SQL script for Exploratory Data Analysis.
- `pic1.png`, `pic2.png`, `pic3.png`: Visualizations and charts.
- `Spotify_Youtube.csv`: Combined dataset of Spotify and YouTube metrics.
- `Youtube Cleaned data.xlsx`: Cleaned YouTube data.
- `Youtube.ipynb`: Jupyter notebook for YouTube data analysis.

## How to Run

1. **Data Setup**: Ensure `Spotify_Youtube.csv` and `Youtube Cleaned data.xlsx` are placed in the project directory.
2. **Jupyter Notebooks**: Open `Youtube.ipynb` for YouTube analysis. Run `EDA Analysis pandas.py` for Spotify data analysis.
3. **SQL Analysis**: Execute `EDA Analysis SQL.sql` in an SQL environment for additional insights.

## Conclusions

The project concludes with a set of actionable insights for music industry stakeholders, highlighting the key factors that contribute to a song's popularity on Spotify and YouTube. These insights are instrumental in shaping future music production and marketing strategies.

