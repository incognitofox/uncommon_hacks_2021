import keys
import json
import requests
import sys
import os

def url_to_mp3 (url):
    os.system("youtube-dl --extract-audio --audio-format mp3 --output \"noise.mp3\" " + url + " -k")

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
    if (tmp["result"] == None):
        return (None, None)
#    print("title: " + str(tmp["result"]["title"]))
#    print("artist: " + str(tmp["result"]["artist"]))
    return (str(tmp["result"]["title"]), str(tmp["result"]["artist"]))
   
def url_to_audio (url):
    if "youtube" not in url:
        print ("This is not a youtube video")
        os.system ("rm -rf noise*")
        return False
    url_to_mp3(url)
    title, artist = get_audio_info ("noise.mp3.mp3", file = True)
    if (title == None and artist == None):
        print ("This is not a song")
        os.system ("rm -rf noise*")
        return False
    is_rick = (title == "Never Gonna Give You Up" and artist == "Rick Astley")
    if is_rick:
        print ("Ha! Get pranked! You've been Ricked Rolled")
        os.system ("rm -rf noise*")
        return True
    else:
        print ("This is actually " + title + " by " + artist)
        os.system ("rm -rf noise*")
        return False
    os.system ("rm -rf noise*")

url_to_audio(sys.argv[1])