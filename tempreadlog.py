import serial
import time as time

ser =serial.Serial('/dev/ttyUSB0',9600)
i=0
while i < 8:
    line1= ser.readline()
    i=i+1 


print (line1)
target=open('templog.txt','wb')
target.write(line1)
target.close()
    
    






