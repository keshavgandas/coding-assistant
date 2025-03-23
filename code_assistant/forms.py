from django import forms 

class ProblemForm(forms.Form):
    query = forms.CharField(max_length=255 , widget= forms.TextInput(attrs = {'placeholder': 'Ask your problem'}))