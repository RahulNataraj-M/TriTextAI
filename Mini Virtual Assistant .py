import speech_recognition as sr
import pyttsx3
import pywhatkit
import requests
import time

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Check available voices
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # female voice 
else:
    engine.setProperty('voice', voices[0].id)  # male voice

engine.say("Hello, I am ASSIST_NAME. How can I help you?")
engine.runAndWait()

# Function to query Wolfram Alpha's spoken result API using a simple natural language query
def wolfram_spoken(query):
    APP_ID = "YOUR APP_ID"  # Your Wolfram Alpha app ID
    url = f"http://api.wolframalpha.com/v1/spoken?appid={APP_ID}&i={query}"
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else "I couldn't fetch an answer."
    except Exception as e:
        print("Spoken API error:", e)
        return "Sorry, I couldn't reach."

# Function to capture audio input from microphone and convert it to text
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        return command.lower()

# Main function that handles voice commands and executes tasks accordingly
def run_ASSIST_NAME():
    try:
        command = take_command()  #Fetch the command
        print("Command:", command)

        # Play music if the command includes "play"
        if 'play' in command:
            song = command.replace('play', '').strip()
            engine.say('Playing ' + song)
            engine.runAndWait()
            pywhatkit.playonyt(song)  # Play song on YouTube

        # Ask ASSIST_NAME a question that triggers Wolfram Alpha processing
        elif 'ASSIST_NAME' in command:
            query = command.replace('ASSIST_NAME', '').strip()
            output = wolfram_spoken(query)  # Fetch spoken answer
            print("Answer:", output)
            engine.say("Got it")
            engine.say(output)
            engine.runAndWait()

        # If command is not recognized, ask to repeat
        else:
            print("Sorry, please say again.")
            engine.say("Sorry, please say again.")
            engine.runAndWait()

    except Exception as e:
        print("Sorry, please say again.",e)  # Log the exception
        engine.say("Sorry, please say again.")
        engine.runAndWait()

# Loop to keep the assist running indefinitely with a short pause between interactions
while True:
    run_ASSIST_NAME()
    engine.runAndWait()
    time.sleep(2) 
