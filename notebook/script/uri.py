import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

def uri_to_feature(uri):

    with open("secret.txt") as f:
        cid = f.readlines()[0][:-2]
        secret = f.readlines()[1]
        
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
