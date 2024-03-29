# Class

# #### Article variables
title1 = "개발"
author1 = "마르코"
content1 = "개발은 쉬워요"
view_count1 = 0

title2 = "코칭"
author2 = "마르코"
content2 = "코칭은 쉬워요"
view_count2 = 0

title3 = "창업"
author3 = "마르코"
content3 = "창업은 쉬워요"
view_count3 = 0

##### Article Class
# class Article:
#     title = "개발"
#     author = "마르코"
#     content = "개발은 쉬워요"
#     view_count = 0
#
# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "코칭"
# print(article1.title)
# print(article2.title)

class Article():
    """docstring for Article."""
    author = "마르코"
    view_count = 0

    def __init__(self, title, content):
        super(Article, self).__init__()
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

# print(article1.view_count)
# article1.read()

######## Article class inheritance 상속
