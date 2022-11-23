import csv

filename = "main_playlist_sentiment.csv"

# Initializing row list
rows = []
# Initialzing field list
fields = []


# read csv file in current directory

with open(filename, 'w') as csvfile:

    # creating a csv reader object

    csvreader = csv.reader(csvfile)

    # remove columns "artist_id", "track_id", and "lyric". Then save it as "sentiment_library.csv"
    fields = next(csvreader)
    fields.remove("artist_id")
    fields.remove("track_id")
    fields.remove("lyric")

    # creating a csv writer object

    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    for row in csvreader:
        rows.append(row)

        # remove columns "artist_id", "track_id", and "lyric". Then save it as "sentiment_library.csv"
        
