import requests
from operator import itemgetter
from config import PolygonIOKey

def main():
    enterTickers = input('Enter your preferred stock tickers (FB AMZN APPL NFLX GOOGL etc.): ')
    enterTickers = enterTickers.upper()
    print(enterTickers)
    tickerList = enterTickers.split()
    # print(tickerList)
    print('Generating news articles for selected tickers...')
    getTicker(tickerList)

# Ticker Details and News
def getTicker(tickerList):
    for ticker in tickerList:
        print('Ticker:', ticker)
        details = f'https://api.polygon.io/v1/meta/symbols/{ticker}/company?&apiKey={PolygonIOKey}'
        news = f'https://api.polygon.io/v1/meta/symbols/{ticker}/news?perpage=1&page=1&apiKey={PolygonIOKey}'

        responseDetails = requests.get(details)
        responseNews = requests.get(news)
        detailsJSON = responseDetails.json()
        newsJSON = responseNews.json()
        
        print('Ticker Details:\n', detailsJSON)
        print('')
        print('Ticker News:\n', newsJSON)
        print('')

        for i in range(len(newsJSON)):
            title = newsJSON[i]['title']
            url = newsJSON[i]['url']
            source = newsJSON[i]['source']
            summary = newsJSON[i]['summary']

            print('Title:', title)
            print('URL: ', url)
            print('Source:', source)
            print('Summary: ', summary)

            print('')
            print('Next Article')

main()