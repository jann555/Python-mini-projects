from bs4 import BeautifulSoup
import requests
from spotify_auth import add_songs_to_spotify_playlist


def get_top_100_by_date(date):
    # Scraping Billboard 100
    billboard_url = 'https://www.billboard.com/charts/hot-100/' + date
    response = requests.get(billboard_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]
    return song_names
