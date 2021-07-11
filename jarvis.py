import pyttsx3
import datetime
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate=190
engine.setProperty('rate',newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
#time()
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("Today is ")
    speak(date)
    speak(month)
    speak(year)
#date()
def wishme():
    speak("Welcome back sir")
    speak("Time is ")

    time()
    date()
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <=12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    elif hour >=18 and hour <=24:
        speak("Good Evening")
    else:
        speak("Good Night")
wishme()
