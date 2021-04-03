import keys
import requests

print(keys.audd_key)
files = {
    'file' : open("test.mp3", "rb")
}
data = {
    'api_token': keys.audd_key,
    'return': 'apple_music,spotify',
}
result = requests.post('https://api.audd.io/', data=data, files=files)
print(result.text)
