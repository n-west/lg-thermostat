
import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=100,
        bytesize=8, stopbits=1, timeout=1.5)
print ser.timeout

for x in xrange(20):
    dump_file = "msg%i.hex" % x
    with open(dump_file, "wb") as f:
        c = ser.read()
        while len(c) == 0:
            c = ser.read()
        f.write(c)
        while len(c) > 0:
            c = ser.read()
            f.write(c)


