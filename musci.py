import requests
import pygame
from io import BytesIO
from pydub import AudioSegment

def get_lastfm_track_info(api_key, artist, track_name):
    base_url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        'method': 'track.search',
        'api_key': api_key,
        'artist': artist,
        'track': track_name,
        'format': 'json'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Assuming the first track in the search results
        track = data['results']['trackmatches']['track'][0]
        track_url = track['url']

        return track_url
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def play_lastfm_track(api_key, artist, track_name):
    track_url = get_lastfm_track_info(api_key, artist, track_name)

    if track_url:
        # Download the audio file
        audio_response = requests.get(track_url.replace('/track/', '/music/') + '/+audio.mp3')
        audio_data = BytesIO(audio_response.content)

        # Convert the audio file to WAV format
        audio = AudioSegment.from_mp3(audio_data)
        wav_data = BytesIO()
        audio.export(wav_data, format="wav")

        # Initialize pygame
        pygame.init()

        # Load the WAV audio file
        pygame.mixer.init()
        pygame.mixer.music.load(wav_data)

        # Play the audio
        pygame.mixer.music.play()

        # Wait for the song to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Clean up
        pygame.mixer.quit()
        pygame.quit()

# Replace 'YOUR_API_KEY' with your Last.fm API key
api_key = '68d0a730031d29f6905e62e6d4d95353'
artist = 'sid sriram'
track_name = 'parayuvaan'

play_lastfm_track(api_key, artist, track_name)
