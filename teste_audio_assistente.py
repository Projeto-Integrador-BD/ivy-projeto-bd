# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:48:15 2020

@author: Casa
"""

import webbrowser
import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS


r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            fala_ivy(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio, language='pt-BR')
        except sr.UnknownValueError:
            fala_ivy('Desculpa, eu não consegui compreender!')
        except sr.RequestError:
            fala_ivy('Desculpa, o reconhecimento de voz não está funcionando!')
        return voice_data

def fala_ivy(audio_string):
    tts = gTTS(text=audio_string, lang='pt-BR')
    r = random.randint(1, 100000)
    arquivo_texto = 'audio' + str(r) + '.mp3'
    tts.save(arquivo_texto)
    playsound.playsound(arquivo_texto)
    os.remove(arquivo_texto)
    
def retorno_ivy(voice_data):
        if 'Qual é o seu nome' in voice_data:
            fala_ivy('O meu nome é Ivy')
        if 'pesquisar' in voice_data:
            pesquisar = record_audio('O que você quer pesquisar')
            url = 'https://google.com/search?q=' + pesquisar
            webbrowser.get().open(url)
            fala_ivy('Aqui está o que eu encontrei sobre ' + pesquisar)
            
            
fala_ivy('Como posso te ajudar')
voice_data = record_audio()
fala_ivy(voice_data)
retorno_ivy(voice_data)