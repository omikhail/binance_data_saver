import requests
import csv
import time
import os


def collect_order_book_data(pair, limit):
    url = f'https://api.binance.com/api/v3/depth?symbol={pair}&limit={limit}'
    response = requests.get(url).json()
    bids = response['bids']
    asks = response['asks']

    timestamp = int(time.time())
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{symbol}.csv")

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        for bid in bids:
            price, qty = float(bid[0]), float(bid[1])
            writer.writerow([timestamp, 'bid', price, qty])
        for ask in asks:
            price, qty = float(ask[0]), float(ask[1])
            writer.writerow([timestamp, 'ask', price, qty])

    print(f"Data collected and appended to {filename} for symbol {symbol}")


symbol = 'BTCUSDT'  # Здесь можно указать нужный символ
depth_limit = 10  # Здесь можно указать нужную глубину стакана
puase = 60

while True:
    collect_order_book_data('BTCUSDT', depth_limit)
    collect_order_book_data('ADAUSDT', depth_limit)
    collect_order_book_data('ETHBTC', depth_limit)
    collect_order_book_data('XRPUSDT', depth_limit)
    collect_order_book_data('BNBBTC', depth_limit)

    collect_order_book_data('DOTUSDT', depth_limit)
    collect_order_book_data('SOLUSDT', depth_limit)
    collect_order_book_data('MATICUSDT', depth_limit)
    collect_order_book_data('DOGEUSDT', depth_limit)
    collect_order_book_data('LINKUSDT', depth_limit)

    time.sleep(puase)

# в  файл с названием соответсвующем паре записываються 10 лучших ордеров на покупку и на продажу (глубина стакана)
# Timestamp: текущая дата и время, когда был получен стакан
# Price: цена ордера в стакане
# Quantity: количество валюты в ордере
# Type: тип ордера (bid - ордер на покупку, ask - ордер на продажу)
