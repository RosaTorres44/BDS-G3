from gtts import gTTS
import os

texto = input("Digite o texto que deseja transformar em audio: ")
tts = gTTS(texto, lang='es')
finename = 'MODULO02/AUDIO/audio.mp3'

tts.save(finename)
import platform

os.system(f"open {finename}")