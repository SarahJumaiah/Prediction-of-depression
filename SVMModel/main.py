from flask import Flask, request, jsonify
from flask_cors import CORS
from auth import authenticate
from get_tweets import get_user_tweets
from get_user_id import get_user_id
from preprocessing import preprocess_text
import pickle
import joblib

app = Flask(__name__)
CORS(app)
model = joblib.load('SVM.pkl')
def predict_depression(sentence):
    # Make prediction
    prediction = model.predict([sentence])
    # Map prediction to "depression" or "not depression"
    if prediction[0] == 1:
        return "Depressed"
    else:
        return "Not Depressed"

consumer_key = "4LvzlC0kIvEBOwUFKgDF8gGRq"
consumer_secret = "f2mXLQsNNW0JTEvDp43ERMsBCN1wu0FEH3R38cquIzdDI7x14I"
access_token = "1788651821243756545-XhSPoMCOTmCjysW8SxaGhKQBu9Zmue"
access_token_secret = "HBIvDnbAR6FYZXT3p2BTsQ0fpJL0Aw9vVAIsOzfb90icq"

@app.route('/api/get_posts', methods=['POST'])
def get_posts():
    username = request.json.get('username')
    params = {"usernames": username, "user.fields": "created_at,description"}

    # Authenticate and get user ID
    user_ids = get_user_id(consumer_key, consumer_secret, access_token, access_token_secret, params)
    tweets = []
    for user_id in user_ids:
        tweets += get_user_tweets(user_id)
    tweets = list(map(lambda sentence: preprocess_text(sentence), tweets))

    # Predict depression for each tweet
    depression_predictions = [predict_depression(tweet) for tweet in tweets]

    # Count the number of depressed tweets
    num_depressed_tweets = sum(prediction == "Depressed" for prediction in depression_predictions)
    num_non_depressed_tweets = len(tweets) - num_depressed_tweets

    # Calculate percentage of depressed posts
    total_tweets = len(tweets)
    if total_tweets == 0:
        percentage_depressed = 0
    else:
        percentage_depressed = (num_depressed_tweets / total_tweets) * 100

    # Determine overall depression status
    status = f"Depression percentage is  {percentage_depressed:.2f}%"

    return jsonify({
        'overall_status': status,
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
