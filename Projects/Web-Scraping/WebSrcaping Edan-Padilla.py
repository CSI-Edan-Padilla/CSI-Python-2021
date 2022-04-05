#import webbrowser
#webbrowser.open("https://espndeportes.espn.com/")
import requests 
res = requests.get("https://gutenberg.org/cache/epub/67772/pg67772.txt")
print(len(res.text))
print(res.text[:300])