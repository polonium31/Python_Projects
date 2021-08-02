import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
date = input("what year you would like to travel to in (YYYY-MM-DD) format:\t")
response = requests.get("https://bestoftheyear.in/music/hindi/")
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("h4", class_="entry-title title-font")
song_names = [song.getText() for song in song_names_spans]
print(song_names)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="d25228dfb0aa4c328a6e9decbcd47b01",
        client_secret="fde2541081a3454b8facaa8cd88522f6",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
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

playlist = sp.user_playlist_create(user=user_id, name=f"bollywood 100 top songs", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)