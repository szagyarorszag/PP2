import datetime as dt
from config import some_math

Aigera_s_birthday = dt.datetime(2005,5,7) 

now = dt.datetime.now()

datetime_age = now - Aigera_s_birthday

if some_math(datetime_age) == 18 : 
    print("I wish you to be what you want to be ! \n"
          "And of course first of all be happy and healthy \n" 
          "Then be rich(if you will become rich call me , actually you knew my phone ;) ) \n" 
          "Always be motivated i knew you can do a lot of things and smile :) ")






