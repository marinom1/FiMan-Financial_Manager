import requests
from config import NewsAPIKey

# Test cases

sector = 'Financial-Technology-Sector'

sectorNewsRequest = f'https://newsapi.org/v2/everything?q={sector}&sortBy=popularity&apiKey={NewsAPIKey}'
sectorNewsResponse  = requests.get(sectorNewsRequest)
sectorNewsJSON = sectorNewsResponse.json()

print(sectorNewsJSON) 
