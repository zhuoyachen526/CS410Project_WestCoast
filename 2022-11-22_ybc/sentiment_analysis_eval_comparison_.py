#####################################################################
# 1. code is adapted from the code below.                           #
#   https://github.com/PetrKorab/The-Most-Favorable-Pre-trained     #
#   -Sentiment-Classifiers-in-Python/blob/main/analysis.ipynb       #
#   the purpose of the code:                                        #
#   is to compare various pretrained analyzer                       #
# 2. please make sure the libraries "vaderSentiment",               #
#    "textblob","happytransformer" and "emoji" are installed        #
#####################################################################
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
import requests
import time
from textblob import TextBlob
from happytransformer import HappyTextClassification
import matplotlib.pyplot as plt

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



###########
# 1.VADER #
###########
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
playlist_df['VADER_sentiment'] = sentiment_list
playlist_df['VADER_sentiment_score'] = sentiment_score_list

playlist_df.loc[playlist_df['VADER_sentiment']=="None",'VADER_sentiment'] = "Neutral"
#########################
# 2.textblob            #
# pip install textblob  #
#########################
#The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity).
#The polarity score is a float within the range [-1.0, 1.0]. 
#The subjectivity is a float within the range [0.0, 1.0] 
#where 0.0 is very objective and 1.0 is very subjective.
sentiment_list = []
sentiment_score_list = []
for lyric in lyric_list:
    classifier = TextBlob(lyric)
    polarity = classifier.sentiment.polarity
    #subjectivity = classifier.sentiment.subjectivity
    sentiment_score_list.append(polarity)
    
playlist_df['textblob_sentiment_score'] = sentiment_score_list


playlist_df.loc[playlist_df['textblob_sentiment_score']>0,'textblob_sentiment'] = "Positive"
playlist_df.loc[playlist_df['textblob_sentiment_score']==0,'textblob_sentiment'] = "Neutral"
playlist_df.loc[playlist_df['textblob_sentiment_score']<0,'textblob_sentiment'] = "Negative"
################################
# 3.Happy Transformer          #
# pip install happytransformer #
# pip3 install emoji==0.6.0    #
################################
#https://www.youtube.com/watch?v=Ew72EAgM7FM
#models are found from the website https://huggingface.co/
sentiment_list = []
sentiment_score_list = []
for lyric in lyric_list:
    classifier = HappyTextClassification(model_type="RoBERTa", model_name="finiteautomata/bertweet-base-sentiment-analysis", num_labels=3)
    try:
        if len(lyric)>128:
            lyric= lyric[:128]
        polarity = classifier.classify_text(lyric)
        sentiment_list.append(polarity.label)
        sentiment_score_list.append(polarity.score)
    except:
        sentiment_list.append("NA")
        sentiment_score_list.append(404)

playlist_df['HF_sentiment'] = sentiment_list
playlist_df['HF_sentiment_score'] = sentiment_score_list
playlist_df.loc[playlist_df['HF_sentiment']=='POS','HF_sentiment'] = "Positive"
playlist_df.loc[playlist_df['HF_sentiment']=='NEU','HF_sentiment'] = "Neutral"
playlist_df.loc[playlist_df['HF_sentiment']=='NEG','HF_sentiment'] = "Negative"

################################
# 4. sentiment_consistency     #
################################
x =np.array(playlist_df['VADER_sentiment']==playlist_df['HF_sentiment'])*1
y =np.array(playlist_df['VADER_sentiment']==playlist_df['textblob_sentiment'])*1
z =np.array(playlist_df['HF_sentiment']==playlist_df['textblob_sentiment'])*1
playlist_df['sentiment_consistency']=x+y+z
# 3 means all the sentiments agrees
# 1 means two sentiments agrees
# 0 means no sentiments agrees
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'All agree', 'Two agrees', 'no agrees'
x0=playlist_df.loc[playlist_df['sentiment_consistency']==3].shape[0]/playlist_df.shape[0]
y0=playlist_df.loc[playlist_df['sentiment_consistency']==1].shape[0]/playlist_df.shape[0]
z0=playlist_df.loc[playlist_df['sentiment_consistency']==0].shape[0]/playlist_df.shape[0]
sizes = [x0, y0, z0]
explode = (0, 0, 0.1)  # only "explode" the 3nd slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title(f"total songs #: {playlist_df.shape[0]}")
plt.savefig("sentiment_consistency.png", dpi =300,
            transparent = True,
            bbox_inches = 'tight')
plt.show()


#####################
# 4.Export the data #
#####################
playlist_df=playlist_df.loc[:,['artist_name', 'artist_id', 'track_name', 'track_id', 'lyric',
       'VADER_sentiment', 'VADER_sentiment_score', 
       'textblob_sentiment', 'textblob_sentiment_score',
       'HF_sentiment','HF_sentiment_score','sentiment_consistency']]
playlist_df.to_csv('playlist_sentiment_comparison.csv',header=True, index=False)
