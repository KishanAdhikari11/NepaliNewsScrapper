from onlinekhabar import OnlinekhabarScraper
from nayapatrika import NayaPatrikaScraper
from ratopati import RatopatiScraper
from gorkhapatra import GorkhapatraScraper
from setopati import SetopatiScraper
from ekantipur import EkantipurkhabarScraper
from base import BaseScraper

SCRAPERS = {
    "onlinekhabar": OnlinekhabarScraper,
    "nayapatrika": NayaPatrikaScraper,
    "ratopati": RatopatiScraper,
    "gorkhapatra": GorkhapatraScraper,
    "setopati": SetopatiScraper,
    "ekantipur":EkantipurkhabarScraper
}

def main():
    url = input("Enter Url: ")
    base_scraper = BaseScraper(url)  
    portal_name = base_scraper.portal_name  
    print("Detected portal:", portal_name)
    scrapper_class=SCRAPERS.get(portal_name)
    scrapper=scrapper_class(url)
    news_json=scrapper.get_news()
    print(news_json)


if __name__ == "__main__":
    main()
