class Article_context:
    title = "bugungi yngilik"
    content = "yangilik xaqida to'liq malumot"


class Article(Article_context):
    published = "04/04/2024"


new_article = Article()
print(new_article.published)
print(new_article.title)