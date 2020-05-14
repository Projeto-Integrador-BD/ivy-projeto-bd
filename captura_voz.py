# Necessário instalar o pyAudio: 
# pip install pyaudio
# depois instala o speech_recognition: 
# pip install SpeechRecognition
#test
import speech_recognition as sr

# cria uma variavel para reconhecimento do audio
reconhecedor = sr.Recognizer()

with sr.Microphone() as source:
    # passar o que o programa ouviu para a variavel audio
    audio = reconhecedor.listen(source)

    # imprime o audio e passa para o algoritmo de reconhecimento escolhido
    # no caso, a google
    print(reconhecedor.recognize_google(audio, language="pt-BR"))

print("FIM DO PROGRAMA")