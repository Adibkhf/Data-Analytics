import pandas as pd 

# Load the DataFrame from an Excel file
df = pd.read_excel('Youtube Cleaned data.xlsx')

# Average Danceability by Album Type
average_danceability_by_album_type = df.groupby('Album_type')['Danceability'].mean()

# Top 10 Tracks with Highest Energy Levels
top_10_tracks_highest_energy = df.nlargest(10, 'Energy')[['Track', 'Energy']]

# Count of Tracks per Key
count_tracks_per_key = df['Key'].value_counts()

# Median Duration (in minutes) for each Album Type
median_duration_per_album_type = df.groupby('Album_type')['Duration_min'].median()

# Total Number of Streams per Artist
total_streams_per_artist = df.groupby('Artist')['Stream'].sum()

# Average Loudness and Tempo for Each Key
average_loudness_tempo_per_key = df.groupby('Key')[['Loudness', 'Tempo']].mean()

# Tracks with Maximum and Minimum Speechiness
max_min_speechiness_tracks = df[(df['Speechiness'] == df['Speechiness'].max()) | (df['Speechiness'] == df['Speechiness'].min())]

# Total Views per Channel
total_views_per_channel = df.groupby('Channel')['Views'].sum()

# Top 5 Most Commented Videos
top_5_most_commented_videos = df.nlargest(5, 'Comments')[['Title', 'Comments']]

# Average Valence for Licensed and Non-Licensed Content
average_valence_licensed = df.groupby('Licensed')['Valence'].mean()

# Number of Unique Tracks per Artist
unique_tracks_per_artist = df.groupby('Artist')['Track'].nunique()

# List of Tracks with Acousticness over 0.8
tracks_acousticness_over_0_8 = df[df['Acousticness'] > 0.8]['Track']

# Total Likes for Official Videos
total_likes_official_videos = df[df['official_video'] == 1]['Likes'].sum()

# Average Duration for Each Album Type
average_duration_per_album_type = df.groupby('Album_type')['Duration_ms'].mean()

# Tracks with Danceability Lower Than 0.3 and Energy Higher Than 0.7
danceability_energy_filter = df[(df['Danceability'] < 0.3) & (df['Energy'] > 0.7)]

# Top 10 Most Liked Tracks
top_10_most_liked_tracks = df.nlargest(10, 'Likes')[['Track', 'Likes']]

# Distribution of Tracks by Album Type
tracks_distribution_by_album_type = df['Album_type'].value_counts()

# Average Tempo for Tracks with High Valence (> 0.75)
average_tempo_high_valence = df[df['Valence'] > 0.75]['Tempo'].mean()

# Number of Tracks with Liveness above 0.8
tracks_liveness_above_0_8 = df[df['Liveness'] > 0.8].shape[0]

# Tracks with High Instrumentalness and Low Speechiness
high_instrumentalness_low_speechiness = df[(df['Instrumentalness'] > 0.8) & (df['Speechiness'] < 0.1)]

# Count of Tracks by Artist for Top 10 Artists by Stream Count
top_artists = df.groupby('Artist')['Stream'].sum().nlargest(10).index
count_tracks_by_artist_top_10 = df[df['Artist'].isin(top_artists)].groupby('Artist').size()

# Tracks with Duration Longer than the 90th Percentile
duration_90th = df['Duration_ms'].quantile(0.9)
tracks_longer_than_90th_percentile = df[df['Duration_ms'] > duration_90th]

# Standard Deviation of Tempo and Loudness for Each Album Type
std_tempo_loudness_per_album_type = df.groupby('Album_type')[['Tempo', 'Loudness']].std()

# Bottom 5 Tracks with Least Views
bottom_5_tracks_least_views = df.nsmallest(5, 'Views')

# Tracks with 'official_video' and More than 1 Million Views
tracks_official_video_1_million_views = df[(df['official_video'] == 1) & (df['Views'] > 1e6)]

# Proportion of Tracks with Liveness Above Average
proportion_tracks_liveness_above_average = df[df['Liveness'] > df['Liveness'].mean()].shape[0] / df.shape[0]

# Artists with Only One Track in the Dataset
artists_with_only_one_track = df.groupby('Artist').filter(lambda x: len(x) == 1)['Artist']

# Average Number of Comments for Different Album Types
average_comments_per_album_type = df.groupby('Album_type')['Comments'].mean()

# Tracks with Valence in the Top 25% and Energy in the Bottom 25%
valence_top_25_energy_bottom_25 = df[(df['Valence'] > df['Valence'].quantile(0.75)) & (df['Energy'] < df['Energy'].quantile(0.25))]


