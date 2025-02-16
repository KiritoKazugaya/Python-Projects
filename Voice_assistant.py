import pyttsx3 #converts speech
import speech_recognition as sr #recognizes speech
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio,language='en-in')
            print(data)
        except sr.UnknownValueError:
            print("Could not understand audio")
sptext()