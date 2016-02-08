import minimalmodbus
import time

class D113003PowerMeter(minimalmodbus.Instrument):
    
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
        self.serial.baudrate = 9600
        minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
    def get_energy(self):
        """Return the accumulated active energy in Watt-hours"""
        return self.read_long(7)
    
    def get_supplyVoltage(self):
        """Return the supply voltage in Volts"""
        return self.read_register(0,1)
    
    def get_current(self):
        """Return the current drawn in Amps"""
        return self.read_register(1,1)
    
    def get_supplyFrequency(self):
        """Return the supply frequency in Hertz"""
        return self.read_register(2,1)
    
    
pm = D113003PowerMeter('/dev/ttyUSB0', 1)
while True:
    try:
        print("Energy: "+str(pm.get_energy()))
        print("Voltage: "+str(pm.get_supplyVoltage()))
        print("Frequency: "+str(pm.get_supplyFrequency()))
    except IOError:
        print("Failed to read from instrument")
    time.sleep(2)