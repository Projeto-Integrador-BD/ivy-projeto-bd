import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
reconhecedor = sr.Recognizer()

with sr.Microphone()as source:
    while(True):
        try:
            audio=reconhecedor.listem(source)
            frase= reconhecedor.recognize_google(audio, language= "pt-BR")
            print(frase)
            if frase == "ola":
                engine.say("hoje vou ajudar ?")
                engine.runAndWait()
            break

        except Exception as erro:
            engine.say("o que você quer dizer ?")
            engine.runAndWait()
print("fim do programa!")





