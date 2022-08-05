import requests
import urllib.parse
import time

token = {"authorization":"token"}



choices = input("Single/Multiple reaction(1 for single, 2 for multiple, E to exit): ")

if choices == "1":
    channel_id = input("Channel ID: ")
    message_id = input("Message ID: ")
    emoji = input("Emoji: ")
    req = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me?location=Message", headers = token)


elif choices == "2":
    req = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50", headers = token)
    penis = req.json()
    def slanje(message_id):
        req = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me?location=Message", headers = token)

    for id in penis:
        slanje(id["id"])
        time.sleep(1)

elif choices == "E":
    exit
