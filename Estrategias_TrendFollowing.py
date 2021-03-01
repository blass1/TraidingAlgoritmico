# -*- coding: utf-8 -*-
"""
Esta estrategia trata de seguir la direccion de la tendencia y posicionarlos 
a favor de ella.

Historia de las torutugas que es un experimento de traders.
https://www.investopedia.com/articles/trading/08/turtle-trading.asp

Reglas del sistema: En cuanto haya una vela con un high sea el mayor de los 
ultimos 10 dias es una se;al de compra.
Y cuando haya una vela cuyo low sea el menor de los ultimos 10 dias es una 
senal de venta.
"""

from pandas_datareader.data import DataReader
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

#Desde / hasta (aaaa/mm/dd)
start = dt.datetime(2000,2,28)
end = dt.datetime(2021,2,28)
# Par Dolar estadounidense frente al franco suizo 
# El identificador FOREX de yahoo es : USDCHF=X
df = DataReader('USDCHF=X', 'yahoo', start, end)

# Este parametro del sistema despues cuando se haga la "Evaluacion del sistema"
# pondremos los valores optimos de este parametro
window = 10
# Creamos la columna que almacena el maximo y minimo de las muestras
df['Highest high'] = df['High'].rolling(window=window).max()
df['Lowest low'] = df['High'].rolling(window=window).min()

# SE;ANES DE TRAIDING
df['trigger'] = np.where(df['High']==df['Highest high'],1,np.nan)
df['trigger'] = np.where(df['Low']==df['Lowest low'],-1,df['trigger'])