import time
import numpy as np
import pandas as pd
import json
import requests
country_code = "US"

# get a fresh token, it expires in a short time.
# https://developer.spotify.com/console/post-playlists/
# get token
authorization = "BQBS0uKPMmomURxIWjlp59wnsGLdZ7AE6H-TjihnW1FtRvRLfm548fQihbmYWD_BixhfuVAm8g1XLkt8qEX9uOaE2jcnoJpjx1cKVEmm7GjjcarIoXtYOawl0UfaHxnGG_eF05ilNELE8US9_T-mXMKZHGrcoan4YoeFUAl0k9m8eGct2EXS7iAJGJH2UDs87Hf3dJ7oUA5h1wK2PB8"
user_id = "22ku6efy73kw6pajgbuynw6xy"
# this playlist id is for
playlist_id0 = '1CKQrgQXIM53Qvw5TaOQmt'


# track0_id = "2ooIqOf4X2uz4mMptXCtie"
# artist0_id = "1jeYbk5eqo6wgsQPjLeU5w"


def get_artist_from_artistid(artist_id):
    url = ''.join(["https://api.spotify.com/v1/artists/", artist_id])

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])}

    response = requests.request("GET", url, headers=headers, data=payload)
    data_temp = json.loads(response.text)
    return data_temp['name']


def get_artist_from_trackid(trackid):
    url = ''.join(["https://api.spotify.com/v1/artists/", trackid])

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])}

    response = requests.request("GET", url, headers=headers, data=payload)
    data_temp = json.loads(response.text)
    return data_temp['name']


def get_track_from_trackid(trackid):
    url = ''.join(["https://api.spotify.com/v1/tracks/", trackid])

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])}

    response = requests.request("GET", url, headers=headers, data=payload)
    data_temp = json.loads(response.text)
    return data_temp['name']


def get_related_artists_from_trackid(trackid):
    url = ''.join(["https://api.spotify.com/v1/artists/",
                  trackid, "/related-artists"])

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data_temp = json.loads(response.text)
    dic0 = data_temp['artists']
    artist_list = []
    artist_id_list = []
    for value in dic0:
        artist_list.append(value['name'])
        artist_id_list.append(value['id'])
    return artist_list, artist_id_list


def create_a_playlist(new_playlist_name):
    url = ''.join(["https://api.spotify.com/v1/users/", user_id, "/playlists"])

    payload = json.dumps({
        "name": new_playlist_name,
        "description": "bocheng's playlist for the group project of CS410",
        "public": False
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data_temp = json.loads(response.text)
    new_playlist_id = data_temp['id']
    return new_playlist_id


def get_artist_top_tracks_from_artist_id(artist_id):
    url = ''.join(["https://api.spotify.com/v1/artists/",
                  artist_id, "/top-tracks?market=US"])

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data_temp = json.loads(response.text)
    dic0 = data_temp['tracks']
    track_list = []
    track_id_list = []
    for value in dic0:
        track_list.append(value['name'])
        track_id_list.append(value['id'])
    return track_list, track_id_list


def add_tracks_to_playlist(track_id_list, playlist_id):
    url = ''.join(["https://api.spotify.com/v1/users/",
                   user_id,
                  "/playlists/",
                   playlist_id,
                   "/tracks?uris="])
    for track_id in track_id_list:
        url += ''.join(["spotify:track:",
                        track_id,
                       ","])
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# pass json to lists
def json_read_to_list(info_temp):
    playlist_tracks_info_list = []
    print("length:", len(info_temp))
    for i in np.arange(len(info_temp)):
        temp0 = [info_temp[i]['track']['artists'][0]['name'],
                 info_temp[i]['track']['artists'][0]['id'],
                 info_temp[i]['track']['name'],
                 info_temp[i]['track']['id']]
        playlist_tracks_info_list.append(temp0)
    return playlist_tracks_info_list

# get playlist tracks from platlist id
def get_playlist_tracks(playlist_id):
    url = ''.join(["https://api.spotify.com/v1/playlists/",
                   playlist_id,
                   "/tracks"])

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': ''.join(['Bearer ', authorization])
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data_temp = json.loads(response.text)
    info_temp = data_temp['items']
    playlist_tracks_info_list0 = json_read_to_list(info_temp)

    next_temp = data_temp['next']
    count_next = 0
    while (next_temp):
        count_next += 1
        time.sleep(0.2)
        response = requests.request(
            "GET", next_temp, headers=headers, data=payload)
        data_next_temp = json.loads(response.text)
        info_next_temp = data_next_temp['items']
        next_temp = data_next_temp['next']
        playlist_tracks_info_list0 += json_read_to_list(info_next_temp)
        print("WHAT IS the ", str(count_next), " next: ", next_temp)
    print("the total number of item captured: ",
          len(playlist_tracks_info_list0))

    playlist_df = pd.DataFrame(playlist_tracks_info_list0,
                               columns=['artist_name', 'artist_id', 'track_name', 'track_id'])

    playlist_df.to_csv('my_playlist_clean.csv', header=True, index=False)

    return playlist_df

playlist_tracks1 = get_playlist_tracks(playlist_id0)

