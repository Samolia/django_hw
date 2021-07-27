from django.shortcuts import render

from articles.models import Article, Scope


def show_articles(request):
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related('scopes', 'scopes__tag')
    context = {
        'object_list': articles
    }
    return render(request, template, context)