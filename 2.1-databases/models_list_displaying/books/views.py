from django.shortcuts import render

from .models import Book


def books_catalog_view(request, pub_date=None):
    template = 'books/books_list.html'
    books_catalog = Book.objects.all()
    context = {'books_catalog': books_catalog}
    if pub_date:
        template = 'books/about_book.html'
        books_catalog = books_catalog.filter(pub_date=pub_date)
        prev_page = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
        next_page = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

        prev_page = prev_page.pub_date.strftime('%Y-%m-%d') if prev_page else None
        next_page = next_page.pub_date.strftime('%Y-%m-%d') if next_page else None

        context = {'books_catalog': books_catalog,
                   'prev_page': prev_page,
                   'next_page': next_page
                   }
    return render(request, template, context)
