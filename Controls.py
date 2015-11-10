# -*- coding: utf-8 -*-
from HeaterControlTools import printCurrentTime

class BangBang(object):
    """DOKUMENTATION
    
    """

    def __init__(self, setpoint, zone):
        """Return a Relay object whose name is *name* and starting
        state is TRUE (ON)"""
        self.setpoint = setpoint
        self.neutralZone = zone


    def control(self, output, temp):
        if temp > self.setpoint+self.neutralZone and output.state:
            output.disable()
            print(printCurrentTime()+"Raditoren slukkes ! - Fra Class \o/")
    
        if temp < self.setpoint-self.neutralZone and not(output.state):
            output.enable()
            print(printCurrentTime()+"Radiatoren tændes ! - Fra Class \o/")
        
        


    def disable(self):
        self.state = False
        return self.state