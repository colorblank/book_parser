from lib.Exiaoshuo import search,get_chapters,get_chapter_content


class Book:
    name = "未知"     # 书名
    cover_url = ''      # 封面URL
    description = ""    # 简介
    author = "未知"       # 作者
    contents = []        # 目录
    latest_chapter = []  # 最新章节
    novel_url = ''       # 小说链接


if __name__ == '__main__':

    # 0. 创建一个书籍类
    new_book = Book()

    # 1. 搜索小说，返回搜索结果
    search_res = search("重生")
    print(search_res)

    # 2. 默认选择第一个结果，返回结果的书籍信息
    book_info = search_res[0]
    print(book_info)

    # 3. 写入书籍信息
    new_book.name = book_info["书名"]
    new_book.author = book_info["作者"]
    new_book.description = book_info["简介"]
    new_book.cover_url = book_info["封面URL"]
    new_book.novel_url = book_info["小说链接"]

    # 4. 根据小说链接解析目录，返回目录列表
    chapters = get_chapters(new_book.novel_url)
    new_book.contents = chapters
    print(chapters)

    # 5. 遍历小说目录链接，解析正文，返回正文段落列表
    # 下面是解析第一章内容，并写入书籍目录
    for id,chapter in enumerate(new_book.contents):
        url = chapter["章节链接"]
        context = get_chapter_content(url)
        new_book.contents[id]["正文"] = context
        break
    print(context)

    # 6. 选择某一章解析 | 解析全文 | 解析后30章

    # 7. 书籍类目录属性自动更新
