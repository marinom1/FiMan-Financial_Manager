import requests, json
from config import FinnhubIOKey

def getSymbols():
    symbolsRequest = f'https://finnhub.io/api/v1/stock/symbol?exchange=US&currency=USD&token={FinnhubIOKey}'
    symbolsResponse = requests.get(symbolsRequest)
    symbolsJSON = symbolsResponse.json()

    print(symbolsJSON)

getSymbols()