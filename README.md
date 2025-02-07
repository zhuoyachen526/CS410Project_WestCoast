# CS-410 Course Project
# Spotify Sentiment Analysis (Recommender and models comparison)

## Presentation Video
**Link to presentation (Access with school email):**
https://mediaspace.illinois.edu/media/t/1_wrzhzr7b

## Presentation Slides
please check the file "Presentation_West_Coast_Final.pptx".

## Codes

  Check the subfolders (Part 1 / 2 / 3):
  - part1.spotifymusic_extraction
  - part2.song_recommender
  - part3.multi_models
  
  Software Requirement:
  - VSCode or JetBrains (We highly recommend VSCode since it can execute ipynb like as you run it via jupyter notebook command)
  - jupyter notebook 

  **User guide**
  - please check the Code Documentation Below.

## Code Documentation

**Part 1: Spotify Music Extraction**

*Code 1: spotify_api.py*

Function: This code is to 1) extract list of songs and artists' names into a csv file by using Spotify account token to call the Spotify develper tool API, 2) to call MusicMatch api to pull lyrics of each song and add them to the list. The logic is as follows:

1. find your user id
go to the spotify profile webpage and check the webpage address. https://open.spotify.com/user/****

**** is your spotify user id 

2. get a fresh OAuth Token
from an spotify console. e.g. https://developer.spotify.com/console/get-playlists/

3. edit the personal info in the "spotify_api.py" and export a playlist as "my_playlist.csv". 

*Code 2: sentiment_analysis.py*

Function: This code is to use the VADER (Valence Aware Dictionary and sEntiment Reasoner) library to conduct sentiment analysis and then add them to the list of songs info which we created from Code 1.

4. sentiment analysis
try "sentiment_analysis.py" and export a table as "my_playlist_sentiment.csv"


**Part 2: Song Recommender**

*Code 1: Sentiments_app.ipynb*

Function: This code is for users to utilize the song recommendation function based on the sentiment analysis result from the user’s playlist(s). The data source is from the extraction of songs and lyrics, and the sentiment analysis result from Part 1. The first cell of the program is to read the csv file and to drop songs with duplicated name. The second cell is the core logic of the program. When the user execute the third cell to call the sentiment function, the program will ask the user to enter the name of the artist. If found, it will ask the user to enter the song name. If not found, the program will stop executing and the user can simple work re-run the cell. When the user enters the song name and it is found, it would generate two lists: top 20 most similar songs based on the sentiment scores and top 20 least similar songs based on the sentiment scores as well. To help the user to better visualize the score different in similarity and dissimilarity, the program also use matplotlibrary to display the charts. 

**Part 3. Compare different pre-trained sentiment analysis models**

*Code 1: HaggingFace_Models.ipynb*

Function: This code is to choose a proper pre-trained sentiment analysis model from the top-listed models in the Hugging Face, an AI community. An easy test set is used and expected to generate a sentiment label “positive”, “neutral” or “negative’. Only the model that make the full accurate prediction will be selected to predict our playlist with over 400 songs. 
Implementation: The code doesn’t require input file. It can be practiced in Jupyter Notebook. 

*Code 2: sentiment_analysis_eval_multi_models_comparison_final.py*

Function: This code will predict the sentiment labels of lyrics from a playlist with over 400 songs using three pre-trained sentiment analysis models. They are “Vader”, “TextBlob”, and “Hugging Face: Bertweet”. Prediction inconsistency among the three models will be tabulated and visualized in plots. The lyrics are also manually evaluated. Model prediction will be compared with the manual evaluations to calculate the model accuracy. 
Implementation: The code can be run on any python IDE. Prerequisite python libraries include ”VaderSentiment", "textblob", "happytransformer", "emoji", and other necessary libraries. The code will take “my_playlist_4_multi_model.csv” as an input for the 1st part (sentiment prediction) and take “playlist_sentiment_eval.xlsx” as an input for the 2nd part (model accuracy).


