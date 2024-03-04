import os

from dotenv import load_dotenv

from spotify_auth import add_songs_to_spotify_playlist
from top_100_billboard_scraper import get_top_100_by_date

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME')

spotify_user_creds = {
    'spotify_client_id': os.getenv('SPOTIFY_CLIENT_ID'),
    'spotify_client_secret': os.getenv('SPOTIFY_CLIENT_SECRET'),
    'spotify_username': os.getenv('SPOTIFY_USERNAME'),
}


def main():
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

    songs_list = get_top_100_by_date(date)
    add_songs_to_spotify_playlist(
        spotify_user_creds=spotify_user_creds,
        songs_list=songs_list,
        date=date
    )

main()
