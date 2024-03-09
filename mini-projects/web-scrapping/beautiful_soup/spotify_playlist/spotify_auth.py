import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Spotify Authentication
def __authenticate_spotify_user(spotify_user_creds):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=spotify_user_creds['spotify_client_id'],
            client_secret=spotify_user_creds['spotify_client_secret'],
            show_dialog=True,
            cache_path="token.txt",
            username=spotify_user_creds['spotify_username'],
        )
    )
    user_id = sp.current_user()["id"]
    print(user_id)
    return sp


def __get_song_list_uri(sp, song_names, date):
    song_uris = []
    year = date.split("-")[0]

    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    return song_uris


def add_songs_to_spotify_playlist(spotify_user_creds, songs_list, date):
    sp = __authenticate_spotify_user(spotify_user_creds)
    user_id = sp.current_user()["id"]
    song_uris = __get_song_list_uri(sp=sp, song_names=songs_list, date=date)
    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
