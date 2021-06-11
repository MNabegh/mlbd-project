# Machine learning for behavioural data - Project

## Topic

Characterisation of the emotional state of mind by studying the music consumption of a user and leverage this data to built a refined personalized ephemeral recommender system.

## Research Questions
- To what extend do audio and lyrics based features improve a hybrid recommender system when compared to a simple collaborative filtering recommender system?
- Can we extract common topics of song lyrics and use them as meaningful features?
- Can we build a continous embedding for topics?

## Proposed dataset
- Last.fm Dataset - 1K users
- Spotify API: To find the mood of a song we can use the spotify API
- Lyrics from different web pages

## Experimental plan

- Requests or existing data set to associate the lyrics to the different songs.
- Use the spotify API to add information to every song. We extract 14 features e.g.:

| Dancebility | Energy | Key | Loudness | Mode | Speechiness | Acousticness | Instrumentalness | Liveness | Valence | Duration (in ms) | Tempo | Genres | Popularity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.627 | 0.871 | 9.0 | -8.742 | 0.0 | 0.0328 | 0.09620 | 0.358000 | 0.1090 | 0.9560 | 89.102 | 272707.0 | ['nu jazz', 'electro jazz'] | 42.0 |


Valence (Positive or negative mood of a song)
- Create a baseline recommender system
- Cluster the songs by using the newely created features by using different clustering methods.
- Cluster the songs by lyrics for topics or emotions (e.g spectral clustering, topic
modeling implementations)
- Identify clusters of user doing time series analysis

## ??How to??
- 'scrape_spotify_info.py': Contains the code that uses the Spotify API to extract the audio features from the Spotify database. 
- 'Genres_map.ipynb': The creation of the genres map is done in this notebook. It illustrates how we build the graph and construct the embeddings we will use for the recommender system.


## Methods

- Requests to scrape the lyrics
- Spotify API
- Create a baseline recommender system based on matrix factorization.
- Explore the new features and try to cluster the time series of the users.
- Use this information to improve the baseline recommender system.
