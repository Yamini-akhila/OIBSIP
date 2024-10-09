import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    paused = False
    while True:
        if not paused:
            command = listen()
            if 'stop' in command:
                speak("Goodbye!")
                break
            elif 'pause' in command:
                speak("Pausing. Say 'resume' to continue.")
                paused = True
            elif 'hello' in command:
                speak("Hello! How can I assist you?")
            elif 'your name' in command:
                speak("I am a Python voice assistant.")
            elif 'time' in command:
                current_time = datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}.")
            elif 'date' in command:
                current_date = datetime.now().strftime("%B %d, %Y")
                speak(f"Today's date is {current_date}.")
            elif 'search' in command:
                speak("What would you like to search for?")
                query = listen()
                if query:
                    url = f"https://www.google.com/search?q={query}"
                    webbrowser.open(url)
                    speak(f"Here are the search results for {query}.")
            else:
                speak("Sorry, I can't help with that right now.")
        else:
            command = listen()
            if 'resume' in command:
                speak("Resuming conversation.")
                paused = False

if _name_ == "_main_":
    main()
