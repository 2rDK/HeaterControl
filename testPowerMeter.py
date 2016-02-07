import minimalmodbus
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600

Vs = instrument.read_register(0,1)
A = instrument.read_register(1,1)
Fs = instrument.read_register(2,1)
Pf = instrument.read_register(6,1)
E = instrument.read_register(7,1)
Ti = instrument.read_register(25,1)

print("Supply voltage: "+str(Vs)+" Volt")
print("Supply frequency: "+str(Fs)+" Hz")
print("Current: "+str(A)+" Amp")
print("Power factor: "+str(Pf))
print("Energy: "+str(E)+" kWh")
print("Temp: "+str(Ti)+" C")
print("\o/ yay !!")