import sys
import time as time
from twython import Twython
from random import randint

CONSUMER_KEY = 'HURRYA'
COMSUMER_SECRET = 'MY SECRET'
ACCESS_KEY = 'BLA BLA BLA'
ACCESS_SECRET = 'JMORE NLA'

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
       
   
