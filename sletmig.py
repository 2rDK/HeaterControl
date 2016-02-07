# -*- coding: utf-8 -*-
import requests
test = "http://localhost:8888/writetemp/"
try:
    rqs = requests.get(test)
except requests.exceptions.RequestException as e:    
    print(e)
    print("GUI lader til at være offline, check Tornado !")



