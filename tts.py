from gtts import gTTS 
import os

#text.txt file should have the text which is to be converted to speech/audio
f=open('text.txt')
x=f.read()

language='en' #set language to english
audio=gTTS(text=x,lang=language,slow=False) #convert text to speech

#The audio file is saved in the same directory
audio.save('audio.wav')
os.system('audio.wav')
