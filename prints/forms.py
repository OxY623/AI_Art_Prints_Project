from django import forms
from .models import Print
from django.core.exceptions import ValidationError


class SearchForm(forms.Form):
    search = forms.CharField(min_length=3, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("title", "Title"),
                                      ("description", "Description")
                                  ),
                                  widget=forms.Select(
                                      attrs={
                                          'class': 'form-control'
                                      }))


class SearchPrintsForm(forms.Form):
    date_from = forms.DateField(required=False,
                                widget=forms.DateInput(attrs=
                                                       {'type': 'date',
                                                        'class': 'form-control'
                                                        }))
    date_to = forms.DateField(required=False,
                              widget=forms.DateInput(attrs=
                                                     {'type': 'date',
                                                      'class': 'form-control'
                                                      }))
    price_from = forms.IntegerField(required=False,
                                    widget=forms.NumberInput(attrs=
                                    {
                                        'type': 'number',
                                        'class': 'form-control'
                                    }), min_value=0, max_value=9999)
    price_to = forms.IntegerField(required=False,
                                  widget=forms.NumberInput(attrs=
                                  {
                                      'type': 'number',
                                      'class': 'form-control'
                                  }), min_value=0, max_value=9999)



class PrintFormCreate(forms.ModelForm):
    class Meta:
        model = Print
        fields = ['title', 'artist', 'description', 'image', 'quantity', 'price']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1 or quantity > 50:
            raise forms.ValidationError('Количество должно быть от 1 до 50.')
        return quantity

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0 or price >= 100000:
            raise forms.ValidationError('Цена должна быть от 0.02 до 99999.')
        return price
