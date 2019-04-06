from django import forms


class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(),label="Password")


class PartyID:
    id = forms.CharField(label="Game Token", max_length=4)