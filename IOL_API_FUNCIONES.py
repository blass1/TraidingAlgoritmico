#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json
import pandas
import time
from datetime import datetime
import os


# In[4]:


url = "https://api.invertironline.com/token"

username = os.environ.get('IOL_USER')
password = os.environ.get('IOL_PASS')

data = {
    "username":username,
    "password":password,
    "grant_type":"password"
}

def bearer_tokken():
    return json.loads(requests.post(url,data=data).text)["access_token"]


# In[5]:


bearer_tokken()


# In[ ]:


# El plazo t0 es inmediato, t1 24 horas, t2 48 horas

def vender(simbolo,precio,cantidad):
    url = "https://api.invertironline.com/api/v2/operar/Vender"
    headers = {"Authorization":"Bearer "+ bearer_tokken()}
    data = {
        "mercado":"bCBA",
        "simbolo":simbolo,
        "cantidad":cantidad,
        "precio":precio,
        "validez":"2019-04-30",
        "plazo":"t1"
    }
    return requests.post(url=url, headers=headers, data=data).text

def comprar(simbolo,precio,cantidad):
    url = "https://api.invertironline.com/api/v2/operar/Comprar"
    headers = {"Authorization":"Bearer "+ bearer_tokken()}
    data = {
        "mercado":"bCBA",
        "simbolo":simbolo,
        "cantidad":cantidad,
        "precio":precio,
        "validez":"2019-04-30",
        "plazo":"t1"
    }
    return requests.post(url=url, headers=headers, data=data).text

