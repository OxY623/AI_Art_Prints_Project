from django import forms
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

