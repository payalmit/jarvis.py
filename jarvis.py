import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
import wikipedia
from requests import get
import webbrowser
import pywhatkit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 0.8
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
    try:
        print('recognizing...')
        Query = r.recognize_google(audio, language='en-in')
        print('user said:' + Query)
    except Exception as e:
        speak("say this again please...")
        return 'none'
    return Query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning')
    elif hour > 12 and hour < 18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('hello sir, i am jarvis...how can i help you')


def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('payalmittal651@gmail.com', 'payalasd')
    server.sendmail('payalmittal651@gmail.com', to, content)


if __name__ == "__main__":
    wish()
    while True:
        if 1:
            Query = takecommand().lower()
        # logic buiding for task
        if 'open notepad' in Query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open command prompt' in Query:
            os.system('start cmd')

        elif 'open camera' in Query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('camera', frame)
                cv2.waitKey(5)
            cap.release()
            cv2.destroyWindow()




        elif 'play music' in Query:
            music_dir = "c:\\"
            songs = os.listdir(music_dir)
            rs = random.choice(songs)
            os.startfile(os.path.join(music_dir, rs))

        elif 'ip address' in Query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip is {ip}")

        elif 'wikipedia' in Query:
            speak("seaching wikipedia")
            Query = Query.replace("wikipedia", "")
            results = wikipedia.summary(Query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in Query:
            webbrowser.open("youtube.com")

        elif 'open google' in Query:
            speak('what i should search sir')
            go = takecommand().lower()
            webbrowser.open(f"{go}")

        elif 'send whatsapp message ' in Query:
            speak('tell the message')
            message = takecommand().lower()
            pywhatkit.sendwhatmsg('+919090245339', message, 13, 8)

        elif 'play song in youtube' in Query:
            pywhatkit.playonyt('tera yaar hun mein')

        elif 'send mail' in Query:
            to = 'payalmittal651@gmail.com'
            speak('content..')
            content = takecommand().lower()
            SendEmail(to, content)
            speak('send email successful')
            server.close()


        elif 'tell me the time' in Query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")



        elif 'no thanks' in Query:
            speak('thanks for using me')
            sys.exit()

        speak('sir do you any other work')
