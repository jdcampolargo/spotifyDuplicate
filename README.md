# Spotify Playlist Duplicator

This Python script allows you to duplicate a public Spotify playlist to your own Spotify account. It utilizes the Spotify Web API and the Spotipy library.

## Setup

1. Ensure you have Python 3.x installed on your machine.

2. Install the required dependencies by running the following command:

`pip install spotipy`

3. Obtain Spotify API credentials:

- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in (or create an account if you don't have one).
- Create a new app and note down the `Client ID` and `Client Secret`.
- In the app settings, add a redirect URI. This can be any valid URL, such as `http://localhost:8000/callback`.

4. Replace the placeholder values in the `duplicator.py` script:

- Set the `client_id` variable to your Spotify `Client ID`.
- Set the `client_secret` variable to your Spotify `Client Secret`.
- Set the `redirect_uri` variable to the redirect URI you provided in the Spotify Developer Dashboard.

## Usage

1. Get the public playlist URL that you want to duplicate. It should be in the format `https://open.spotify.com/playlist/PLAYLIST_ID`.

2. Open the `duplicator.py` script and update the following variables:

- Set the `public_playlist_url` variable to the public playlist URL you obtained.
- Set the `new_playlist_name` variable to the desired name for your new playlist.

3. Run the script by executing the following command:

`python duplicator.py`


The script will authenticate with Spotify, create a new playlist in your account, and duplicate the songs from the public playlist.

4. Once the script finishes, you can check your Spotify account to find the newly duplicated playlist.

Note: During the first run, you may be prompted to authorize the script to access your Spotify account. Follow the instructions provided in the terminal to complete the authorization process.

## Contact

Juan David Campolargo
[![Twitter Follow](https://img.shields.io/twitter/follow/jdcampolargo?style=social)](https://twitter.com/jdcampolargo)

* [Website](https://juandavidcampolargo.com/)
* [Twitter](https://twitter.com/jdcampolargo)
* [LinkedIn](https://linkedin.com/in/jdcampolargo)


## License
[MIT](https://choosealicense.com/licenses/mit/)
# spotifyDuplicateWebsite
