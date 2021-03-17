import requests, json
from config import FinnhubIOKey

marketNewsRequest = f'https://finnhub.io/api/v1/news?category=general&token={FinnhubIOKey}'
marketNewsResponse = requests.get(marketNewsRequest)
marketNewsJSON = marketNewsResponse.json()

for i in range(len(marketNewsJSON)):

    print(marketNewsJSON[i])

    marketNewsJSON = str(marketNewsJSON[i])

    print(marketNewsJSON)

    marketNewsJSON = marketNewsJSON.replace("'", '"')

    print(marketNewsJSON)

    marketNewsFormatted = json.loads(marketNewsJSON)

    marketNewsFormatted = json.dumps(marketNewsFormatted, indent = 4, sort_keys = True)

    print(marketNewsFormatted)
