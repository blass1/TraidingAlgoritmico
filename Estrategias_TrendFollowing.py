"""
Esta estrategia trata de seguir la direccion de la tendencia y posicionarlos 
a favor de ella.

Historia de las torutugas que es un experimento de traders.
https://www.investopedia.com/articles/trading/08/turtle-trading.asp

Reglas del sistema: En cuanto haya una vela con un high sea el mayor de los 
ultimos 10 dias es una se;al de compra.
Y cuando haya una vela cuyo low sea el menor de los ultimos 10 dias es una 
senal de venta.

Los puntos de entrada al mercado de esta estrategia que son el maximo high
y el minimo low de los ultimos dias son pun tos de entrada muy populares para
los traders, lo que susede es que tantos traders emitiendo operaciones en el mercado
conlleva un deslizamiento importante (diferencia del precio) que queriamos
comprar o vender con respecto al precio. Puede repectur de manera negativa en el
rendimiento de la estrategia
"""

from pandas_datareader.data import DataReader
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

#Desde / hasta (aaaa/mm/dd)
start = dt.datetime(2020,3,3)
end = dt.datetime(2021,3,3)
# Par Dolar estadounidense frente al franco suizo 
# El identificador FOREX de yahoo es : USDCHF=X
df = DataReader('MELI', 'yahoo', start, end)

# Este parametro del sistema despues cuando se haga la "Evaluacion del sistema"
# pondremos los valores optimos de este parametro
window = 10
# Creamos la columna que almacena el maximo y minimo de las muestras
df['highest high'] = df['High'].rolling(window=window).max()
df['lowest low'] = df['High'].rolling(window=window).min()

# SENANES DE TRAIDING
df['trigger'] = np.where(df['High']==df['highest high'],1,np.nan)
df['trigger'] = np.where(df['Low']==df['lowest low'],-1,df['trigger'])

"""En la columna Trigger su justo hubo un high o low va a aparecer 1 o -1
Y nan intermedios entre las senales de traiding.
ffill() Rellena el mismo valor de la anterior senal que no es un "nan".
fullna(0) reemplaza los "nans" del principio por cero (osea fuera del mercado)
"""
df['position'] = df['trigger'].ffill().fillna(0)

# Rendimiento de nuestra estrategia frente a la evolucion del precio
df['returns'] = df['Adj Close']/df['Adj Close'].shift(1)
df['strategy'] = df['returns'] ** df['position'].shift(1)

# Imprimimos el grafico y mostramos ambos en el mismo
plt.style.use('seaborn')
df[['returns', 'strategy']].dropna().cumprod().plot(figsize=(10,6))