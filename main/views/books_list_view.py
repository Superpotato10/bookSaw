from django.views.generic import ListView

from main.models import Book, Genre


class BooksListView(ListView):
    template_name = 'pages/book-list.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_genres = Genre.objects.all()
        context['first_genres'] = all_genres[:5]
        context['rest_genres'] = all_genres[5:]

        selected_genres = self.request.GET.getlist('genres')
        context['selected_genres'] = selected_genres

        is_discounted = self.request.GET.get('is_discounted') == 'on'
        context['is_discounted'] = is_discounted

        is_new = self.request.GET.get('is_new') == 'on'
        context['is_new'] = is_new

        search = self.request.GET.get('search')

        if len(selected_genres) != 0:
            context['book_list'] = Book.objects.filter(genres__in=selected_genres).distinct()

        if is_discounted:
            context['book_list'] = context['book_list'].filter(discount__gt=0)

        if is_new:
            context['book_list'] = [book for book in context['book_list'] if book.is_new()]

        if search is not None:
            context['book_list'] = Book.objects.filter(name__icontains=search)

        return context
