import requests
import gmail

api_key = "86a80f8923b5436d836ba3ae2cf87825"

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-21&sortBy=\
publishedAt&apiKey=86a80f8923b5436d836ba3ae2cf87825"

requests = requests.get(url)


# get dictionary
content = requests.json()

# access article and description
body = ""
for article in content["articles"]:
    # print(article["title"])
    # print(article["description"])
    if article['title'] is not None and article['description'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"
body = body.encode("utf-8")
gmail.send_mail(message=body)


