import requests
from config import PolygonIOKey

# Ticker Details
def getTicker(tickerList):
    for ticker in tickerList:
        print('Ticker:', ticker)
        details = f'https://api.polygon.io/v1/meta/symbols/{ticker}/company?&apiKey={PolygonIOKey}'

        responseDetails = requests.get(details)
        detailsJSON = responseDetails.json()

        print('Ticker Details:')
        # print(detailsJSON)

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

def main():
    enterTickers = input('Enter your preferred stock tickers (FB AMZN APPL NFLX GOOGL etc.): ')
    enterTickers = enterTickers.upper()
    tickerList = enterTickers.split()
    # print(tickerList)
    print('Generating details for selected tickers...')
    getTicker(tickerList)

main()