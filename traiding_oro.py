import pandas_datareader.data as web
import datetime as dt
import mplfinance as mpf

#Desde aaaa/mm/dd
start = dt.datetime(2015,2,26)
#Hasta
end = dt.datetime(2021,12,26)


df = web.DataReader('GLD', 'yahoo', start, end)


df['ma'] = df['Close'].rolling(window=10, min_periods=0).mean()

mc = mpf.make_marketcolors(up='tab:green', down='tab:red', wick={'up':'green', 'down':'red'})

s = mpf.make_mpf_style(base_mpl_style="seaborn", mavcolors=["orange"], marketcolors=mc)
mpf.plot(df, type='candle', style= s,mav=10,title='GLD')