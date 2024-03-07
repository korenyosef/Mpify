# Spotify Playlist to YouTube Downloader
This script allows you to download the audio of the first 20 songs from a public Spotify playlist and save them as MP3 files using YouTube. It uses the Spotify and YouTube APIs and intentionally includes delays to avoid spamming YouTube's API.

## Requirements
Before running the script, make sure to create a .env file in the same directory with the following information:

```txt
CLIENT_ID = "your spotify client id"
CLIENT_SECRET = "your spotify client secret"
YOUTUBE_API_KEY = "your youtube api key"
```

You can obtain your Spotify client ID and client secret by creating a Spotify application [here](https://developer.spotify.com/dashboard), and your YouTube API key by following the steps [here](https://developers.google.com/youtube/v3/getting-started).

## Usage
Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

Run the script and enter the public Spotify playlist URL or ID when prompted.
```bash
python main.py
```

The songs will be downloaded to the music folder.

## Important Notes
The script uses 15% of the YouTube quota and can be run 6 times a day.
The Spotify playlist must be public for the script to access it.
It downloads the first 20 songs from the playlist.
The intentional delays in the script are designed to prevent spamming YouTube's API.
Note: Ensure that the script is used responsibly and complies with the terms of service of Spotify and YouTube.

# Disclaimer
This script is provided as-is, and the developer is not responsible for any misuse or violations of terms of service by users. Use the script responsibly and adhere to the policies of Spotify and YouTube.