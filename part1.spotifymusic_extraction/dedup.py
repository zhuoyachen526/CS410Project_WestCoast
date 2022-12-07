from more_itertools import unique_everseen
with open('my_playlist.csv', 'r') as f, open('my_playlist_clean.csv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))