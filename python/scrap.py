import serial
ser = serial.Serial('COM5', 9600, timeout=0)
while 1:
    
    # var = raw_input("Enter 0 or 1 to control led: ")
 fh = open("C:\Program Files (x86)\EasyPHP-Webserver-14.1b2\www\newfile.txt", "w")

 s = fh.read()

 x=int(s)


 fh.close()

 ser.write(var)
    
    
    
