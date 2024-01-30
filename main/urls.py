from django.urls import path

from main.views import HomeView, BookDetailView, BooksListView, CartView, CheckoutView
from main.views.order_list_view import OrdersListView

app_name = 'main'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("books/", BooksListView.as_view(), name="books"),
    path("detail/<int:pk>/", BookDetailView.as_view(), name="detail"),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("last-orders/", OrdersListView.as_view(), name="last-orders"),
]
