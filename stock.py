from yahoo_fin import stock_info as si

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.day_open = round(si.get_quote_table(ticker)['Open'], 3)
        self.cur_price = round(si.get_live_price(ticker), 3)
        self.day_change = round(self.day_open - self.cur_price, 3)
        self.percent_change = self.day_change / self.day_open
    
    def update(self):
        self.cur_price = si.get_live_price(self.ticker)
        self.day_change = round(self.day_open - self.cur_price, 3)
        self.percent_change = 100 * self.day_change / self.day_open
    
    def __str__(self):
        day_open = '{0:.3f}'.format(self.day_open)
        cur_price = '{0:.3f}'.format(self.cur_price)
        day_change = '{0:.3f}'.format(self.day_change)
        percent_change = '{0:.3f}'.format(self.percent_change)

        return '{0:>10}{1:>15}{2:>15}{3:>15}{4:>15}'.format(self.ticker, day_open, cur_price, day_change, percent_change)