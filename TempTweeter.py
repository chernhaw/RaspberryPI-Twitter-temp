import sys
import time as time
from twython import Twython
from random import randint

CONSUMER_KEY = 'RNdkBc0t6l4KLCUoxlQ7pF9ZQ'
COMSUMER_SECRET = 'tJaMNfu5Kr1rKvMnJqqjOvG5r0nJkQDNHlKk9CCkwJrq4MZFTH'
ACCESS_KEY = '803222273540833280-WERQinEzdj60dxawryZN6xtyLEAgS6G'
ACCESS_SECRET = 'JpQe4YrcF7nzNHI3MTuyogbEXAoOs208dpfn9WyWKJkbS'

api = Twython (CONSUMER_KEY,COMSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)


file=open('templog.txt','r')
logfile=open('tweetlog.txt','a')
    
for line in file:
        
 
        localtime = time.asctime(time.localtime(time.time()))
   
        api.update_status(status=str(localtime +" "+ line))
        logfile.write(str(localtime +" "+ line))
logfile.close()
file.close()
    #Write what is being
       
   