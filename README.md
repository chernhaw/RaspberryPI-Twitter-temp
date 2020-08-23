# RaspberryPI-Twitter-temp
Raspberry Pi connected to Arduino DHT11 

DHT11 is connected to Arduino running the DHT11_reading.ino file.
Arduino is connected to Raspberry PI via USB
Python script ReadNTweetTemp1.py to receive and send temperature and humidity data on Twitter.

Deployed code **@23 Aug 2020**

1. TempTwetter.py - tweet message
2. tempreadlog.py - read message from text file written by DHT11_reading.ino.ino file
3. DHT11_reading.ino


2020-Aug-15 Replaced sensor **back to DHT11 for more reliable reading, TMP35 sensor gives unaccurate reading, strange values of 40 deg**

2020-AUG-22 Added temp-firebase.py script to update to Firebase realtime db resolved 
https://github.com/chernhaw/RaspberryPI-Twitter-temp/issues/1 by
"serviceAccount": "/home/pi/Desktop/TweetTemp/myroomtemp-c7758-firebase-adminsdk-1f4dx-4f4f7b0175.json" 

