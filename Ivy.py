######################
# Captura de voz Ivy#
######################

# Importar biblioteca
import speech_recognition as sr
import playsound
import time
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
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            ivy_speak('Desculpe não consegui entender')
        return voice_data


def ivy_speak(audio_string):
    tts = gTTS(text=audio_string, lang='pt-BR')
    r = random.randint(1, 10000000)
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
                ivy_speak('somar, ok, então será uma operação de adição')
            elif 'subtrair' in record_audio():
                ivy_speak('subtrair, ok, então será uma operação de subtração')
            elif 'multiplicar' in record_audio():
                ivy_speak('multiplicar, ok, então será uma operação de multiplicação')
            elif 'dividir' in record_audio():
                ivy_speak('dividir, ok, então será uma operação de divisão')


#if 'ivy' in record_audio():
ivy_speak('O que posso ajudar?')
voice_data = record_audio()
respond(voice_data)

