import minimalmodbus

class D113003PowerMeter(minimalmodbus.Instrument):
    
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
        self.serial.baudrate = 9600
    def get_energy(self):
        """Return the process value (PV) for loop1."""
        return self.read_long(7)
    
    
pm = D113003PowerMeter('/dev/ttyUSB0', 1)
print(pm.get_energy())