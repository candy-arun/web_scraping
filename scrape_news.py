import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Every news block is inside <li class="BxDma">
items = soup.find_all("li", class_="BxDma")

news_list = []

for item in items:
    link_tag = item.find("a")
    headline_tag = item.find("div", class_="CRKrj")

    if link_tag and headline_tag:
        headline = headline_tag.text.strip()
        link = link_tag["href"]

        # TOI sometimes gives URLs without "https:"
        if link.startswith("//"):
            link = "https:" + link

        news_list.append((headline, link))

# Print results
for h, l in news_list:
    print("•", h)
    print("  Link:", l)
    print()
