from django import forms


class FormMembers(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
