import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 검색어와 검색 페이지
query = '야구'
page = 1

# 100개의 기사 주소, 제목, 내용 크롤링
for i in range(10):
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={query}&start={page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('div.news_area')
    
    for article in articles:
        title = article.select_one('a.news_tit').text
        url = article.select_one('a.news_tit')['href']
        response_article = requests.get(url)
        soup_article = BeautifulSoup(response_article.text, 'html.parser')
        content = soup_article.select_one('div#articleBodyContents').text.strip()
        print('제목:', title)
        print('URL:', url)
        print('내용:', content)
    
    page += 10