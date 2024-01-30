from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from main.models import Order


class OrdersListView(ListView, LoginRequiredMixin):
    template_name = 'pages/orders-list.html'
    model = Order

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
