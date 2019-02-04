from bs4 import BeautifulSoup
import requests
import random
import time


# class Book:
#     name = "未知"     # 书名
#     cover_url = ''      # 封面URL
#     description = ""    # 简介
#     author = "未知"       # 作者
#     contents = []        # 目录
#     latest_chapter = []  # 最新章节
#     novel_url = ''       # 小说链接

# BookSites = {
#     "文学迷": 'https://www.wenxuemi6.com',
#     "E小说": 'https://www.zwda.com',
#     "顶点208": "https://www.208xs.com",
# }


SITE_URL = 'https://www.wenxuemi6.com'
# https://www.zwda.com
search_url = 'https://www.wenxuemi6.com/search.php?keyword='
# https://www.zwda.com/search.php?keyword=
keyword = '重生'
# 重生
header = [{'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
          {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
          {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}
]


def get_soup(any_url):
    # 传入链接
    # 返回BeautifulSoup对象
    result = requests.get(any_url, headers=header[random.randint(0, 4)])
    html_doc = result.content
    try:
        html_doc = html_doc.decode('utf-8')
    except UnicodeDecodeError:
        html_doc = html_doc.decode('gbk')
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup


def search(keyword):

    res = []
    url = search_url + keyword
    soup = get_soup(url)
    res_tags = soup.find_all("div", class_="result-item result-game-item")

    for res_tag in res_tags:
        book = {
            "书名": "",
            "封面URL": "",
            "简介": "",
            "作者": "",
            "小说链接": "",
        }
        img_tag = res_tag.find_all("img",class_="result-game-item-pic-link-img")[0]
        book["封面URL"] = img_tag["src"]


        name_tag = res_tag.find("a",class_="result-game-item-title-link")
        book["书名"] = name_tag["title"]

        description_tag = res_tag.find("p",class_="result-game-item-desc")
        description = description_tag.get_text()
        book["简介"] = "".join(description.split())
        # 5. 筛选作者
        p_tag = res_tag.find_all("p",class_="result-game-item-info-tag")[0]
        author_tag = p_tag.find_all("span")[-1]
        author = author_tag.get_text()
        book["作者"] = "".join(author.split())
        # 5. 筛选小说链接
        book["小说链接"] = name_tag["href"]
        res.append(book)

    return res

def get_chapters(url):
    contents = []
    soup = get_soup(url)
    div_tag =  soup.find_all("div",id="list")[0]
    a_tags = div_tag.find_all("a")
    for a_tag in a_tags:
        chapter = {
            "章节名": "",
            "正文": "",
            "章节链接": "",
            "时间戳": 0,
        }
        chapter["章节名"] = a_tag.get_text()
        chapter_url = SITE_URL + a_tag["href"]
        chapter["章节链接"] = chapter_url
        update_time = int(time.time())
        chapter["时间戳"] = update_time
        contents.append(chapter)
    return contents

def get_chapter_content(url):
    paragraphs = []
    soup = get_soup(url)
    content_tag = soup.find_all("div",id="content")[0]
    texts = content_tag.find_all(text=True)
    for text in texts:
        paragraph = "".join(text.split())
        paragraphs.append(paragraph)
    return paragraphs

# if __name__ == '__main__':
#     res = search(keyword)
#     #print(res)
#
#     book_url = res[0]["小说链接"]
#     chapters = get_chapters(book_url)
#     #print(chapters)
#
#     chap_url = 'https://www.wenxuemi6.com/files/article/html/26/26059/13077769.html'
#     p = get_chapter_content(chap_url)
#

