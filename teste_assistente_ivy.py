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


def record_audio(repeat_talk = False, language = 'pt-BR'):
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language=language)
            if (voice_data != '' and repeat_talk):
                fala_ivy("Você disse " + voice_data)
            print(voice_data)
        except sr.UnknownValueError:
            if(repeat_talk):
                fala_ivy('Desculpa, eu não consegui compreender!')
        except sr.RequestError:
            if (repeat_talk):
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
            fala_ivy('O que você quer pesquisar?')
            pesquisar = record_audio(False)
            url = 'https://google.com/search?q=' + pesquisar
            webbrowser.get().open(url)
            fala_ivy('Aqui está o que eu encontrei sobre ' + pesquisar)
        if 'Como está o tempo' in voice_data:
            fala_ivy('Tranquilo e favorável')
        if 'como você está' in voice_data:
            fala_ivy('Estou bem, e você?')
        if 'sair' in voice_data:
            fala_ivy('Até logo')
            exit()


while(True):
    voice_data = record_audio(False, 'en-US')
    if(voice_data == 'ivy'):
        fala_ivy('Diga meu rei, Como posso te ajudar')
        voice_data = record_audio(True)
        if(voice_data != ''):
            retorno_ivy(voice_data)