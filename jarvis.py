import pyttsx3   #pip install pyttsx3
import datetime  #pip install datetime
import speech_recognition as sr #pip install SpeechRecognition
import pyaudio  #first insatall pipwin by pip install pipwin and pipwin install pyaudio
import wikipedia #pip install wikipedia
import smtplib #pip install smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate=190
engine.setProperty('rate',newVoiceRate)
def speak(audio): #for audio
    engine.say(audio)
    engine.runAndWait()
def time(): #function for Time
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
#time()
def date():#function for date
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("Today is ")
    speak(date)
    speak(month)
    speak(year)
#date()
def wishme(): #function for wishme
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
    speak("Kanchi at your service sir and madam ")
#wishme()
def takecomand(): #funtion for take command from user
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
def sendmail(to,context): #function to send a Email
    server = smtplib.SMTP('smtp.gmail.com'),587
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","123test")
    server.sendmail("test@gmail.com",to,context)
    server.close()

def screenshot(): #function to screenshot
    img=pyautogui.screenshot()
    img.save(r'C:\Users\17bcs\Videos\ss.png')

def cpu(): #function for cpu and battery
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+usage)

    battery = psutil.sensors_battery
    speak("battery is at")
    speak(battery.percent )
def jokes(): #function to crack a jokes
    speak(pyjokes.get_jokes())
if __name__ =="__main__": #main funtion
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
        elif "play songs" in query:
            songs_dir ="E:\songs"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember that" in query:
            speak("What should i Remmber")
            data = takecomand()
            speak("you said me to remember" + data)
            remember= open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know something" in query:
            remember= open("data.txt","r")
            speak("you said me to remember that "+ remember.read())
        elif"take a picture" in query:
            screenshot()
            speak("Done")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
