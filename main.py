#import the libary for the project
from gtts import gTTS as tts
import os

#clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

#welcome text
print('Welcome to text to spleech program !')
print('Check supported language list and language code here : https://cloud.google.com/text-to-speech/docs/voices')

#select language for the spleech synthesizer
inpLang = input('Language = ')

#input source text for spleech synthesizer
inpText = input('Input your word here : ')

#input filename
filename = input('Filename : ')

#generate and save audio file from the source text as .mp3 format
to_spleech = tts(text = inpText, lang = inpLang)
to_spleech.save(filename + '.mp3')

#print out success messeage
print('Successfully generated audio file !')
