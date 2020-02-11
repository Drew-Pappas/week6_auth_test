import requests
import secrets
 


base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "country" : "us",
    "q":"new hampshire",
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()

for item in result["articles"]:
    print(f"{item['title']}")
