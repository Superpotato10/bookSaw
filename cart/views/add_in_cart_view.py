from cart.apps import CartConfig
from django.http import HttpResponseRedirect
from django.views import View


class AddInCartView(View):
    def post(self, request, *args, **kwargs):
        pk = str(kwargs['pk'])
        cart = request.session.get(CartConfig.cart_session_key, {})

        book_count = cart.get(pk, 0)
        cart[pk] = book_count + 1

        request.session[CartConfig.cart_session_key] = cart

        return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])
