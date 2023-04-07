from django import forms

from .models import card


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = card
        fields = ['__all__']

# class studForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     cardno = forms.IntegerField()
#     expiredate = forms.DateField()
#     qr_code = forms.ImageField()
