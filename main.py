import requests

def get_bitcoin_price():
    url = 'https://min-api.cryptocompare.com/data/price'
    params = {'fsym': 'BTC', 'tsyms': 'USD'}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('USD', 'Price not available')

if __name__ == '__main__':
    price = get_bitcoin_price()
    print(f'The current price of Bitcoin is: {price}')