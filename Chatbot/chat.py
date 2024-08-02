import pyttsx3
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)


def female(audio):
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def rect():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak")
        female("Please Speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Analyzing ...")
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            female("You said : {}".format(text))
            return text
        except:
            print("Sorry could not recognize what you said")
            female("Sorry could not recognize what you said")
            rect()


def who_is(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query, sentences=2)
            except Exception:
                pass
    return "I don't know about "+query


female("Hi everyone. I am Barbie. Barbie with Brains.")
counter = 1
while counter == 1:
    lines = rect()
    if(lines == "hi barbie" or lines == "hello Barbie" or lines == "hi Bhabi" or lines == "hello Bhabi"):
        female("Hello. Nice to meet you.")
    elif(lines == "how are you"):
        female("I am good. How are you?")
    elif(lines == "I am fine" or lines == "fine"):
        female("I am very pleased to know.")
    elif(lines == "tell me a joke"):
        female("Here is one for you. What does a cloud wear under his raincoat ? The answer is: Thunderwear")
    elif(lines == "what is your name"):
        female("My name is barbie.")
    elif(lines == "tell me about yourself"):
        female("I am barbie. From outside I am a soft toy, but , from the inside I am a conversational chatbout built in python. You can ask me anything by saying after a pause of 1 second when I say please speak. You can say quit to shut me down.")
    elif(lines == "quit"):
        counter = 0
        female("It was nice to meet you. See you again.")
    else:
        female("Let me look it up for you.")
        female(who_is(lines))
