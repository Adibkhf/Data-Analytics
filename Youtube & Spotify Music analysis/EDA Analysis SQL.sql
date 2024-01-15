-- Create a table to store the data
CREATE TABLE music_data (
    Track VARCHAR(255),
    Artist VARCHAR(255),
    Url_spotify VARCHAR(255),
    Album VARCHAR(255),
    Album_type VARCHAR(20),
    Uri VARCHAR(255),
    Danceability FLOAT,
    Energy FLOAT,
    Key INT,
    Loudness FLOAT,
    Speechiness FLOAT,
    Acousticness FLOAT,
    Instrumentalness FLOAT,
    Liveness FLOAT,
    Valence FLOAT,
    Tempo FLOAT,
    Duration_ms INT,
    Stream INT,
    Url_youtube VARCHAR(255),
    Title VARCHAR(255),
    Channel VARCHAR(255),
    Views INT,
    Likes INT,
    Comments INT,
    Licensed VARCHAR(10),
    official_video INT,
    Duration_min FLOAT
);

-- 2. Ingest data from an external file
-- This step is typically done through a MySQL client or command line tool.
-- For example, using MySQL Workbench or a command like:
-- LOAD DATA INFILE 'path_to_your_csv_file.csv' 
-- INTO TABLE car_market_data
-- FIELDS TERMINATED BY ',' ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

-- 3. Example Queries

-- Average Danceability by Album Type
SELECT Album_type, AVG(Danceability) AS average_danceability
FROM music_data
GROUP BY Album_type;

-- Top 10 Tracks with Highest Energy Levels
SELECT Track, Energy
FROM music_data
ORDER BY Energy DESC
LIMIT 10;

-- Count of Tracks per Key
SELECT Key, COUNT(*) AS track_count
FROM music_data
GROUP BY Key;

-- Median Duration (in minutes) for each Album Type
SELECT Album_type, MEDIAN(Duration_min) AS median_duration
FROM music_data
GROUP BY Album_type;

-- Total Number of Streams per Artist
SELECT Artist, SUM(Stream) AS total_streams
FROM music_data
GROUP BY Artist;

-- Average Loudness and Tempo for Each Key
SELECT Key, AVG(Loudness) AS average_loudness, AVG(Tempo) AS average_tempo
FROM music_data
GROUP BY Key;

-- Tracks with Maximum and Minimum Speechiness
SELECT *
FROM music_data
WHERE Speechiness = (SELECT MAX(Speechiness) FROM music_data)
OR Speechiness = (SELECT MIN(Speechiness) FROM music_data);

-- Total Views per Channel
SELECT Channel, SUM(Views) AS total_views
FROM music_data
GROUP BY Channel;

-- Top 5 Most Commented Videos
SELECT Title, Comments
FROM music_data
ORDER BY Comments DESC
LIMIT 5;

-- Average Valence for Licensed and Non-Licensed Content
SELECT Licensed, AVG(Valence) AS average_valence
FROM music_data
GROUP BY Licensed;

-- Number of Unique Tracks per Artist
SELECT Artist, COUNT(DISTINCT Track) AS unique_tracks
FROM music_data
GROUP BY Artist;

-- List of Tracks with Acousticness over 0.8
SELECT Track
FROM music_data
WHERE Acousticness > 0.8;

-- Total Likes for Official Videos
SELECT SUM(Likes) AS total_likes
FROM music_data
WHERE official_video = 1;

-- Average Duration for Each Album Type
SELECT Album_type, AVG(Duration_ms) AS average_duration
FROM music_data
GROUP BY Album_type;

-- Tracks with Danceability Lower Than 0.3 and Energy Higher Than 0.7
SELECT *
FROM music_data
WHERE Danceability < 0.3 AND Energy > 0.7;

-- Top 10 Most Liked Tracks
SELECT Track, Likes
FROM music_data
ORDER BY Likes DESC
LIMIT 10;

-- Distribution of Tracks by Album Type
SELECT Album_type, COUNT(*) AS track_count
FROM music_data
GROUP BY Album_type;

-- Average Tempo for Tracks with High Valence (> 0.75)
SELECT AVG(Tempo) AS average_tempo
FROM music_data
WHERE Valence > 0.75;

-- Number of Tracks with Liveness above 0.8
SELECT COUNT(*) AS liveness_above_0_8
FROM music_data
WHERE Liveness > 0.8;

-- Tracks with High Instrumentalness and Low Speechiness
SELECT *
FROM music_data
WHERE Instrumentalness > 0.8 AND Speechiness < 0.1;

-- Count of Tracks by Artist for Top 10 Artists by Stream Count
SELECT Artist, COUNT(*) AS track_count
FROM music_data
WHERE Artist IN (SELECT Artist FROM music_data GROUP BY Artist ORDER BY SUM(Stream) DESC LIMIT 10)
GROUP BY Artist;

-- Tracks with Duration Longer than the 90th Percentile
SELECT *
FROM music_data
WHERE Duration_ms > (SELECT PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY Duration_ms) FROM music_data);

-- Standard Deviation of Tempo and Loudness for Each Album Type
SELECT Album_type, STDDEV(Tempo) AS tempo_stddev, STDDEV(Loudness) AS loudness_stddev
FROM music_data
GROUP BY Album_type;

-- Bottom 5 Tracks with Least Views
SELECT Track, Views
FROM music_data
ORDER BY Views ASC
LIMIT 5;

-- Tracks with 'official_video' and More than 1 Million Views
SELECT *
FROM music_data
WHERE official_video = 1 AND Views > 1000000;

-- Proportion of Tracks with Liveness Above Average
SELECT COUNT(*) AS liveness_above_average_count, (SELECT COUNT(*) FROM music_data) AS total_tracks
FROM music_data
WHERE Liveness > (SELECT AVG(Liveness) FROM music_data);

-- Artists with Only One Track in the Dataset
SELECT Artist
FROM music_data
GROUP BY Artist
HAVING COUNT(*) = 1;

-- Average Number of Comments for Different Album Types
SELECT Album_type, AVG(Comments) AS average_comments
FROM music_data
GROUP BY Album_type;

-- Tracks with Valence in the Top 25% and Energy in the Bottom 25%
SELECT *
FROM music_data
WHERE Valence > (SELECT PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY Valence) FROM music_data)
AND Energy < (SELECT PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY Energy) FROM music_data);
