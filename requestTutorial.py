import requests
response = requests.get("https://wttr.in/Vancouver?format=3")
print(response.text)