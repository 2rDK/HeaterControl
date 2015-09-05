class Relay(object):
    """DOKUMENTATION

    
    """

    def __init__(self, pin):
        """Return a Relay object whose name is *name* and starting
        state is TRUE (ON)"""
        self.pin = pin
        self.state = False


    def enable(self):
        self.state = True
        return self.state

    def disable(self):
        self.state = False
        return self.state