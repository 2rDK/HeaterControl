# -*- coding: utf-8 -*-
import time
import random
from Relay import Relay
from Controls import BangBang
from threading import Timer
import threading
import requests
from HTU21D import HTU21D
from mySqlTools import mySqlSenderAnalog
from HeaterControlTools import printCurrentTime

print(printCurrentTime()+"Imports complete")

setpoint = 16
zone = 0.2
radiator = Relay(12)
rumsensor = HTU21D()
controller = BangBang(setpoint, zone)
temp = round(rumsensor.read_temperature(),2)
print(printCurrentTime()+"Setup complete")

temp = 0

def controlLoop():
    ct=Timer(15.0, controlLoop)
    #t.daemon = True
    ct.start()
    print(printCurrentTime()+"Regulering aktiv !")
    #print(time.clock())
    controller.control(radiator, temp)
    
def logLoop():
    lt=Timer(60.0, logLoop)
    #t.daemon = True
    lt.start()
    print(printCurrentTime()+"Starter logning...")
    myKeys = {
        'Vrk_temp': round(rumsensor.read_temperature(),2),
        'Vrk_hum': round(rumsensor.read_humidity(),2)
        }
    
    mySqlSenderAnalog(myKeys,1)
    
    print(printCurrentTime()+"Logning komplet !")
    
    
    
    
""" Starting the control loop """
controlLoop()
"""Starting the logging loop """
logLoop()

while True:
    
    try:
        temp = rumsensor.read_temperature()
    except OSError as err:
        print("OS error: {0}".format(err))
        
    print(round(temp,2))
    temp_adress = "http://localhost:8888/writetemp/"+str(round(temp,2))
    try:
        rqs = requests.get(temp_adress)
    except requests.exceptions.RequestException as e:    
        print(e)
        print("GUI lader til at være offline, check Tornado !")
       
    time.sleep(1)
#GUIThread()