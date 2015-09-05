# -*- coding: utf-8 -*-
import time
import random
from Relay import Relay
from Controls import BangBang
from threading import Timer

setpoint = 22
zone = 0.2
radiator = Relay(1)
controller = BangBang(setpoint, zone)


temp = 20

def controlLoop():
    t=Timer(15.0, controlLoop)
    #t.daemon = True
    t.start()
    print("Regulering aktiv !")
    print(time.clock())
    controller.control(radiator, temp)

controlLoop()


while True:
    if radiator.state:
        temp = temp + random.uniform(0, 0.1)
    else:
        temp = temp - random.uniform(0, 0.05)
        
    print(round(temp,2))
    

       
    time.sleep(1)