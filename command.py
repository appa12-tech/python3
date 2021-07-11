import pyttsx3
import pyaudio
import speech_recognition as sr
engine = pyttsx3.init()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Re")
        query = r.recognize_google(audio,'en=US')
        print(query)
    except Exception as e:
        print(e)
        engine.pyttsx3("Say that again please...")
        engine.runAndWait()
        return "None"
    return query
takecommand()
