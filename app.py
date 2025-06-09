#necessary packages 
from flask import Flask, request, jsonify
from flask_cors import CORS
import text2emotion as te
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import nltk
nltk.download('punkt_tab')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:8000", "null"]}})        #define the app and enable CORS
#
# CORS(app)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="your client ID",
    client_secret="your client secret "
))

mood_map = {                 #map emotions to genres
    'Happy': 'pop',
    'Angry': 'rock',
    'Surprise': 'electronic',
    'Sad': 'acoustic',
    'Fear': 'lofi'
}
@app.route('/')    #define the home route
def home():
    return "Emotion-Based Song Recommender API is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    user_text = request.json.get('text', '')
    if not user_text:
        return jsonify({'error': 'No text provided'}), 400

    emotion_scores = te.get_emotion(user_text)
    if not emotion_scores or max(emotion_scores.values()) == 0:     #check if emotion scores are empty or all zero
        return jsonify({'emotion': 'Unknown', 'songs': []})

    emotion = max(emotion_scores, key=emotion_scores.get)
    genre = mood_map.get(emotion, 'pop')

    results = sp.search(q=f'genre:{genre}', type='track', limit=10)
    songs = [{
        'name': item['name'],
        'artist': item['artists'][0]['name'],
        'url': item['external_urls']['spotify'],
        'preview': item['preview_url']
    } for item in results['tracks']['items']]

    return jsonify({'emotion': emotion, 'songs': songs})

if __name__ == "__main__":   #this is the main function that runs the app
    #set the port to 5000
    app.run(debug=True)
