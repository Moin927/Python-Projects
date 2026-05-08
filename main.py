import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text) :
    engine.say(text)
    engine.runAndWait() 
if __name__=="__main__" :
    speak("Initializing Jarvis......")
while True  :
    # listen for the word Jarvis
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .... ")
        audio =r.listen(source)

# recognize speech using Sphinx
print("Recognizing .....")
try:
    command = r.recognize_google(audio)
    print("You said:", command)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
