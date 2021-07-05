from django.shortcuts import render

from articles.models import Article, Scope


def show_articles(request):
    template = 'articles/news.html'
    about_articles = []
    articles = Article.objects.all()
    for article in articles:
        scope = Scope.objects.filter(article=article).all()
        about_articles.append({
            'title': article.title,
            'text': article.text,
            'image': article.image,
            'scopes': scope,
        })

    context = {'object_list': about_articles}
    return render(request, template, context)
