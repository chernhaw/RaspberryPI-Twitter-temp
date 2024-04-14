import json
import os
import time as time
import pyrebase
from collections import OrderedDict, deque

from pyrebase import pyrebase

config = {
  "apiKey": "c0",
  "authDomain": "myroomtemp-c7758.firebaseapp.com",
  "databaseURL": "https://myroomtemp-c7758.firebaseio.com/",
  "storageBucket": "myroomtemp-c7758.appspot.com",
  "serviceAccount": "/c75.json"
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
        db.child('sensor/current').update(data)
        datastr=str(localtime)+"T"+temperature+"H"+humidity
        update_recent(datastr)

def update_recent(data):
        
        
        fixed_length=6048+168 # 1 week data : 24x4 =168
        response =""
        recent_data=""
        try:
            response=db.child('sensor/recent').get()
            
            if len(response.val())==0:
                recent_data=data
            else:
                recent_data=response.val()+"|"+data
            
        except:
            response=""
        
 
        
        if len(recent_data) > fixed_length:
            recent_data=recent_data[37:]
        
        db.child('sensor/recent').set(recent_data)
          
        
update_firebase()
 
