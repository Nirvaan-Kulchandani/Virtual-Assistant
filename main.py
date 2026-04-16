# pip install speechrecognition
# pip install pyttsx3
# pip install google-generativeai

import speech_recognition as sr
import pyttsx3
# import pyaudio
import google.generativeai as genai
import time
import os
import webbrowser as web
import random
from Music_library import *
import smtplib # To send emails
import pyautogui
# 1270x20

# You are a skilled in genral tasks like alexe, google cloud, etc. You are are very skilled and knowledged friend, and very much skillful in coding. You give short and precise answers. Your name is Jarvis and you are a virtual assistant, made by Nirvaan Kulchandani.

genai.configure(api_key="AIzaSyBP_43TMrjGG-OMXYdywpkxm6our9mPRi8")

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="You are a skilled in genral tasks like alexe, google cloud, etc. You are very skilled and knowledged friend, and very much skillful in coding. You give short and precise answers. Your name is Jarvis and you are a virtual assistant, made by Nirvaan Kulchandani. You can also help with opening applications, playing music, small tasks, etc."
)

# Initialize the speech recognition and text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def AI_Answer(prompt: str):

    prompt_list = []
    try:
        prompt_list.append(prompt)
        response = model.generate_content(prompt_list)
        return response.text
    except Exception as e:
        print("Error generating response:", e)
        speak("I'm sorry, I couldn't process that.")



def send_email(to, subject, body):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        from_address = "someone@domain.com"  # Replace with your Gmail address
        password = "abcd efgh igkl mnop"  # Replace with your gmail App Password

        # Login to your email account
        server.login(from_address, password)

        # Create the email message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(to_addrs=to, from_addr=from_address, msg=message)
        server.quit()
        print("Email sent successfully")
        speak("Email sent successfully")

    except Exception as e:
        print("Some error while sending mail", e)
        speak("Some error while sending mail")

        

def Process_command(command):
    if "open google" in command:
        speak("Opening Google")
        web.open("https://www.google.com")

    elif "open chrome" in command:
        speak("Opening Chrome")
        web.open("https://www.chrome.com")

    elif "minimize" in str(command).strip() or "minimise" in str(command).strip():
        pyautogui.click(x=1270, y=20)
        
    elif "open youtube" in command:
        speak("Opening Youtube")
        web.open("https://www.youtube.com")

    elif "openvscode" in command.replace(" ", ""):
        speak("Opening Visual Studio Code")
        os.system("code")

    elif "open excel" in command:
        speak("Opening Excel")
        os.system("start Excel")

    elif "play music" in command:
        speak("Playing Music")

        any_song = random.choice(musics)
        
        if music_dict[any_song].startswith("https"):
            web.open(music_dict[any_song])
            # time.sleep(17)
            # pyautogui.click(x=1270, y=20)

        else:
            os.system(f"start {music_dict[any_song]}")

        

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "what is the time" in command:
        speak(f"The Time is: {time.strftime('%H:%M:%S')}")
        print(f"The Time is: {time.strftime('%H:%M:%S')}")
        
    elif "open file explorer" in command:
        speak("Opening File Explorer")
        os.system("explorer")
    
    elif "open command prompt" in command:
        speak("Opening Command Prompt")
        os.system("cmd")

    elif "open settings" in command:
        speak("Opening Settings")
        os.system("start ms-settings:")

    elif "open spotify" in command:
        speak("Opening Spotify")
        web.open("https://open.spotify.com")

    elif "send email" in command:
        speak("To whom do you want to send the email?")
        
        with sr.Microphone() as source:
            
            print("Listening for email recipient...")

            audio = r.listen(source, timeout=7)
            try:
                to_voice = r.recognize_google(audio).lower()
                to = f"{to_voice}@gmail.com".replace(" ", "")
                print(f"Recipient: {to}")
                # to = input("Enter") # Testing purpose

            except Exception as e:
                print("Could not understand the recipient name.")
                speak("Could not understand the recipient name.")
                return
            
        speak("What is the subject of the email?")
        with sr.Microphone() as source:
            
            print("Listening for email subject...")

            audio = r.listen(source, timeout=7)
            try:
                command = r.recognize_google(audio).lower()
                subject = command
                print(f"Subject: {subject}")

            except Exception as e:
                print("Could not understand the subject.")
                speak("Could not understand the subject.")
                return
            
        speak("What do you want to send?")
        with sr.Microphone() as source:
            
            print("Listening for email body...")

            audio = r.listen(source, timeout=7)
            try:
                body_voice = r.recognize_google(audio).lower()
                body = body_voice
                print(f"Body: {body}")

            except Exception as e:
                print("Could not understand the body of the email.")
                speak("Could not understand the body of the email.")
                return
            
        speak("Sending email...")
        send_email(to, subject, body)

    else:
        print("Processing with AI...\n")
        a = AI_Answer(command)
        print(a)
        speak(a)




if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
            # Listen for the wake command 'Jarvis'
            # Obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=10, phrase_time_limit=5)

            print("Recognizing...")
            try:
                wake_word = r.recognize_google(audio).lower()

                if "jarvis" in wake_word:
                    speak("Yeah, Jarvis Active!")

                    while True:

                        with sr.Microphone() as source:
                            print("Listening for command...")
                            # Below timeout means that if no command is given within 7 seconds, it will stop listening 
                            audio = r.listen(source, timeout=7)
                            
                            command = r.recognize_google(audio).lower()
                            print(f"Command given: {command}")
                            
                            Process_command(command)

            except Exception as e:
                print(f"No commands given")











# AIzaSyBP_43TMrjGG-OMXYdywpkxm6our9mPRi8