username = ''
playlist_link1 = "https://open.spotify.com/playlist/15MOYCcWvI5LHf1ZJZwcuk"
playlist_link2 = "https://open.spotify.com/playlist/6hUt1RWqPlF8oJFqZkqkmq"
def main(username,playlist_link1,playlist_link2):
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import random

    scope = "playlist-modify-public"
    client_id = ""
    client_secret=""
    redirect_uri="http://localhost:8888/callback"

    token = SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,username=username,scope=scope)
    spotifyObject = spotipy.Spotify(auth_manager=token)

    playlist_name = "Spotify App Playlist"
    playlist_description = "Spotify App Playlist"
    spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)

    names1 = []
    names2 = []
    final = []

    playlist_uri1 = playlist_link1.split("/")[-1].split("?")[0]
    playlist_uri2 = playlist_link2.split("/")[-1].split("?")[0]

    for track1 in spotifyObject.playlist_tracks(playlist_uri1)["items"]:
        track_name1 = track1["track"]["name"]
        names1.append(track_name1)
    for track2 in spotifyObject.playlist_tracks(playlist_uri2)["items"]:
        track_name2 = track2["track"]["name"]
        names2.append(track_name2)


    final_names1 = random.sample(names1,50)
    final_names2 = random.sample(names2,50)
    final.append(final_names1)
    final.append(final_names2)

    list_of_song_names = []
    list_of_songs = []


    list_of_song_names.append(final)
    for i in list_of_song_names:
        for z in i:
            for y in z:
                result = spotifyObject.search(q=y)
                list_of_songs.append(result['tracks']['items'][0]['uri'])

    prePlaylist = spotifyObject.user_playlists(user=username)
    playlist = prePlaylist['items'][0]['id']

    spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)

if __name__ == "__main__":
    main(username,playlist_link1,playlist_link2)

