from decimal import Context
import pyttsx3 #texttospeech
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os 
import smtplib

print("Intializing Alexa")

Master = "Tauqheer"
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

#it will speak the string passed 
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <12:
        speak("Good morning" +Master)
    elif hour >= 12 and hour <18:
        speak("Good Afternoon" +Master)

    else:
        speak("Good evening"+Master)

    speak("I am Alexa,How may I help You?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print("Say that Again Please")
        query = None

    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("yourmail.com","password")
    server.sendmail(" recipient mail id",to,content)
    server.close()

def main():
    #main code starts here 
    speak("Initializing Alexa...")
    wishMe()
    query = command()

    #logic for executing task asked by the user

    if 'wikipedia' in query.lower():
        speak("searching wikipedia..")
        query = query.replace("wikipedia","")
        results  = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif "open youtube" in query.lower():
        #webbrowser.open("youtube.com")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "open google" in query.lower():
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "open chess" in query.lower():
        url = "chess.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "open whatsapp" in query.lower():
        url = "https://web.whatsapp.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "play music" in query.lower():
        songs_dir = "C:\\Users\\Admin\\OneDrive\\Desktop\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[1]))

    elif "beatbox" in query.lower() :
        url = "https://www.youtube.com/watch?v=eiwosaanyM8"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "open code" in query.lower():
        codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codePath)

    elif "send mail" in query.lower():
        try:
            speak("What should i send")
            Content = takeCommand()
            to = " recipient mail id"
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)

main()  