from cart.apps import CartConfig
from django.http import HttpResponseRedirect
from django.views import View


class ClearCartView(View):
    def post(self, request, *args, **kwargs):
        request.session[CartConfig.cart_session_key] = {}
        return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])
