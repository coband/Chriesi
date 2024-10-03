from django import forms
from .models import Book

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'ISBN', 'subject', 'published_date']

class BuchForm(forms.Form):
    titel = forms.CharField(label='Titel', max_length=100)
    autor = forms.CharField(label='Autor', max_length=100)
    fach = forms.CharField(label='Fach', max_length=100)
    erscheinungsjahr = forms.IntegerField(label='Erscheinungsjahr')
    stufe = forms.MultipleChoiceField(
        label='Stufe',
        choices=[
            ('KiGa', 'KiGa'),
            ('1. Klasse', '1. Klasse'),
            ('2. Klasse', '2. Klasse'),
            ('3. Klasse', '3. Klasse'),
            ('4. Klasse', '4. Klasse'),
            ('5. Klasse', '5. Klasse'),
            ('6. Klasse', '6. Klasse'),
        ],
        widget=forms.SelectMultiple,
        required=True,
    )