#reading data from csv file
import pandas as pd
df = pd.read_csv("main_playlist_sentiment.csv")
df = df.drop_duplicates(subset = "track_name")
df = df.reset_index(drop = True)
df.head()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
def sentiment():
    sentiment_diff = []
    artist = input("Enter artist name: ")
    if artist in df["artist_name"].values:
        song = input("Enter song name: ")
        if song in df["track_name"].values:
            sentiment = df[df["track_name"] == song]["sentiment_score"].values[0]
            ind = df[df["track_name"] == song]["sentiment_score"].index.values[0]
            for val,ind2 in zip(df["sentiment_score"].values, df["sentiment_score"].index):
                if val != sentiment and ind2 != ind:
                    sentiment_diff.append(round(abs(sentiment - val),4))
            sentiment_diff_ord = sorted(sentiment_diff)
            sentiment_diff_ord = list(dict.fromkeys(sentiment_diff_ord))
            indexes = [sentiment_diff.index(i) +1  for i in sentiment_diff_ord]
            indexes2 = []
            for i in indexes:
                if i < ind:
                    indexes2.append(i - 1)
                else:
                    indexes2.append(i)
            indexes2 = [i + 1 if i == 792 else i for i in indexes2]
            most_similar = df.iloc[indexes2[:20]][["artist_name", "track_name", "sentiment", "sentiment_score"]]
            least_similar = df.iloc[indexes2[-20:]][["artist_name", "track_name", "sentiment", "sentiment_score"]]
            print("\nMost Similar 20 tracks:\n")
            display(most_similar.reset_index(drop = True))
            print("\nLeast Similar 20 tracks:\n")
            display(least_similar.reset_index(drop = True))
            plt.figure(figsize = (10, 6))
            sns.barplot(data = most_similar, x = "track_name", y ="sentiment_score")
            plt.title("Top 20 Most Similar Tracks", fontsize = 15)
            plt.xticks(rotation = 90)
            plt.show()
            plt.figure(figsize = (10, 6))
            sns.barplot(data = least_similar, x = "track_name", y ="sentiment_score")
            plt.title("Top 20 Least Similar Tracks", fontsize = 15)
            plt.xticks(rotation = 90)
            plt.show()
        else:
            print("Song not found")
    else:
        print("Artist Not Found")
sentiment()