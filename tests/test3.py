# from gtts import gTTS
# import os
#
# # Текстът, който искаш да бъде произнесен
# text = "МАЙКА ТИ ДА ЕБА!"
#
# # Създаване на gTTS обект с избран текст и език
# # 'bg' означава български език
# tts = gTTS(text=text, lang='bg')
#
# # Записваме говорния файл във формат mp3
# tts.save("hello.mp3")
#
# # Възпроизвеждаме файла с помощта на системния плейър
# # За Windows използваме os.system с командата "start"
# os.system("start hello.mp3")
#





import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Пример на използване:
speak("Здравей, какво мога да направя за теб?")



# import requests
#
# r = requests.get('https://www.instagram.com/worldsbk/')
# print(r.text)