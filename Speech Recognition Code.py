# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:50:36 2020

@author: lockd
"""


import speech_recognition as sr

AUDIO_FILE = ("D:/My Python Projects/Week 5/Speech Recognition/Sample.wav")
#Use AUDIO_FILE as source

r = sr.Recognizer()     #Initialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
#Reads the audio file
    
try:
    print("Audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition couldn't understand audio")
except sr.RequestError:
    print("Couldn't get the results from Google Speech Recognition")
    
    