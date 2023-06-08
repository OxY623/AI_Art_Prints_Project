from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(min_length=3, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("title", "Title"),
                                      ("description", "Description")
                                  ), widget=forms.Select(attrs={'class': 'form-control'}))