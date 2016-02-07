import minimalmodbus
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600

Vs = instrument.read_register(0,1)
Fs = instrument.read_register(2,1)

print("Supply voltage: "+str(Vs)+" Volt")
print("Supply frequency: "+str(Fs)+" Hz")
print("\o/ yay !!")