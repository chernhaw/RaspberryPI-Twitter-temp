import time
import serial
import RPi.GPIO as GPIO
from twython import TwythonStreamer
from twython import Twython
from datetime import datetime
from random import randint

# Search terms
TERMS = '#On_'

# GPIO pin number of LED
LED = 22

# Twitter application authentication
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

api = Twython (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# Setup callbacks from Twython Streamer

# Setup serial connection
ser = serial.Serial('/dev/ttyACM0',9600)

class BlinkyStreamer(TwythonStreamer):
        
    
        def on_success(self, data):
                if 'text' in data:
                        message = data['text'].encode('utf-8')
                        #print data['text'].encode('utf-8')
                        print ( message)
                       # GPIO.output(LED, GPIO.HIGH)
                        #time.sleep(0.5)
                       # GPIO.output(LED, GPIO.LOW)
                        sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S -')
                        print (sttime )
                        print ("Twitter message received : %s " %message)
                        #Convert byte to string

                       
                        
                        messageStr= str(message, 'utf-8')
                      #  sttimeStr= str(sttime, 'utf-8')
                        f= open('blink_tweets.txt', 'a') 
                     #   f.writeline( messageStr+"\n")
                        f.write( sttime+" "+ messageStr+"\n")
                        f.close()
                        
                     #   print (messageStr)
                        time.sleep(5) # to prevent crash ?? by putting 5s delay
                                

                        if "hot_" in messageStr:
                            #  blinkLED ()
                            GPIO.output(LED, GPIO.HIGH)
                            time.sleep(0.5)
                            GPIO.output(LED, GPIO.LOW)
                            
                            #read current temp
                            time.sleep(1.5)   #Delay to prevent error connecting to Arduino
                            read_serial=ser.readline()
                            read_serial1=ser.readline()
                            read_serial_all = read_serial + read_serial1
                            read_serial_str = read_serial_all.decode("utf-8")
                            # send message
                            print (read_serial_str)
                            api.update_status(status=str(randint(0,1000))+ " \n" +read_serial_str)
                            
         
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)


# Create streamer
try:
        print("Twitter message receiver started" )
        
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS) 
except KeyboardInterrupt:
        GPIO.cleanup()

