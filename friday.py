import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random 
import smtplib


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Aryan!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Aryan!")
    
    else:
        speak("Good Evening Aryan!")

    speak("I am Friday. Sir tell me how may I help you?")

def takeCommand():
    #It takes microphone input from the user and return an output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e) #prints error
        print("Say that again please...")
        return "None"
    return query

'''def sendEmail(to, content):   
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('','')
    server.sendmail('',to,content)
    server.close()'''


if __name__== "__main__":
    #speak("Aryan is a good boy")
    wishMe()
    while True:
        query=takeCommand().lower()
        #Logic for execting tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia") 
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")

        elif 'open news' in query:
            speak("Opening News...")
            webbrowser.open("https://tinyurl.com/39mf4hkw")

        elif 'play music' in query :
            music_dir='C:\\Users\\Aryan\\Desktop\\DESK FRONT\\Aryan\\Music'
            songs = os.listdir(music_dir)
            rand= random.choice(songs)
            speak("Here is a surprise song for you on my behalf")
            os.startfile(os.path.join(music_dir,rand))

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")  

        elif 'open vs code' in query :
            speak("Opening VS Code")
            codePath1='C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath1)

        elif 'open valorant' in query:
            speak ("Opening valorant")
            codePath2='C:\\Riot Games\\Riot Client\\RiotClientServices.exe'
            os.startfile(codePath2)

        
        elif 'how are you' in query:
            speak('Im fantastic, hope you are doing good')
        

        
        elif 'Good bye' in query or 'quit' in query or'bye' in query or 'bye bye' in query:
            speak('It was a pleasure helping you. Have a nice day. See you soon')
            break

        elif query=="None":
            continue
        
        else:
            speak("Say that again please...")

        '''elif 'email to aryan' in query:
            try:
                speak('What should i say?')
                content=takeCommand()
                to=" "
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry the email has not been sent")'''
            
                    
            


