import speech_recognition as sr
import pyttsx3
import pywhatkit
import requests
import time

listener = sr.Recognizer()
engine = pyttsx3.init()

# Check available voices
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # female voice (if available)
else:
    engine.setProperty('voice', voices[0].id)  # fallback

engine.say("Hello, I am Luna. How can I help you?")
engine.runAndWait()

def wolfram_spoken(query):
    APP_ID = "96J963W495"
    url = f"http://api.wolframalpha.com/v1/spoken?appid={APP_ID}&i={query}"
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else "I couldn't fetch an answer."
    except Exception as e:
        print("Spoken API error:", e)
        return "Sorry, I couldn't reach."

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        return command.lower()

def run_luna():
    try:
        command = take_command()
        print("Command:", command)

        if 'play' in command:
            song = command.replace('play', '').strip()
            engine.say('Playing ' + song)
            engine.runAndWait()
            pywhatkit.playonyt(song)

        elif 'luna' in command:
            query = command.replace('luna', '').strip()
            output = wolfram_spoken(query)
            print("Answer:", output)
            engine.say("Got it")
            engine.say(output)
            engine.runAndWait()
        else:
            print("Sorry, please say again.")
            engine.say("Sorry, please say again.")
            engine.runAndWait()

    except Exception as e:
        print("Sorry, please say again.",e)
        engine.say("Sorry, please say again.")
        engine.runAndWait()

while True:
    run_luna()
    engine.runAndWait()
    time.sleep(2) 
