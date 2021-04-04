# uncommon_hacks_2021

## Installation
### Dependencies
This project uses the python `requests` library, which can be installed with:
```
pip install requests
```

This project also uses ```youtube-dl```, which can be installed using:
```
brew install youtube-dl
```

## Usage
Store audd API key in a file called `keys.py` as a variable named  `audd_key`.

To run the audio identification from a YouTube link:
```python audd_test.py <link>```

## Roadmap
1. Identify and correctly handle links that redirect (eg bit.ly, tinyurl, etc)
2. Create web front-end
3. Implement web scraper to classify all links in a webpage

## Authors
Zachary Rothwell, Bhakti Shah, William Wang
