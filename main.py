#import the libary for the project
from gtts import gTTS as tts
from tqdm import tqdm
import os

#setup the save folder directory
os.system('cls' if os.name == 'nt' else 'clear')
print('Paste your folder path directory that you want to save your file')
os.chdir(input('save to : '))
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

#generate audio file from the source text as .mp3 format
print('Generating...')
to_spleech = tts(text = inpText, lang = inpLang)

#save audio file as .mp3 format
for i in tqdm(range(1)):
    to_spleech.save(filename + '.mp3')

#print out success messeage
print('Successfully generated audio file !')
