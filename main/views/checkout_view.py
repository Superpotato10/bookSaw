from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cart.apps import CartConfig
from main.forms import CreateOrderForm
from main.models import Order, Book, OrderItem


class CheckoutView(CreateView, LoginRequiredMixin):
    model = Order
    form_class = CreateOrderForm
    template_name = 'pages/checkout.html'

    def get_initial(self):
        initial = super(CheckoutView, self).get_initial()
        return {
            'user': self.request.user,
            **initial
        }

    def form_valid(self, form):
        self.object = form.save()

        cart = self.request.session.get(CartConfig.cart_session_key)
        data = [(Book.objects.get(id=int(id)), int(count)) for id, count in cart.items()]
        items = [OrderItem(product=book, order=self.object, price=book.get_price(), count=count)
                 for book, count in data]

        for item in items:
            item.save()

        self.request.session[CartConfig.cart_session_key] = {}

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("main:last-orders")
