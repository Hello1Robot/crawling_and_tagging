import requests
from bs4 import BeautifulSoup
import time

# --------------------- 크롤링 파트 ---------------------------- #
# user input
keywords = ["경제","사회","문화","생활","과학"]
lastpage = 1

for keyword in keywords:
    page_num = 1
    for i in range(1, lastpage * 10, 10):
        print(f"{page_num} page...")
        response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}&sort=1")
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.select("div.info_group")

        for article in articles:
            links = article.select("a.info")
            if len(links) >= 2:
                url = links[1].attrs["href"]
                response = requests.get(url, headers={'User-agent': 'Mozila/5.0'})      # to avoid error use headers
                html = response.text                                                    # for each url get html
                soup = BeautifulSoup(html, "html.parser")                               # for each html make soup
                try:
                    # separation
                    if "entertain" in response.url:                                         # to avoid redirection error
                        title = soup.select_one(".end_tit")                                 # get the title
                        content = soup.select_one("#articeBody")                            # get the body

                    elif "sports" in response.url:                                          # to avoid redirection error
                        title = soup.select_one("h4.title")                                 # get the title
                        content = soup.select_one("#newsEndContents")                       # get the body

                        # delete unnecessary elements
                        divs = content.select("div")
                        for div in divs:
                            div.decompose()

                        paragraphs = content.select("p")
                        for p in paragraphs:
                            p.decompose()

                    else:
                        title = soup.select_one(".media_end_head_headline")                 # get the title
                        content = soup.select_one("#dic_area")                              # get the body
                except:
                    title = "잘못된 게시글입니다."
                    content = " "

                # print("========LINK========\n", url)
                print("========TITLE========\n", title.text.strip())
                print("========BODY========\n", content.text.strip())
                time.sleep(0.3)

        page_num += 1

# --------------------- 크롤링 파트 끝 ---------------------------- #
# --------------------- 형태소 분석파트 시작 ---------------------- #
from soynlp.utils import DoublespaceLineCorpus

corpus_fname = 'processed_wiki_ko.txt'
sentences = DoublespaceLineCorpus(corpus_fname, iter_sent=True)
len(sentences)