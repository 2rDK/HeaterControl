# -*- coding: utf-8 -*-
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
            print("Raditoren slukkes ! - Fra Class \o/")
    
        if temp < self.setpoint-self.neutralZone and not(output.state):
            output.enable()
            print("Radiatoren tændes ! - Fra Class \o/")
        
        


    def disable(self):
        self.state = False
        return self.state