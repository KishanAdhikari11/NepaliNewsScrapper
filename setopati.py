from base import BaseScraper

class SetopatiScraper(BaseScraper):
    def get_news(self):
        soup = self.get_soup()
        news = soup.find('div', class_='editor-box')
        if news:
            news_paragraphs = news.find_all('p')
            news_content = []
            for p in news_paragraphs:
                paragraph = p.text.strip()  # Strip to remove extra whitespace
                if paragraph:  # Exclude empty paragraphs
                    news_content.append(paragraph)
            return ' '.join(news_content)
        else:
            return "No news found on Setopati"
