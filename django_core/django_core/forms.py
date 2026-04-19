from django import forms

class UsersForm(forms.Form):
    number1= forms.CharField(label="value 1", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    number2= forms.CharField(label="value 2", widget=forms.TextInput(attrs={'class': "form-control"}))