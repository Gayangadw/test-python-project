import numpy as np

class chatBot():
    def __init__(self, name):
        print("-----starting up", name, "-----")
        self.name = name

if __name__ == "__main__":
    ai = chatBot(name="dev")

    import speech_recognition as sr
    def speech_to_text(self):
        recognizer= sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening.............")
            audio = recognizer.listen(mic)
            try:
                self.text = recognizer.recognize_google(audio)
                print("me--->" , self.text)
            except:
                print("me---> Error" )

                if __name__== "__main__":
                    ai = chatBot(name="dev")
                    while True:
