# CS-410 Course Project
# Spotify Sentiment Analsys (Recommender and models comparison)

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


