import pyaudio
import pyttsx3
import speech_recognition as sr
import os
def take_commands():
    #initializing speech_recognition
    r=sr.Recognizer()
    #opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=0.7
        audio=r.listen(source)
        try:
            print('Recognizing')
            #Recognizing audio using google api
            Query=r.recognize_google(audio)
            print("The query is printed='",Query,",")
        except Exception as e:
            print(e)
            print('Say that again sir')
            return 'None'
        import time
        time .sleep(2)
        return Query
#crating speak() function to giving speaking power
def speak(audio):
    # initializing pyttsx3 module
    engine=pyttsx3.init()
    #anything  we pass inside engine.say()
    #will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()
speak("Do you want to shutdown your computer?")
while True:
    command=take_commands()
    if 'no' in command:
        speak('Thank you sir I will not shut down the computer')
    if 'yes' in command:
        command.speak('Shutting the computer')
        os.system('shutdown /s /t 30')
        break
    speak('say that again sir')