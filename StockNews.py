import requests
from config import PolygonIOKey

# Ticker News
def getTicker(tickerList):
    for ticker in tickerList:
        print('Ticker:', ticker)
        news = f'https://api.polygon.io/v1/meta/symbols/{ticker}/news?perpage=1&page=1&apiKey={PolygonIOKey}'

        responseNews = requests.get(news)
        newsJSON = responseNews.json()

        print('Ticker News:')

        def displayArticles():
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

        displayArticles()

def main():
    enterTickers = input('Enter your preferred stock tickers (FB AMZN APPL NFLX GOOGL etc.): ')
    enterTickers = enterTickers.upper()
    tickerList = enterTickers.split()
    # print(tickerList)
    print('Generating news articles for selected tickers...')
    getTicker(tickerList)

main()