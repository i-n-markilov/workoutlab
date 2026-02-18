from django import forms


class NameSearchForm(forms.Form):
    name = forms.CharField(max_length=150,
                            label='',
                            required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Search by name..',}))