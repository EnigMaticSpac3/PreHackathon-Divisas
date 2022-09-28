from django import forms
from webapp.functions import *

rates    = rate_display('https://api.exchangerate.host/latest')
symbols  = symbols_display(rates)
new_list = convert_list(symbols)


class ConverterForm(forms.Form):
    amount              = forms.IntegerField()
    current_currency    = forms.ChoiceField(choices=new_list)
    desired_currency    = forms.ChoiceField(choices=new_list)
