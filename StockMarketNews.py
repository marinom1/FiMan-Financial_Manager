import requests
from config import FinnhubIOKey

marketNewsRequest = f'https://finnhub.io/api/v1/news?category=general&token={FinnhubIOKey}'
marketNewsResponse = requests.get(marketNewsRequest)
marketNewsJSON = marketNewsResponse.json()

img = marketNewsJSON[0]['image']

print(img)

"""
for i in range(len(marketNewsJSON)):
    print('Next Article:', marketNewsJSON[i])
    print('')
"""