Machine learning for behavioural data - Project

1. Topic

Studying the consumption of music over time by creating lyrics related features such as topics and emotions. Create a p

2. Research Questions

- Can we identify user clusters from lyrics and music related features? Can we identify emotional state of minds of users?
- Is it possible to use them to improve a personalized and ephemeral recommender system? We could use a baseline 
- Can we extract common topics of song lyrics and use them as meaningful features?

3. Proposed dataset
- Last.fm Dataset - 1K users
- Spotify API: To find the mood of a song we can use the spotify API
- Lyrics from different web pages

4. Methods

- Requests or existing data set to associate the lyrics to the different songs.
- Use the spotify API to add information to every song. We extract 14 features:
  - Dancebility
  - Energy
  - Key
  - Loudness
  - Mode
  - Speechiness
  - Acousticness
  - Instrumentalness
  - Liveness
  - Valence (Positive or negative mood of a song)
  - Duration (in ms)
  - Tempo
  - Genres
  - Popularity
- Cluster the songs by using the newely created features by using different clustering methods.
- Cluster the songs by lyrics for topics or emotions (e.g spectral clustering, topic
modeling implementations)
- Analyse how this clusters are distributed over the time for different groups of user.

5. Different steps
- Scrape the lyrics and preprocess these in order to extract topics.
- Use the Spotify API to extract genres and audio related features.
- Create a baseline recommender system based on matrix factorization.
- Explore the new features and try to cluster the time series of the users.
- Use this information to improve the baseline recommender system.
