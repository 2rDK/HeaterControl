import minimalmodbus
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600

Vs = instrument.read_register(0,1)
A = instrument.read_register(1,1)
Fs = instrument.read_register(2,1)
P = instrument.read_register(6,1)
E = instrument.read_register(7,1)

print("Supply voltage: "+str(Vs)+" Volt")
print("Supply frequency: "+str(Fs)+" Hz")
print("Current: "+str(A)+" Amp")
print("Power: "+str(P)+" kW")
print("Energy: "+str(E)+" kWh")
print("\o/ yay !!")