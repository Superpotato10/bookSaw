from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView

from appauth.forms import RegistrationForm

User = get_user_model()


class RegistrationView(CreateView):
    template_name = 'pages/registration.html'
    model = User
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse_lazy("main:home")
