from django.shortcuts import render

from divisasproject.webapp.forms import *

# Create your views here.


def index(request):
    form = ConverterForm
    if request.method == 'POST':
        amount           = request.POST['amount']
        current_currency = request.POST['current_currency']
        desired_currency = request.POST['desired_currency']

        # si current_currency no es igual a euros entonces lo convierte antes de convertirlo a desired_currency
        if current_currency != 'EUR':
            amount_in_euro = int(amount) / rates.get(current_currency)
            result = amount_in_euro * rates.get(desired_currency)

        # o si la current_currency es igual a euros entonces lo convierte a la desired_currency
        elif str(current_currency) == 'EUR':
            result      = int(amount) / rates.get(current_currency)
        
        # obteniendo el simbolo tanto del currento como del desired currency
            current_currency_symbol = CurrencySymbols.get_symbol(current_currency)
            desired_currency_symbol = CurrencySymbols.get_symbol(desired_currency)
            context = {
                'result' = result,
                'amount' = amount,
                'current_currency_symbol' = current_currency_symbol,
                'desired_currency_symbol' = desired_currency_symbol,
                'form' = form
            }

    else:
        return render(request, 'index.html', {'form':form})
