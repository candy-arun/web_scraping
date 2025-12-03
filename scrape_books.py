import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")

for b in books:
    title = b.h3.a["title"]
    price = b.select_one(".price_color").text
    availability = b.select_one(".availability").text.strip()

    print("Title:", title)
    print("Price:", price)
    print("Availability:", availability)
    print("-" * 40)
