import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")
        return ""

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def perform_task(command):
    command = command.lower()
    
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'what is your name' in command:
        speak("I am your personal assistant.")
    elif 'what time is it' in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif 'open google' in command:
        import webbrowser
        webbrowser.open("http://www.google.com")
        speak("Opening Google")
    else:
        speak("Sorry, I didn't understand that command.")

def main():
    while True:
        command = listen()
        if command:
            perform_task(command)
        if 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()

import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def perform_task(command):
    command = command.lower()
    
    if 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'what is your name' in command:
        speak("I am your personal assistant.")
    elif 'what time is it' in command:
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif 'open google' in command:
        webbrowser.open("http://www.google.com")
        speak("Opening Google")
    else:
        speak("Sorry, I didn't understand that command.")

def main():
    while True:
        command = listen()
        if command:
            perform_task(command)
        if 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
