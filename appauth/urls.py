from django.contrib.auth.views import LogoutView
from django.urls import path

from appauth.views import LoginView, RegistrationView
from booksShop import settings

app_name = 'appauth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]
