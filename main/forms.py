from django import forms

class Rejestracja(forms.Form):
    name = forms.CharField(label="Imie", max_length=52)
    surname = forms.CharField(label="Nazwisko", max_length=52)
    goodAge = forms.BooleanField(label="Mam ukończone 18 lat")