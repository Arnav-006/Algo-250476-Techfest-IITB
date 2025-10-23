from tvDatafeed import TvDatafeed, Interval
import pandas as pd

username = 'arnavb006'
password = 'Arnav@TradingView7'

tv = TvDatafeed(username, password)

tcs_data = tv.get_hist(symbol='TCS',exchange='NSE',interval=Interval.in_1_hour,n_bars=1000)
print(tcs_data.head())
print(tcs_data.tail())