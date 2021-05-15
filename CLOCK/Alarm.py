import time,pyttsx3                # ppttsx3 python text to speech lib offline
from datetime import datetime      # date and time as human read lib

print("ALARM")                                              
Because = input("You need the alarm to say: ")           # getting purpose of the alarm
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is: ", current_time)                    # giving reference of current time

Time=input("You need to be alarmed at(HH24:MM): ")          # set alarm time in Time 


while True:                                                 # starting the loop
    Time_Now=datetime.now().strftime("%H:%M")               # storing time right now in Trn with datetime module
    time.sleep(1)                                           # sleep the program for about 1 sec
    if Time==Time_Now:                                      # checking if it's time for alarm
        count=0
        while count<=2:                                     # speak thrice
            count=count+1
            engine=pyttsx3.init()                           # creating a engine for voice mode
            engine.say("Wake up"+Because)                   # setting the voice
            engine.runAndWait()
        print("Hope You Were Alarmed Well! :)")
        break
