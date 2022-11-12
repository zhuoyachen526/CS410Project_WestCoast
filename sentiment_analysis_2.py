#pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import requests
import time

analyser = SentimentIntensityAnalyzer()

playlist_df= pd.read_csv("my_playlist.csv")
def get_lyric(artist_name,track_name):
    # musixmatch api base url
    base_url = "https://api.musixmatch.com/ws/1.1/"
    # your api key
    api_key = "&apikey=95f7e1aa1421c9807a18a2abdef5ce6e"
    #api method
    lyrics_matcher = "matcher.lyrics.get"
    "&q_artist="
    "&q_track="
    api_call = base_url + lyrics_matcher + "?format=json&callback=callback" + "&q_artist=" + artist_name + "&q_track=" + track_name + api_key
    request = requests.get(api_call)
    data = request.json()
    lyric = data['message']['body']['lyrics']['lyrics_body']
    return lyric




lyric_list = []
sentiment_list = []
sentiment_score_list = []

for track0 in playlist_df[['artist_name','track_name']].values:


    try:
        song = get_lyric(track0[0], track0[1])
        sentiment_score = analyser.polarity_scores(song)

        if sentiment_score['compound'] >= 0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Positive'
        elif sentiment_score['compound'] > -0.05 and sentiment_score['compound'] < 0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Neutral'
        elif sentiment_score['compound'] <= -0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Negative'

        sentiment_list.append(sentiment)
        sentiment_score_list.append((abs(sentiment_percentage) * 100))

    except:
        sentiment_list.append('None')
        sentiment_score_list.append(0)
    lyric_list.append(song)
    time.sleep(0.2)
    #the end of the for loop
playlist_df['lyric'] = lyric_list
playlist_df['sentiment'] = sentiment_list
playlist_df['sentiment_score'] = sentiment_score_list
playlist_df.to_csv('my_playlist_sentiment2.csv',header=True, index=False)
#print lyric of an song
song_index = 3
print("the "+str(song_index+1)+"th song in my list",playlist_df['lyric'][song_index])