import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Movie cards (new IMDb structure)
movies = soup.select("div.sc-fc35a1ef-1.lmHCrT.cli-parent.li-compact")

for movie in movies:
    # title
    title_tag = movie.select_one("span.ipc-title__text")
    title = title_tag.text.strip() if title_tag else "N/A"

    # link
    link_tag = movie.select_one("a.ipc-title-link-wrapper")
    if link_tag:
        link = "https://www.imdb.com" + link_tag["href"]
    else:
        link = "N/A"

    # find year (inside the metadata section)
    year_tag = movie.select_one("span.dli-title-metadata-item")
    year = year_tag.text.strip() if year_tag else "N/A"

    print("Title:", title)
    print("Year:", year)
    print("Link:", link)
    print("-" * 50)
