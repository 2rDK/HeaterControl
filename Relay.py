import RPi.GPIO as GPIO
from mySqlTools import mySqlSenderDigital

GPIO.setmode(GPIO.BOARD)



class Relay(object):
    """DOKUMENTATION
    
    """

    def __init__(self, pin):
        """Return a Relay object whose name is *name* and starting
        state is TRUE (ON)"""
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.state = False
        GPIO.output(pin,  not self.state)

    def enable(self):
        self.state = True
        GPIO.output(self.pin, not self.state)
        myKeys = {
                  'Vrk_radiator': self.state
                  }
        mySqlSenderDigital(myKeys)
        return self.state

    def disable(self):
        self.state = False
        GPIO.output(self.pin, not self.state)
        myKeys = {
                  'Vrk_radiator': self.state
                  }
        mySqlSenderDigital(myKeys)
        return self.state