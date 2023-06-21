import spotipy
import re
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# Spotify Token Access

client_id = "YOUR CLIEND ID"
client_secret = "YOUR CLIENT SECRET"
redirect_uri = "http://localhost:8888/callback"  # This should match the redirect URI in your Spotify Developer Dashboard

# Add the URL of the playlist you want to duplicate and the name of the new playlist
public_playlist_url = "YOUR PLAYLIST LINK"
new_playlist_name = "My Duplicated Playlist"


# Create an instance of the Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-public"))

def extract_playlist_id(public_playlist_url):
    # Use regular expression to extract the playlist ID
    pattern = r"playlist/([a-zA-Z0-9]+)"
    match = re.search(pattern, public_playlist_url)
    if match:
        return match.group(1)
    else:
        return None

def duplicate_playlist(public_playlist_url, new_playlist_name):
    # Get the playlist ID from the public playlist URL
    playlist_id = extract_playlist_id(public_playlist_url)
    if not playlist_id:
        print("Invalid playlist URL")
        return

    # Get the tracks from the public playlist
    results = sp.playlist_tracks(playlist_id)

    # Create a new playlist
    user = sp.current_user()
    new_playlist = sp.user_playlist_create(user["id"], new_playlist_name)

    # Add the tracks to the new playlist
    tracks = [track["track"]["uri"] for track in results["items"]]
    sp.playlist_add_items(new_playlist["id"], tracks)

    print("Playlist duplicated successfully!")

# Run the script and duplicate those BANGERS!!!!
duplicate_playlist(public_playlist_url, new_playlist_name)
