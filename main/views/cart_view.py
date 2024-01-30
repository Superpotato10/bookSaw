from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class CartView(TemplateView, LoginRequiredMixin):
    template_name = 'pages/cart.html'
