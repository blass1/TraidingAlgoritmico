#!/usr/bin/env python
# coding: utf-8

# In[12]:


import json
import requests
import os


# In[65]:


url = "https://api.invertironline.com/token"

username = os.environ.get('IOL_USER')
password = os.environ.get('IOL_PASS')

data = {
    "username":username,
    "password":password,
    "grant_type":"password"
}


# In[66]:


r = requests.post(url=url, data=data)
print(r)
acceso = json.loads(r.text)
print(acceso)


# ### Con este token estamos online, en 15 minutos vence y tenemos que usar el refresh_token

# In[67]:


acceso


# ### Variables con las llaves del acceso

# In[68]:


bearer_token = acceso['access_token']
refresh_token = acceso['refresh_token']


# In[69]:


bearer_token


# ### Mostramos las opciones de un titulo

# In[70]:


mercado = "bCBA"
simbolo = "PAMP"

url = f"https://api.invertironline.com/api/v2/{mercado}/Titulos/{simbolo}/Opciones"
headers = {
    "Authorization":"Bearer "+bearer_token
}

opciones = requests.get(url=url, headers=headers)

op_pamp = json.loads(opciones.text)


# In[71]:


op_pamp


# In[72]:


pais = "argentina"

url = f"https://api.invertironline.com/api/v2/portafolio/{pais}"
headers = {
    "Authorization":"Bearer "+bearer_token
}

portafolio = requests.get(url=url, headers=headers)

portafolio = json.loads(portafolio.text)
portafolio


# In[74]:


op = "Vender"

url = f"https://api.invertironline.com/api/v2/operar/{op}"
headers = {
    "Authorization":"Bearer "+bearer_token
}

cantidad = "0"
precio = "0.5"
plazo = "t0"
validez = "2020-04-20"

data = {"mercado": mercado,
        "simbolo": simbolo,
        "cantidad": cantidad,
        "precio": precio,
        "plazo": plazo,
        "validez": validez
       }

vender = requests.post(url=url, headers=headers, data=data)
vender.text


# In[1]:





# In[ ]:




