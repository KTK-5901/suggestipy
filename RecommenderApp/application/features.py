import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

def extract(URL):

    with open(r"secret.txt") as f:
        client_id = f.readlines()[0][:-2]
        client_secret = f.readlines()[1]

    credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credentials_manager)

    checklist = URL.split("/");
    check_df = pd.DataFrame();
    if len(checklist)<5:
        return check_df

    playlist_id = URL.split("/")[4].split("?")[0]


    try:
        playlist_track_data = sp.playlist_tracks(playlist_id)

        tracks_id = []
        tracks_title = []
        tracks_artists = []
        tracks_first_artist = []

        for track in playlist_track_data['items']:
            tracks_id.append(track['track']['id'])
            tracks_title.append(track['track']['name'])
            artist_list = []
            for artist in track['track']['artists']:
                artist_list.append(artist['name'])
            tracks_artists.append(artist_list)
            tracks_first_artist.append(artist_list[0])

        features = sp.audio_features(tracks_id)
        features_df = pd.DataFrame(data=features, columns=features[0].keys())
        features_df['title'] = tracks_title
        features_df['first_artist'] = tracks_first_artist
        features_df['all_artists'] = tracks_artists
        features_df = features_df[['id', 'title', 'first_artist', 'all_artists',
                                    'danceability', 'energy', 'key', 'loudness',
                                    'mode', 'acousticness', 'instrumentalness',
                                    'liveness', 'valence', 'tempo',
                                    'duration_ms', 'time_signature']]
    except:
        return check_df

    return features_df
