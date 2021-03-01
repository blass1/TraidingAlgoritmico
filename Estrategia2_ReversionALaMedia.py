# -*- coding: utf-8 -*-
"""
1ERA PARTE
Indicadores y reglas de la ESTRATEGIA para Crear y evaluar un sistema de traiding
El precio de un instrumento financiero puede evolucionar bajo 2 regimenes distintos
Uno TENDENCIAL y otro CICLICO .Existen 2 estrategias que usan los traders "Trend folowin" para regimes TENDECIALES 
y "Reversion a la media" para regimenes CICLICOS.
No es facil cinbinarlas ya que siguen una logicas contrarias
Trend folowin se basa en posicionarse enfavor de de la direccion reciente del precio
En reversion a la media se da por hecho que el precio deve volver a un valor intermedio,
por lo que vamos a posicionarnos en la direccion opuesta.
Analizar que tipo de estrategia conviene usar para cada instrumento financiero en partiocular
Este instrumento financiero (El oro) historicamente funciona la estrategia de reversion a la media
Cuando el instrumento se situe en una cierta distancia del valor medio de los ultimos dias
lo tomaremos como una se;al de venta y de compra en el caso opuesto (Cuando el precio este por 
debajo de la media de los ultiumos dias)
Hay que decidir 2 cosas, de cuantos dias queremos hacer la media
y de cuanta distancia estamos hablando (arbitrario como parametros dle sistema)
En la 4ta parte de la serie (evaluacion del sistema de trading) las arbitrariedades
desaparecen ya que trataremos los mejores parametros de entrada para optimizar el sistema
"""
from pandas_datareader.data import DataReader
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

#Desde / hasta (aaaa/mm/dd)
start = dt.datetime(2000,2,28)
end = dt.datetime(2021,2,28)
# Oro en acciones de yahoo
data = DataReader('GDX', 'yahoo', start, end)
data['price'] = data['Adj Close']

# Media movil en dias
SMA = 25
data['SMA'] = data['price'].rolling(window=SMA).mean()

# Numero de desviaciones estandar que le estamos exigiendo al sistema
N = 1
# Valor de distancia del precio respecto de la media movil sea 
# la de la "desviacion de estandar" del precio de los ultimos dias
data['STD'] = N*data['price'].rolling(window=SMA).std()

# Valores de la media movil + y - la desviacion estandar
data['SMA+STD'] = data['SMA'] + data['STD']
data['SMA-STD'] = data['SMA'] - data['STD']
plt.style.use('seaborn')
data[['price', 'SMA+STD', 'SMA-STD']].plot(figsize=(10,6))

data['position'] = np.where(data['price'] > data['SMA+STD'], -1, 0)
data['position'] = np.where(data['price'] < data['SMA-STD'], 1, data['position'])
data['position'] = data['position'].fillna(0)

data['returns'] = data['price']/data['price'].shift(1)
data['strategy'] = data['returns'] ** data['position'].shift(1)
data[['returns', 'strategy']].dropna().cumprod().plot(figsize=(10,6))







