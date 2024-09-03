import requests

def get_stock_price(symbol):
    api_key = 'your_api_key'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['Time Series (5min)'][0]['1. open']