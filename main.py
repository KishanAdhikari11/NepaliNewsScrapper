from onlinekhabar import OnlinekhabarScraper

def main():
    url = "https://www.onlinekhabar.com/2024/03/1443168"
    scraper = OnlinekhabarScraper(url)
    news_json = scraper.get_news_json()
    print(news_json)

if __name__ == "__main__":
    main()
