<<<<<<< HEAD
# Necessário instalar o pyAudio: 
# pip install pyaudio
# depois instala o speech_recognition: 
# pip install SpeechRecognition
import speech_recognition as sr
import pyttsx3
from gerador_senha import gerar_senha

# Inicializa o sintetizador de voz
engine = pyttsx3.init()

# cria uma variavel para reconhecimento do audio
reconhecedor = sr.Recognizer()

opcoes = ["senha"]

with sr.Microphone() as source:
    while (True):
        try:
            # passar o que o programa ouviu para a variavel audio
            audio = reconhecedor.listen(source)

            # engine.say("Olá, por favor me peça uma funcionalidade")
            # engine.runAndWait()

            # imprime o audio e passa para o algoritmo de reconhecimento escolhido
            # no caso, a google
            frase = reconhecedor.recognize_google(audio, language="pt-BR")
            print(frase)

            if frase in opcoes:
                if frase == "senha":
                    engine.say("ok, estou gerando a sua senha. Aguarde um segundo")
                    engine.runAndWait()
                    
                    senha_gerada = gerar_senha()
                    
                    engine.say("sua senha foi gerada com sucesso. Olhe na tela para verifica-la")
                    engine.runAndWait()

                break
    
        except Exception as err:
            engine.say("Nao entendi, poderia falar novamente?")
            engine.runAndWait()


# gerar senha aleatória 
# quando for perguntado gerar senha deve-se aparecer na tela ( Com quantos números?)
# após a identificação do número deve-se gerar a senha com os números respectivos


print("FIM DO PROGRAMA")
=======
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
print("teste")
>>>>>>> 8ce782e959178bb687571a1341415fec11508ffa
