######################
# Captura de voz Ivy#
######################

# Importar biblioteca
import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS

# Reconhecedor de Aúdio
r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="pt-BR")
            print(voice_data)
        except sr.UnknownValueError:
            ivy_speak('Desculpe não consegui entender')
        except sr.RequestError:
            ivy_speak('Desculpe, o reconhecimento de voz não está funcionando')
        return voice_data


def ivy_speak(audio_string):
    tts = gTTS(text=audio_string, lang='pt-BR')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
        if 'calculadora' in voice_data:
            ivy_speak('Ok, me diga qual operação deseja realizar? somar, subtrair, mutiplicar ou dividir?')
            voice_data = record_audio()
            if 'somar' in voice_data:
                ivy_speak('Pode falar o primeiro numero')
                voice_data = record_audio()
                num1 = float(voice_data)
                ivy_speak('Pode falar o segundo numero')
                voice_data = record_audio()
                num2 = float(voice_data)
                total = num1 + num2
                ivy_speak('O resultado é:', str(total))
            elif 'subtrair' in voice_data:
                ivy_speak('subtrair, ok, então será uma operação de subtração')
            elif 'multiplicar' in voice_data:
                ivy_speak('multiplicar, ok, então será uma operação de multiplicação')
            elif 'dividir' in voice_data:
                ivy_speak('dividir, ok, então será uma operação de divisão')
        return respond(voice_data)

ivy_speak('O que posso ajudar?')
voice_data = record_audio()
respond(voice_data)

