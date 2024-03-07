import json
from dotenv import load_dotenv
import os
import base64
from requests import post,get
from googleapiclient.discovery import build
from pytube import YouTube
import time

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
youtube_api_key = os.getenv("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=youtube_api_key)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_results = json.loads(result.content)
    token = json_results["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

token = get_token()

def song_names(id):
    headers = get_auth_header(token)
    result = get(url=f"https://api.spotify.com/v1/playlists/{id}/tracks", headers=headers)
    json_result = json.loads(result.content)
    if "error" in json_result and json_result["error"]["status"] == 404:
        print("Error: Invalid playlist ID. Please enter a valid ID or URL.")
        return None
    songs = []
    for x in range(20):
        print(json_result)
        jsonX = json_result["items"][x]["track"]["name"]
        x =+ x
        songs.append(jsonX)
    return songs

def extract_playlist_id(url_or_id):
    
    if("open.spotify.com/playlist/" in url_or_id):
        url_parts = url_or_id.split("/")
        id = url_parts[-1]
        
        id = id.split("?")[0]
    else:
        id = url_or_id
    
    return id

if __name__ == "__main__":
    try:
        while True:
            url_or_id = str(input("Enter public Spotify ID/URL: "))
            id = extract_playlist_id(url_or_id)
            
            songs = song_names(id)
            
            if songs is not None:
                break
            
        for song in songs:
            request = youtube.search().list(
                part="snippet",
                maxResults=1,
                q=song
            )
            time.sleep(1)
            response = request.execute()
            time.sleep(3)
            
            if "error" in response:
                print(f"Error searching for '{song}': {response['error']['message']}")
                continue
            
            res = response["items"][0]["id"]["videoId"]
            yt = YouTube(f"https://www.youtube.com/watch?v={res}")
            audio = yt.streams.filter(only_audio = True).first()
            destination = './music'
            out_file = audio.download(output_path=destination) 
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " has been successfully downloaded.")

        print("Finished downloading your music, thanks for using Mpify.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")