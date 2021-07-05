from django.urls import path

from articles.views import show_articles

urlpatterns = [
    path('', show_articles, name='articles'),
]
