import requests, json
from config import PolygonIOKey, FinnhubIOKey, NewsAPIKey

# Stock Symbols
def getSymbols():
    symbolsRequest = f'https://finnhub.io/api/v1/stock/symbol?exchange=US&currency=&token={FinnhubIOKey}'
    symbolsResponse = requests.get(symbolsRequest)
    symbolsJSON = symbolsResponse.json()

    # print(symbolsJSON)
    return symbolsJSON

#Stock Symbols Details
def getTicker(tickerList):
    for ticker in tickerList:
        print('Ticker:', ticker)
        # detailsRequest = f'https://api.polygon.io/v1/meta/symbols/{ticker}/company?&apiKey={PolygonIOKey}'
        detailsRequest = f'https://finnhub.io/api/v1/stock/profile2?symbol={ticker}&token={FinnhubIOKey}'
        detailsResponse = requests.get(detailsRequest)
        detailsJSON = detailsResponse.json()
        detailsJSON = str(detailsJSON)
        detailsJSON = detailsJSON.replace("'", '"')
        detailsJSON = json.loads(detailsJSON)
        detailsJSON = json.dumps(detailsJSON, indent = 4, sort_keys = True)

        print('Ticker Details:\n', detailsJSON)

        # FinnhubIO
        """
        def displayDetails():
            logo
            name
            country
            marketCapitalization
            volume
            exchange
            industry
        """

        # PolygonIO Response
        """
        def displayDetails():
            logo = detailsJSON['logo']
            country = detailsJSON['hq_country']
            industry = detailsJSON['industry']
            sector = detailsJSON['sector']
            marketcap = detailsJSON['marketcap']
            ceo = detailsJSON['ceo']
            url = detailsJSON['url']
            description = detailsJSON['description']
            name = detailsJSON['name']
            symbol = detailsJSON['symbol']
            state = detailsJSON['hq_state']
            tags = detailsJSON['tags'][0]

            print('Name:', name)
            print('State:', state)
            print('Country:', country)
            print('Symbol:', symbol)
            print('Sector:', sector)
            print('Industry:', industry)
            print('Description:', description)
            print('Market Cap:', marketcap)
            print('CEO:', ceo)
            print('URL:', url)
            print('Tags:', tags)
            print('')
        """

        # displayDetails()

# Stock Market News
def getMarketNews():
    marketNewsRequest = f'https://finnhub.io/api/v1/news?category=general&token={FinnhubIOKey}'
    marketNewsResponse = requests.get(marketNewsRequest)
    marketNewsJSON = marketNewsResponse.json()

    for i in range(len(marketNewsJSON)):
        print('Next Article:', marketNewsJSON[i])
        print('')

    return marketNewsJSON

# Stock Symbols News



# Stock Sector News
def getSectorNews(sector):
    sectorNewsURL = f'https://newsapi.org/v2/everything?q={sector}&apiKey={NewsAPIKey}'
    sectorNewsRequest = requests.get(sectorNewsURL)
    sectorNewsResponse = json.loads(sectorNewsRequest.content)

    # print(sectorNewsResponse)

    sectorArticles = len(sectorNewsResponse['articles'])

    for i in range(sectorArticles):
        author = sectorNewsResponse['articles'][i]['author']
        print(author)

        title = sectorNewsResponse['articles'][i]['title']
        print(title)

        description = sectorNewsResponse['articles'][i]['description']
        print(description)

        url = sectorNewsResponse['articles'][i]['url']
        print(url)

        publishedAt = sectorNewsResponse['articles'][i]['publishedAt']
        print(publishedAt)

        print()

sector = 'energy-sector'

getSectorNews(sector)
