import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

#prices = client.get_all_tickers()
#print(prices)

#for price in prices:
#    print(price)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('RealTime.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

#for candlestick in candles:
    #print(candlestick)

    #candlestick_writer.writerow(candlestick)

#print(len(candles))

#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jul, 2020")
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "22 Jul, 2021")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 Jul, 2020")

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()