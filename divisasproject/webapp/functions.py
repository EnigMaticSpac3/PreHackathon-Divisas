import requests
def rate_display(url):
    return requests.get(url)

def symbols_display(data):
    return requests.get(data)

def CurrencySymbols():
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    return data
def get_symbol(a):
    
    return a
def convert_list(lst = list):
    """
    :param lst takes the list object
    :return a list of tuples
    """

    nw_list = list()
    for x in lst:
        tp = (x,x)
        nw_list.append(tp)
    return nw_list