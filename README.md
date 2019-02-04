# book_parse
爬虫练手，解析在线小说，可切换书源

## 主要内容

1. 定义了一个书籍类；
2. 规定了书籍类相关属性的类型和结构；
3. 规定了一些方法的输入输出类型；
4. 实现多书源网站解析。

```python
class Book:
    name = "未知"     # 书名
    cover_url = ''      # 封面URL
    description = ""    # 简介
    author = "未知"       # 作者
    contents = []        # 目录
    latest_chapter = []  # 最新章节
    novel_url = ''       # 小说链接


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

```


## 友情提醒
欢迎第三方加入各种网站解析，望遵守书籍类的类型规定。

遵守书籍类的规定可以提高效率，下图是书籍类思维导图：
![](https://ws1.sinaimg.cn/large/006tNc79ly1fztg62y0gqj31950nd42s.jpg)
