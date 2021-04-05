import requests, json
from config import PolygonIOKey, FinnhubIOKey

# Ticker Details
def getTicker(tickerList):
    for ticker in tickerList:
        print('Ticker:', ticker)
        # details = f'https://api.polygon.io/v1/meta/symbols/{ticker}/company?&apiKey={PolygonIOKey}'
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

        displayDetails()
        """

def main():
    enterTickers = input('Enter your preferred stock tickers (FB AMZN AAPL NFLX GOOGL etc.): ')
    enterTickers = enterTickers.upper()
    tickerList = enterTickers.split()
    # print(tickerList)
    print('Generating details for selected tickers...')
    getTicker(tickerList)

main()
