import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

def uri_to_feature(uri):

    cid = "2481a07aec484e1dabcc4b9926c3ac4f"
    secret = "99803b830a0f4ec0a8acf3cde3d1e5eb"

    client_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_manager)

    feature = sp.audio_features(uri)[0]

    artist = sp.track(uri)["artists"][0]["id"]
    artist_pop = sp.artist(artist)["popularity"]
    artist_genres = sp.artist(artist)["genres"]

    track_pop = sp.track(uri)["popularity"]

    feature["artist_pop"] = artist_pop

    if artist_genres:
        feature["genres"] = " ".join([re.sub(' ','_',i) for i in artist_genres])
    else:
        feature["genres"] = "unknown"

    feature["track_pop"] = track_pop

    return feature


if __name__ == '__main__':
    result  = uri_to_feature("7H6ev70Weq6DdpZyyTmUXk")
    print(result)