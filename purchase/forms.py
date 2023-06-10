from django import forms
from django.core.exceptions import ValidationError


class PurchaseForm(forms.Form):
    address = forms.CharField(max_length=100, label='Адрес',
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control'
                              }))
    city = forms.CharField(max_length=50, label='Город', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    state = forms.CharField(max_length=50, label='Область', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    country = forms.CharField(max_length=50, label='Страна', widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    zip_code = forms.CharField(max_length=10, label='Почтовый индекс', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    def clean_city(self):
        value = self.cleaned_data['city']
        return value.capitalize()

    def clean_country(self):
        value = self.cleaned_data['country']
        return value.capitalize()

    def clean_state(self):
        value = self.cleaned_data['state']
        return value.capitalize()

    def clean_zip_code(self):
        value = self.cleaned_data['zip_code']
        if value.isalnum() and len(value) == 6:
            return value
        else:
            raise ValidationError(f'{value}-это не индекс')
