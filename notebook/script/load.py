from pprint import pprint
import json
import pandas as pd

path = "../data/First_1000.json"
raw_json = json.loads(open(path).read())

playlist = raw_json["playlists"]
df = pd.json_normalize(playlist, record_path='tracks', meta=['name'])

df.to_csv("../data/raw_data.csv")