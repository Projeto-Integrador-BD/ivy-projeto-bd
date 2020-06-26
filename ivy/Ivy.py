
import webbrowser
import speech_recognition as sr
import playsound
import os
import random
from gtts import gTTS
from util import audio, info_clima_inpe, minha_localizacao

class Ivy():
    nome = "Ivy"
    def falar(self, audio_string):
        tts = gTTS(text=audio_string, lang='pt-BR')
        r = random.randint(1, 100000)
        arquivo_texto = 'audio' + str(r) + '.mp3'
        tts.save(arquivo_texto)
        playsound.playsound(arquivo_texto)
        os.remove(arquivo_texto)

    def ouvir(self, aguardar_chamar = True):
        voice_data = ''
        if(aguardar_chamar):
            voice_data = audio.record_audio('en-US')

        if (voice_data == 'ivy' or not aguardar_chamar):
            self.falar('Diga' + self.rand_tratamento() + ', Como posso te ajudar')
            voice_data = audio.record_audio()
            if (voice_data != ''):
                self.falar("Você disse" + voice_data)
                self.entender(voice_data)
            else:
                self.falar("Desculpa, eu não consegui compreender")
                self.ouvir(False)


    def entender(self, voice_data):
        if 'Qual é o seu nome' in voice_data or 'seu nome' in voice_data or 'qual o seu nome' in voice_data:
            self.falar('O meu nome é ' + self.nome)
        if 'pesquisar' in voice_data:
            self.falar('O que você quer pesquisar?')
            pesquisar = audio.record_audio()
            url = 'https://google.com/search?q=' + pesquisar
            webbrowser.get().open(url)
            self.falar('Aqui está o que eu encontrei sobre ' + pesquisar)
        if 'Como está o tempo' in voice_data or 'Como está o clima' in voice_data or 'clima' in voice_data:
            self.falar('Tranquilo e favorável')
            self.falar("Vou consultar o clima para você")
            location = minha_localizacao.get_localizacao_atual_by_ip()
            coordenadas = location['loc'].split(',')
            latitude = coordenadas[0]
            longitude = coordenadas[1]
            previsao_texto = info_clima_inpe.get_texto_previsao_tempo(latitude, longitude)
            self.falar(previsao_texto)
        if 'como você está' in voice_data:
            self.falar('Estou bem, e você?')
        if 'sair' in voice_data:
            self.falar('Até logo')
            exit()

    def rand_tratamento(self):
        num = random.randrange(1, 6)
        if(num == 1):
            return "meu rei"
        elif(num == 2):
            return "meu amado"
        elif(num == 3):
            return "meu senhor"
        elif(num == 4):
            return "meu lindo"
        elif(num == 5):
            return "meu fofucho"
        elif(num == 6):
            return "meu rei"
        elif(num == 7):
            return "meu cosmos"






