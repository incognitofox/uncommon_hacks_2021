import keys
import json
import requests
import sys

def get_audio_info(directory, file = False, url = False):
    result = None
    if file:
        files = {
            'file' : open(directory, "rb"),
        }
        data = {
            'api_token': keys.audd_key,
            'return': 'apple_music,spotify',
        }
        result = requests.post('https://api.audd.io/', data=data, files = files)
    if url:
        data = {
            'api_token': keys.audd_key,
            'url': "https://audd.tech/example1.mp3", 
            'return': 'apple_music,spotify',
        }
        result = requests.post('https://api.audd.io/', data=data)
         
    tmp = result.json()
    print("title: " + str(tmp["result"]["title"]))
    print("artist: " + str(tmp["result"]["artist"]))
   
args = sys.argv
get_audio_info(args[1], file = args[2], url = not args[2])

