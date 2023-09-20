import requests

api_key = "fc5798e4cf6e468e9467e177c420c2c8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-19" \
      "&sortBy=publishedAt&apiKey=fc5798e4cf6e468e9467e177c420c2c8"

# make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions

for article in content["articles"]:
    print(article["title"])
    print(article["description"])