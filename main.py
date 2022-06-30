from gtts import gTTS as tts
from tqdm import tqdm
import os

# Set working directory
os.system('cls' if os.name == 'nt' else 'clear')
print('Paste your folder path directory that you want to save your file')
os.chdir(input('save to : '))
os.system('cls' if os.name == 'nt' else 'clear')

print('Welcome to text to spleech program !')
print('Check supported language list and language code here : https://cloud.google.com/text-to-speech/docs/voices')

inpLang = input('Language = ')
inpText = input('Input your word here : ')
filename = input('Filename : ')

print('Generating...')
to_spleech = tts(text = inpText, lang = inpLang)

for i in tqdm(range(1)):
    to_spleech.save(filename + '.mp3')

print('Successfully generated audio file !')