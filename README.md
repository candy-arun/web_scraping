# Web Scraping Practice – Python 🕸️🐍

This repository contains multiple beginner-friendly web scraping scripts built using
Requests + BeautifulSoup.

Each script scrapes real websites such as IMDb, Hacker News, Books to Scrape,
NDTV News, Wikipedia, and more.

This project is made for learning, experimentation, and understanding how
web data extraction works.

---

## 📦 Project Structure

SCRAPPING_QUOTES/
- scrape_books.py
- scrape_HackersNews.py
- scrape_imdb.py
- scrape_MeteoWeather.py
- scrape_news.py
- scrape_quotes.py
- scrape_wikepedia.py

Each file targets a different website.

---

## 🛠️ Requirements

Install dependencies:

pip install requests  
pip install beautifulsoup4

---

## ▶️ How to Run

Run any script like this:

python scrape_books.py  
python scrape_imdb.py

---

## 🌐 Websites Covered

| Script | Website | Data Scraped |
|--------|---------|---------------|
| scrape_books.py | https://books.toscrape.com | Titles, prices, availability |
| scrape_HackersNews.py | https://news.ycombinator.com | Latest headlines |
| scrape_imdb.py | https://imdb.com/chart/top | Top movies, rating, year |
| scrape_MeteoWeather.py | https://open-meteo.com | Current weather |
| scrape_news.py | NDTV / TOI | Latest India news headlines |
| scrape_quotes.py | https://quotes.toscrape.com | Quote text & author |
| scrape_wikepedia.py | https://wikipedia.org | Article paragraphs |

---

## ⚠️ Important: Website Structure May Change

Web scraping depends on the website's HTML structure:

- Tags (div, p, span)
- Class names (titleColumn, ipc-title__text)
- IDs and attributes

If the site updates its HTML, your scraper may break.

Example:
If website changes:

<div class="movie-title">

to:

<div class="film-title">

Update your scraper:

from: .movie-title  
to:   .film-title

This is normal in web scraping.

---

## 📚 Learning Goals

These scripts teach you:

- Sending HTTP requests
- Parsing HTML using BeautifulSoup
- Extracting text, links, and lists
- Debugging scrapers using browser inspect
- Handling dynamic class names
- Understanding when websites break scrapers

---

## 🚀 Future Enhancements

- Save scraped data to CSV or JSON
- Handle pagination
- Add Selenium for JavaScript-heavy sites
- Add proxy/user-agent rotation
- Add error handling and retries

---

## 🤝 Contributing

Pull requests are welcome.
Feel free to add new scrapers or improve existing code.

---

## 📄 License

This project is for educational & learning use only.
Respect all website Terms of Service and robots.txt.
