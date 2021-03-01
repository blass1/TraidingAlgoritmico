import pandas_datareader.data as web
import datetime as dt
from numpy import where

#Desde aaaa/mm/dd
start = dt.datetime(2017,2,26)
#Hasta
end = dt.datetime(2021,2,26)

"""
Creamos un dataframe con pandas y utilizando DataReader 
A esta funcion se le pueden pasar muchas variables, pero tiene 4 indisponsables
Probamos bajando la accion de apple, tenemos que buscar el identificador. Buscar "ticket apple"
Descarga data de diferentes splataformas, en este caso yahoo finanzas

"""
df = web.DataReader('AMZN', 'yahoo', start, end)

"""
Rolling le decimos que a pesar de querer una media(mean),
A cada muestra de las 42 muestras (1 muestra de precio x dia)
El mercado esta abierto solo los dias habiles por eso 21 dias tienen los dias habiles del mes
"""
# Media movil corta de 42 dias "ma" en ingles 
df['42ma'] = df['Close'].rolling(window=42, min_periods=0).mean()
# Media movil larga de 252 (252 dias habiles osea 1 ano)
df['252ma'] = df['Close'].rolling(window=252, min_periods=0).mean()
# Difedrencia de los valores entre la media movil corta y la larga
df['diferencia'] = df['42ma'] - df['252ma']
# Regime almacena la senial de compra / venta
# Where almacena 3 paramentros, la condicion, que valor toma el elemento de esta columna cuando se cumple
# y el 3er es el valor que va a tomar ese elemtno cuando no se cumpla esta condicion 
# Aca compramos acciones
df['Regime'] = where(df['diferencia']>0,1,0)
# Cuando el valor de la media movil larga este por encima del valor de la media mivol corta
# queremos que nuestro programa mande senial de venta
# 1 senial de compra, -1 es senial de venta, 0 totalmente fuera del mercado
df['Regime'] = where(df['diferencia']<0,-1,df['Regime'])

#df[['Close', '42ma', '252ma']].plot(grid=True)

# Ponemos a prueba esta estrategia, medimos los incrementos relativos
# El precio del dia actual entre el dia del precio del dia anterior
# El resultado superior a 1 nos indica incremento del precio
# 2 qeurrria decir que se duplico y 0.5 es que se redujo a la mitad
# Incrtementos relativos de precio de un dia para otro
df['Market'] = df['Close']/df['Close'].shift(1)
# Nuestro benefio o perdida de un dia para otro de nuestra estrategia
df['Strategy'] = df['Market']**df['Regime'].shift(1)
# Representamos la evolucion de cada una de estas columnas
# Esto lo logramos haciendo un producto acumulativo
df[['Market', 'Strategy']].cumprod().plot(grid=True)
