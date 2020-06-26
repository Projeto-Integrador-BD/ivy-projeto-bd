import speech_recognition as sr
def record_audio(language = 'pt-BR'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language=language)
            print(voice_data)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""
        return voice_data