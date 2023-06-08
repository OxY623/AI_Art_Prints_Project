from django import forms

class PurchaseForm(forms.Form):
    address = forms.CharField(max_length=100, label='Адрес')
    city = forms.CharField(max_length=50, label='Город')
    state = forms.CharField(max_length=50, label='Штат')
    country = forms.CharField(max_length=50, label='Страна')
    zip_code = forms.CharField(max_length=10, label='Почтовый индекс')