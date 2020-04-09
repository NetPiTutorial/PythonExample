
#import serial

#ser = serial.Serial ( port = '/dev/ttyACM0',         \
#                      baudrate =  9600,              \
#                      bytesize = serial.EIGHTBITS,   \
#                      parity = serial.PARITY_NONE,   \
#                      stopbits = serial.STOPBITS_ONE )

#Out = raw_input("Hier Nachricht eingeben: ")
#Out = Out + "\n"
#Out = bytes(Out)
#ser.write(Out)

#In = ""
#while True:
#    if ser.in_waiting:
#        symbol = ser.read(1)

#        if symbol != "\n":
#            In += symbol
#        else:
#            print(In)
#            break

while True:
  print("Hello World")


