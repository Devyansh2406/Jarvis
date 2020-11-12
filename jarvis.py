import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voice', voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!") 

    speak("I am Jarvis Sir. Please tell how may i help you sir")
  
def takecommand():
    # It takess microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
     wishMe()
     while True:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
           webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
           webbrowser.open("https://www.google.com/")

        elif 'open my website' in query:
            webbrowser.open("https://devyanshsandwar.whjr.site/")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open code.org' in query:
            webbrowser.open("https://studio.code.org/home#")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.com/")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com/")

        elif 'open earth' in query:
            webbrowser.open("https://earth.google.com/web/@51.14757366,-150.62172979,-14086.08965768a,22265839.23206091d,35y,0h,0t,0r")

        elif 'open gaana' in query:
            webbrowser.open("https://gaana.com/")

        elif 'my music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=LBr7kECsjcQ")         

        elif 'play music' in query:
            speak("playing sir")
            music_dir = 'D:\My music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            speak("telling time sir")
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strtime}")

        elif 'open code' in query:
            speak("launching sir")
            codePath = "C:\\Users\\DevyanshR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        elif 'open whatsapp' in query:
            speak("launching sir")                                 
            codePath = "C:\\Users\\DevyanshR\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath) 

        elif 'open life' in query:
            speak("launching sir")
            codePath = "C:\\Users\\DevyanshR\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)

        elif 'open game' in query:
            speak("launching sir")
            codePath = "Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak("launching sir")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
    

        elif 'what is your name' in query:
            speak("sir,my name is jarvis and i am your assistant sir") 

        elif 'play a song that tony stark would like to hear while working' in query:
            speak('i know what to play')
            webbrowser.open("https://www.youtube.com/watch?v=WNlFFKNKkvw")

        elif 'who created you' in query:
            speak("sir, i am created by you")

        elif 'open google sheets' in query:
            speak('opening sir right away')
            webbrowser.open("https://docs.google.com/spreadsheets/u/0/")
