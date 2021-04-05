import requests, json
from config import FinnhubIOKey

symbolsRequest = f'https://finnhub.io/api/v1/stock/symbol?exchange=US&currency=&token={FinnhubIOKey}'
symbolsResponse = requests.get(symbolsRequest)
symbolsJSON = symbolsResponse.json()

print(symbolsJSON)

"""
Debugging

print(len(symbolsJSON))
print(symbolsJSON)
"""
