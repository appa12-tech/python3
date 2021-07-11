import pyttsx3
import datetime
enengine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("This is Sunday")
