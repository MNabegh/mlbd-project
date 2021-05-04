# Machine learning for behavioural data - Project

## Topic

Characterisation of the emotional state of mind by studying the music consumption of a user and use this data to built a refined personalized ephemeral recommender system.

## Research Questions

- Is it possible to identify a emotional state of mind of a user by studying their music consumption? 
- Is it possible to use them to improve a personalized and ephemeral recommender system? We could use a baseline 
- Can we extract common topics of song lyrics and use them as meaningful features?

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


## Methods

- Requests to scrape the lyrics
- Spotify API
- Create a baseline recommender system based on matrix factorization.
- Explore the new features and try to cluster the time series of the users.
- Use this information to improve the baseline recommender system.
