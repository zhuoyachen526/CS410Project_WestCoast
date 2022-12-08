# CS-410 Course Project
# Spotify Sentiment Analysis (Recommender and models comparison)

**Link to presentation (Access with school email):**
https://mediaspace.illinois.edu/media/t/1_wrzhzr7b

Software Requirement:
- VSCode or JetBrains (We highly recommend VSCode since it can execute ipynb like as you run it via jupyter notebook command)
- jupyter notebook 

Application components (Part 1 / 2 / 3):
- Songs and lyrics extraction
- Song recommender
- Sentiment analysis models

**User guide**
1. Open the ipynb file with VSCode or run "jupyter notebook" at the project folder (part 1 / 2 / 3)
2. Install the required libraries and run the cells
3. If you would like to test with your own playlist, please follow the *Use Your Own Playlist* instruction


**Use Your Own Playlist**
1. find your user id
go to the spotify profile webpage and check the webpage address. https://open.spotify.com/user/****

**** is your spotify user id 

2. get a fresh OAuth Token
from an spotify console. e.g. https://developer.spotify.com/console/get-playlists/

3. edit the personal info in the "spotify_api.py" and export a playlist as "my_playlist.csv". 

4. sentiment analysis
try "sentiment_analysis_2.py" and export a table as "my_playlist_sentiment.csv"

5. song recommender
import the "my_playlist_sentiment.csv" into the same folder of Sentiments_app.ipynb and run the cell

#Code Documentation#

###Part 1: Spotify Music Extraction###


###Part 2: Song Recommender###

*Code 1: Sentiments_app.ipynb*

Function: This code is for users to utilize the song recommendation function based on the sentiment analysis result from the user’s playlist(s). The data source is from the extraction of songs and lyrics, and the sentiment analysis result from Part 1. The first cell of the program is to read the csv file and to drop songs with duplicated name. The second cell is the core logic of the program. When the user execute the third cell to call the sentiment function, the program will ask the user to enter the name of the artist. If found, it will ask the user to enter the song name. If not found, the program will stop executing and the user can simple work re-run the cell. When the user enters the song name and it is found, it would generate two lists: top 20 most similar songs based on the sentiment scores and top 20 least similar songs based on the sentiment scores as well. To help the user to better visualize the score different in similarity and dissimilarity, the program also use matplotlibrary to display the charts. 

###Part 3. Compare different pre-trained sentiment analysis models###

*Code 1: HaggingFace_Models.ipynb*

Function: This code is to choose a proper pre-trained sentiment analysis model from the top-listed models in the Hugging Face, an AI community. An easy test set is used and expected to generate a sentiment label “positive”, “neutral” or “negative’. Only the model that make the full accurate prediction will be selected to predict our playlist with over 400 songs. 
Implementation: The code doesn’t require input file. It can be practiced in Jupyter Notebook. 

*Code 2: sentiment_analysis_eval_multi_models_comparison_final.py*

Function: This code will predict the sentiment labels of lyrics from a playlist with over 400 songs using three pre-trained sentiment analysis models. They are “Vader”, “TextBlob”, and “Hugging Face: Bertweet”. Prediction inconsistency among the three models will be tabulated and visualized in plots. The lyrics are also manually evaluated. Model prediction will be compared with the manual evaluations to calculate the model accuracy. 
Implementation: The code can be run on any python IDE. Prerequisite python libraries include ”VaderSentiment", "textblob", "happytransformer", "emoji", and other necessary libraries. The code will take “my_playlist_4_multi_model.csv” as an input for the 1st part (sentiment prediction) and take “playlist_sentiment_eval.xlsx” as an input for the 2nd part (model accuracy).


