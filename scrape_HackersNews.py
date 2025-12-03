import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.select(".titleline a")

for i, item in enumerate(items[:30], start=1):
    print(i, item.text)
    print("Link:", item["href"])
    print()
