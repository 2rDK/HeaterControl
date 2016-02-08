import minimalmodbus

class D113003PowerMeter(minimalmodbus.Instrument):
    
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
        self.serial.baudrate = 9600
    def get_energy(self):
        """Return the accumulated active energy in Watt-hours"""
        return self.read_long(7)
    
    def get_supplyVoltage(self):
        """Return the supply voltage in Volts"""
        return self.read_register(0,1)
    
    def get_current(self):
        """Return the current drawn in Amps"""
        return self.read_register(0,1)
    
    def get_supplyFrequency(self):
        """Return the supply frequency in Hertz"""
        return self.read_register(0,1)
    
    
pm = D113003PowerMeter('/dev/ttyUSB0', 1)
print("Energy: "+pm.get_energy())
print("Voltage: "+pm.get_supplyVoltage())
print("Frequency: "+pm.get_supplyFrequency())