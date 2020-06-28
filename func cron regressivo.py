import webbrowser
import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
from time import sleep

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            fala_ivy(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio, language='pt-BR')
            print(voice_data)
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
    if 'vou começar a trabalhar' in voice_data:
        fala_ivy('então, vou ajudar, primeiro feche todas as distrações possíveis')


def cronômetro_regressivo():
    fala_ivy("Quantos tempo irá dedicar a sua tarefa ?")
    t = int(record_audio())
    for tempo in range(t, 0, -1):
        if sleep(t) == sleep(8):
            fala_ivy("Foco no trabalho!")
        if sleep(t) == sleep(6):
            fala_ivy("não mexa no whatsapp!")
        if sleep(t) == sleep(2):
            fala_ivy("quase lá")
        break


fala_ivy('Como posso te ajudar')
voice_data = record_audio()
fala_ivy('Vou cronometrar sua tarefa!')
cronômetro_regressivo()
fala_ivy("terminou!")
