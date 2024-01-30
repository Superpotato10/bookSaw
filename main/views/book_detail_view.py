from django.views.generic import DetailView

from main.models import Book


class BookDetailView(DetailView):
    template_name = 'pages/detail.html'
    model = Book
