# Machine learning for behavioural data - Project

## Public link for the repository
[Project repository](https://github.com/MNabegh/mlbd-project)

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
- Cluster the songs by using the newely created features by using different clustering methods.
- Cluster the songs by lyrics for topics or emotions (e.g spectral clustering, topic
modeling implementations)

- Use lyricsgenius to scrape the lyrics
- Implement topic modeling using Latent Dirichlet Allocation (LDA) 
- Evaluate the quality of the created topics

- Build a baseline collabritive filtering model based on shallow matrix factorization
- Build a baseline deep collabritive filtering model
- Build a hybrid deep model using collabritive filtering and content based features
- Implement evaluation metrics for the recommender system
- Perform in depth analysis for the recommender system

## ??How to??
- 'scrape_spotify_info.py': Contains the code that uses the Spotify API to extract the audio features from the Spotify database. 
- 'Genres_map.ipynb': The creation of the genres map is done in this notebook. It illustrates how we build the graph and construct the embeddings we will use for the recommender system.
- 'exploratory_analysis.ipynb': provides a short summary on the used datasets and their features.
- 'recommender_system.ipynb': contains the code that reads the lastFM data performs the preprocessing, and then trains the recommender system and performs the evaluation, this requires all data files except lastFM to be already available and accessible.


## Methods

- Requests to scrape the lyrics
- Spotify API
- Create a baseline recommender system based on matrix factorization.
- Use this information to improve the baseline recommender system by building hybrid recommender system.
- Implement
