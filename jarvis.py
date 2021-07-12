import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb
import os
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
    #speak("Time is ")

    #time()
    #date()
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <=12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    elif hour >=18 and hour <=24:
        speak("Good Evening")
    else:
        speak("Good Night")
#wishme()
def takecomand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Re")
        query = r.recognize_google(audio,language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
#takecomand()
def sendmail(to,context):
    server = smtplib.SMTP('smtp.gmail.com'),587
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","123test")
    server.sendmail("test@gmail.com",to,context)
    server.close()
if __name__ =="__main__":
    wishme()
    while True:
        query = takecomand().lower()
        print(query)
        if "time" in query :
            time()
        elif "date" in query :
            date()
        elif "offline" in query :
            quit()
        elif "wikipedia" in query :
            speak("Searching.......")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speak(result)
        elif "send email" in query :
            try:
                speak("What should I say")
                context = takecomand()
                to ="17bcs3287.cu@gmail.com"
                sendmail(to,context)
                speak("Email send sucessfully")
                #speak(context)
            except Exception as e:
                speak(e)
                speak("Unale to send the message")
        elif "search in chrome" in query:
            speak("What should i search")
            chromepath ="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe%s"
            search= takecomand().lower()
            wb.get(chromepath).open_new_tab(search +".com")
        elif "logout" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
