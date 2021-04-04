import keys
import json
import requests

print(keys.audd_key)
files = {
    'file' : open("hidden_test.mp3", "rb")
}
data = {
    'api_token': keys.audd_key,
    'url': "https://audd.tech/example1.mp3", 
    'return': 'apple_music,spotify',
}
result = requests.post('https://api.audd.io/', data=data)
tmp = result.json()
print("title: " + str(tmp["result"]["title"]))
print("artist: " + str(tmp["result"]["artist"]))
