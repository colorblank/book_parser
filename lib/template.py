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

SITE_URL = 'https://www.zwda.com'

search_url = 'https://www.zwda.com/search.php?keyword='

keyword = '重生'

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
    book = {
        "书名":"",
        "封面URL":"",
        "简介":"",
        "作者":"",
        "小说链接":"",
    }
    res = []
    return res

def get_chapters(url):
    chapter = {
        "章节名":"",
        "正文":"",
        "章节链接":"",
        "时间戳":0,
    }
    contents = []
    return contents

def get_chapter_content(url):
    paragraph = ""
    paragraphs = []
    return paragraphs


