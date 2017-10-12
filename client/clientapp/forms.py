from django import forms

class NameForm(forms.Form):
    Phone = forms.CharField(label='Your Phone.no', max_length=100)
    Pwd = forms.CharField(label='Your Pwd', max_length=100)
