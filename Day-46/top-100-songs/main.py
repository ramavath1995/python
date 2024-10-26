import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("what year you would like to travel to in YYY-MM-DD format.")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")
songs = [song.getText().strip() for song in soup.select(".a-no-trucate")][::2]

s_client_id = "d84a967d10cb42ee8b2be35202999d3f"
s_secret_id = "793d58346e7d47d59a613765e8c351a5"
app_name = "bill-board to spotify"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://billboard.com",
        client_id=s_client_id,
        client_secret=s_secret_id,
        show_dialog=True,
        cache_path="token.txt",
        username=app_name,
    )
)
user_id = sp.current_user()["id"]
user_name = "31w3sctpsq6aleonaq7a5wbrn6wy"

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
