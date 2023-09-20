import requests
from send_email import send_email

api_key = "fc5798e4cf6e468e9467e177c420c2c8"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-19" \
      "&sortBy=publishedAt&apiKey=fc5798e4cf6e468e9467e177c420c2c8"

# make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

# send the email
body = body.encode("utf-8")
send_email(body)