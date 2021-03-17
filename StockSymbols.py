import requests
from config import FinnhubKey

symbolsRequest = f'https://finnhub.io/api/v1/stock/symbol?exchange=US&currency=&token={FinnhubKey}'
symbolsResponse = requests.get(symbolsRequest)
symbolsJSON = symbolsResponse.json()

for i in range(len(symbolsJSON)):
    description = symbolsJSON[i]['description']
    print(description)

"""
Debugging

print(len(symbolsJSON))
print(symbolsJSON)
"""