from django import forms
from main.models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'user': forms.HiddenInput(),
            'postal_code': forms.NumberInput()
        }

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'address': 'Адресс',
            'postal_code': 'Почтовый индекс',
            'city': 'Город',
        }

    def __init__(self, *args, **kwargs):
        super(CreateOrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
