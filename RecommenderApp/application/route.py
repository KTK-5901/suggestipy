import os
from flask import Flask, render_template, request, flash
from application.features import *
from application.model import *

songdf = pd.read_csv("./data/songs.csv")
feature_set = pd.read_csv("./data/allfeatures.csv")

app_path = os.path.dirname(__file__)
app = Flask(__name__, static_folder=app_path+'/static', template_folder=app_path+'/template')

app.config['SECRET_KEY'] = '47736628929377ndhnjejjdnnssaa'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/instruction")
def instruction():
    return render_template('instruction.html')

@app.route('/recommend', methods = ['POST'])
def recommend():
    URL = request.form['URL']
    df = extract(URL);
    my_songs = []
    if len(URL)<56 or df.empty:
        flash('Invalid URL','error')

    else:
        edm_top40 = recommend_from_playlist(songdf, feature_set,df)
        number_of_recs = int(request.form['number-of-recs'])

        for i in range(number_of_recs):
            my_songs.append([str(edm_top40.iloc[i,0]) + ' - '+ '"'+str(edm_top40.iloc[i,2])+'"', "https://open.spotify.com/track/"+ str(edm_top40.iloc[i,1])])
    return render_template('result.html', songs = my_songs)
