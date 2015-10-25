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


setpoint = 15
zone = 0.2
radiator = Relay(12)
rumsensor = HTU21D()
controller = BangBang(setpoint, zone)


temp = 20

def controlLoop():
    ct=Timer(15.0, controlLoop)
    #t.daemon = True
    ct.start()
    print("Regulering aktiv !")
    #print(time.clock())
    controller.control(radiator, temp)
    
def logLoop():
    lt=Timer(60.0, logLoop)
    #t.daemon = True
    lt.start()
    print("Starter logning...")
    myKeys = {
        'Vrk_temp': round(rumsensor.read_temperature(),2),
        'Vrk_hum': round(rumsensor.read_humidity(),2)
        }
    
    mySqlSenderAnalog(myKeys,1)
    
    print("Logning komplet !")
    
    
    
    
""" Starting the control loop """
controlLoop()
"""Starting the logging loop """
logLoop()

while True:
    temp = rumsensor.read_temperature()
    #if radiator.state:
    #    temp = temp + random.uniform(0, 0.1)
    #else:
    #    temp = temp - random.uniform(0, 0.05)
        
    print(round(temp,2))
    test = "http://localhost:8888/writetemp/"+str(round(temp,2))
    rqs = requests.get(test)
    if rqs.status_code != 200:
        print("Problemer med at sende opdatering til GUI (Tjek tornado)")
       
    time.sleep(1)
#GUIThread()