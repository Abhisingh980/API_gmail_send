import requests
import gmail

api_key = "86a80f8923b5436d836ba3ae2cf87825"

query = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={query}&"
       "from=2023-12-21&sortBy=publishedAt&"
       "apiKey=86a80f8923b5436d836ba3ae2cf87825&"
       "language=en")

requests = requests.get(url)

# get dictionary
content = requests.json()

# access article and description
body = "subject:Today's news\n"
for article in content["articles"][:20]:
    # print(article["title"])
    # print(article["description"])
    if article['title'] is not None and article['description'] is not None:
        body = body + article['title'] + \
               "\n" + article['description'] + \
               "\n" + article['url'] + 2 * "\n"
body = body.encode("utf-8")
gmail.send_mail(message=body)
