from datetime import datetime, date
from sys import argv as argv 
from stock import Stock
import os

start = datetime.now()
cur_time = datetime.now()

ticker_file = open(argv[1], 'r')
stocks = [Stock(ticker.strip()) for ticker in ticker_file]

header = '{0:>10}{1:>15}{2:>15}{3:>15}{4:>15}'.format('TICKER', 'DAY OPEN', 'LIVE PRICE', 'CHANGE', '% Change')

while True:
    current = datetime.now()

    banner = '{0:^70}'.format(f'LAST UPDATED [{date.today()} {current.hour}:{str(current.minute).zfill(2)}:{str(current.second).zfill(2)}]')
    output = banner + '\n' + header

    for stock in stocks:
        stock.update()
        output += '\n' + str(stock)
    output += '\n'

    os.system('cls')
    print(output)