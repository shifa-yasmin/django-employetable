from django import forms
class employe(forms.Form):
    name=forms.CharField(max_length=100)
    place=forms.CharField(max_length=100)
    DOB=forms.DateField()