import json
import os
import time as time
import pyrebase

from pyrebase import pyrebase

config = {
  "apiKey": "db70f6e1c18866084d099385ec170d9f5f2db660",
  "authDomain": "myroomtemp-c7758.firebaseapp.com",
  "databaseURL": "https://myroomtemp-c7758.firebaseio.com/",
  "storageBucket": "myroomtemp-c7758.appspot.com",
  "serviceAccount": "/home/pi/Desktop/TweetTemp/myroomtemp-c7758-firebase-adminsdk-1f4dx-4f4f7b0175.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


def update_firebase():
    file=open('templog.txt','r')
    for line in file:
        line = line.strip()
        humidity = line[9:14]
     #   print (line)
        
        temperature = line[26:30] 
        localtime = time.asctime(time.localtime(time.time()))
        
        data = {"date":localtime, "temp":temperature, "humidity":humidity}
        db.child('sensor/dht').push(data)

update_firebase()
 
