import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/India"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.select("div.mw-parser-output > p")

for p in content:
    text = p.get_text(strip=True)
    if text:   # skip empty paragraphs
        print(text)
        print()
