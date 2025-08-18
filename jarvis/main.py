import pyttsx3
import speech_recognition
import  datetime
import markdown
import pyautogui
from i_o import file_w
from AppOpener import open,close

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        r.energy_threshold = 250
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return takeCommand()
    return query
def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")


if __name__ == '__main__':
    from IPython.display import Markdown
    from bs4 import BeautifulSoup
    import google.generativeai as genai
    import textwrap
    import pywhatkit
    from pywhatkit import playonyt
    def to_text(text):
        text = text.replace('•', '  *')
        md = Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
        html_text = markdown.markdown(md.data)
        text = "".join(BeautifulSoup(html_text, "html.parser").findAll(text=True))
        return text

    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])


    def computer_brian(text):
        q = text.split(" ")
        if q[0] == "open":
            open(''.join(q[1::]), match_closest=True)
            speak(f"opening {" ".join(q[1::])}")
        elif q[0] == "close":
            close(''.join(q[1::]), match_closest=True)
            speak(f"closing {" ".join(q[1::])}")
        elif q[0] == "play":
            speak(f"playing music {" ".join(q[1::])} Slowed + Reverb")
            playonyt(f"{" ".join(q[1::])} Slowed + Reverb")
        elif "screenshot" in q:
            speak("please tell me the name of screenshot")
            name = takeCommand()
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot has been saved")
        elif "pause" in q:
            pyautogui.press("k")
            speak("video paused")
        elif "who created you" in text:
            speak("I am virtual assistant created by Nikhil vyavaharee")
        elif "mute" in q:
            pyautogui.press("m")
            speak("video mute")
        elif "full" and "screen" in q:
            pyautogui.press("f")
            speak("video mute")
        elif q[0] == "search":
            speak("This is what I found on google")
            pywhatkit.search(f"{" ".join(q[1::])}")

        else:
            response = chat.send_message(text)
            responsetext = to_text(response.text)
            speak(responsetext)
            file_w(responsetext)

    query = takeCommand().lower()
    if "jarvis" in query:
        greetMe()
        while True:
            query = takeCommand().lower()
            if "wake up" in query:
                while True:
                    query = takeCommand().lower()
                    computer_brian(query)
                    if "go to sleep" in query:
                        speak("Ok , You can me call anytime")
                        break
