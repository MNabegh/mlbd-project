import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
from tqdm import tqdm
import re
from collections import Counter
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from itertools import chain
import csv
import time
import numpy as np


def create_songs_df(min_users=5):
    def drop_unknown_songs(df, min_users=min_users):
        df_no_duplicates = df.drop_duplicates(subset=['user', 'artist', 'song'])
        counts = df_no_duplicates[['song', 'artist']].value_counts().to_frame('song_count')
        accepted_songs = counts[counts['song_count'] > min_users].reset_index()
        df.loc[:, 'song + artist'] = df['song'] + '/' + df['artist']
        df = df[df['song + artist'].isin((accepted_songs['song'] + '/' + accepted_songs['artist']).values)]
        df = df.drop(columns='song + artist')
        return df

    df = pd.read_csv('../data/lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv',
                     error_bad_lines=False,
                     warn_bad_lines=True, sep='\t',
                     names=['user', 'timestamp', 'artist-id', 'artist', 'song-id', 'song'])

    df = df[['user', 'timestamp', 'artist', 'song']]
    # df = drop_unknown_songs(df, min_users=5)
    df = df.dropna(subset=['song'])
    df_songs = df.drop_duplicates(subset=['song', 'artist']).drop(columns=['user', 'timestamp'])
    df_songs.to_csv('../data/songs_frame.csv')


def extract_spotify_uri(song, artist, sp):
    original_artist = artist
    original_song = song
    artist = re.sub('\&.+$', '', artist)
    artist = re.sub('^[t|T]he ', '', artist)
    artist = artist.lower()

    song = re.sub('\(.+\)', '', song)
    song = re.sub("'", "", song)
    song = re.sub('\[.+\]', '', song)
    song = re.sub('dalef', 'dalek', song)
    song = song.lower()

    q = 'artist:{} track:{}'.format(artist, song)
    results = sp.search(q=q, limit=1, type='track')
    track_item = results['tracks']['items']
    if len(track_item) > 0:
        track_uri = track_item[0]['uri']
        album_uri = track_item[0]['album']['uri']
        artists = track_item[0]['artists']
        return original_artist, original_song, track_uri, album_uri, [artist['uri'] for artist in artists]
    else:
        artist = re.sub('squarepusher', 'shobaleader one', artist)

        song = re.sub(', part 2', ', pt. 2', song)
        song = re.sub('/.+]', '', song)

        q = '{} track:{}'.format(artist, song)
        results = sp.search(q=q, limit=1, type='track')
        track_item = results['tracks']['items']
        if len(track_item) > 0:
            album_uri = track_item[0]['album']['uri']
            track_uri = track_item[0]['uri']
            artists = track_item[0]['artists']
            return original_artist, original_song, track_uri, album_uri, [artist['uri'] for artist in artists]
        else:
            return original_artist, original_song, None, None, None


def create_spotify_uri_frame(sp, input_path='../data/songs_frame.csv', output_path='../data/spotify_uris.csv'):
    df_songs = pd.read_csv(input_path)
    df_songs = df_songs[df_songs['song'].apply(lambda x: len(x)) < 200]
    with open(output_path, 'a') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        for i, (index, row) in enumerate(tqdm(df_songs.iloc[1485811:].iterrows())):
            if (i % 136 == 0) & (i != 0):
                time.sleep(np.random.randint(30, high=60))
            if (i % 24134 == 0) & (i != 0):
                time.sleep(np.random.randint(24, high=65))
            if (i % 623432 == 0) & (i != 0):
                time.sleep(np.random.randint(64, high=183))
            spotify_uris = extract_spotify_uri(row['song'], row['artist'], sp)
            writer.writerow(spotify_uris)


def create_spotify_features(sp, input_path='../data/spotify_uris.csv', output_path='../data/spotify_features.csv'):
    def extract_audio_features(audio_features):
        danceability = audio_features['danceability']
        energy = audio_features['energy']
        key = audio_features['key']
        loudness = audio_features['loudness']
        mode = audio_features['mode']
        speechiness = audio_features['speechiness']
        acousticness = audio_features['acousticness']
        instrumentalness = audio_features['instrumentalness']
        liveness = audio_features['liveness']
        valence = audio_features['valence']
        tempo = audio_features['tempo']
        duration_ms = audio_features['duration_ms']
        return [danceability, energy, key, loudness, mode, speechiness, acousticness,
                instrumentalness, liveness, valence, tempo, duration_ms]

    df_uri = pd.read_csv(input_path, converters={'artist_id': lambda x: x.strip("[]").replace("'", "").split(', ')})
    with open(output_path, 'a') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        for index, row in tqdm(df_uri.iloc[198532:].iterrows()):
            track_uri = row['track_id']
            album_uri = row['album_id']
            artist_uris = row['artist_id']
            if len(artist_uris) > 5:
                print(artist_uris)
                artist_uris = artist_uris[:5]
            if track_uri == track_uri:
                audio_features = sp.audio_features(track_uri)
                if audio_features[0] is not None:
                    audio_features = extract_audio_features(audio_features[0])
                else:
                    audio_features = [None] * 12
                if artist_uris is not None:
                    artists = sp.artists(artist_uris)['artists']
                    artist_popularity = artists[0]['popularity']
                    genres = [artist['genres'] for artist in artists]
                    genres = [list(set(chain(*genres)))]

            else:
                audio_features = [None] * 12
                artist_popularity = None
                genres = [None]
            spotify_features = [row['artist'], row['track']] + audio_features + genres + [artist_popularity]
            writer.writerow(spotify_features)


if __name__ == '__main__':
    with open(r'../data/spotify_auth.yaml') as file:
        auth = yaml.full_load(file)
    client_id = auth['client_id']
    client_secret = auth['client_secret']
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                          client_secret=client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                requests_timeout=200, retries=10, backoff_factor=10)
    # create_songs_df(min_users=0)
    # create_spotify_uri_frame(spotify)
    create_spotify_features(spotify)
