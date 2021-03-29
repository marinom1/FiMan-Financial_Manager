import requests, json
from config import FinnhubIOKey

symbolsRequest = f'https://finnhub.io/api/v1/stock/symbol?exchange=US&currency=&token={FinnhubIOKey}'
symbolsResponse = requests.get(symbolsRequest)
symbolsJSON = symbolsResponse.json()

for i in range(len(symbolsJSON)):
    symbolsJSON = str(symbolsJSON[i])
    symbolsJSONFormatted = symbolsJSON.replace("'", '"')
    print(symbolsJSONFormatted)

"""
for j in range(len(symbolsJSON)):
    description = symbolsJSON[j]['description']
    print(description)
"""

"""
Debugging

print(len(symbolsJSON))
print(symbolsJSON)
"""
