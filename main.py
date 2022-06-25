import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ma'am")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon ma'am")

    else:
        speak("Good evening ma'am")

    speak("G.I. Jane, reporting to duty ma'am! Awaiting further instructions!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ma'am.....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source,duration=0.5)
        audio = r.listen(source)
        print("Recognizing...")  
        
    try:  
        query = r.recognize_google(audio, language='en-in') 
        print(f"Command recieved: {query}\n")
        
    except Exception as e:
        speak("Command unclear, please repeat!!")
        print("Command unclear, please repeat!!")
        return "None"

    return query


if __name__ == '__main__' :
    wishMe() 
    while True :
        query = takeCommand().lower()
        speak("Roger that!!")

        if 'open folder' in query:
            os.startfile('C:\\New folder')

        elif 'open word' in query:
            os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD')

        elif 'open whatsapp' in query:
            os.startfile('C:\\Users\\sharm\\AppData\\Local\\WhatsApp\\WhatsApp')

        elif 'open meet' in query:
            webbrowser.open("https://meet.google.com/")

        elif 'open youtube' in query :
            webbrowser.open("https://www.youtube.com")

        elif 'open stack overflow' in query :
            webbrowser.open("https://www.stackoverflow.com")

        elif 'play english songs' in query:
            music_dir = 'C:\\New folder\\New folder\\Playlists'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play music' in query :
            music_dir = 'C:\\New folder\\New folder\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}")
        
        elif 'open google' in query :
            webbrowser.open("https://www.google.com")

        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/h")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

        elif 'over' in query:
            speak("Over and out ma'am")
            sys.exit()

        else:
            speak("Command unclear, please repeat!!")


        time.sleep(5)
