import random

from django.views.generic import TemplateView

from main.models import Book, Genre


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()

        new_books = list(filter(lambda book: book.is_new(), books))
        context['new_books'] = new_books[:2]
        context['last_new_books'] = new_books[:4]
        context['random_book'] = random.choice(new_books)
        context['genres'] = Genre.objects.all()[:6]
        context['discount_books'] = list(filter(lambda book: book.is_discounted(), books))[:4]
        return context
