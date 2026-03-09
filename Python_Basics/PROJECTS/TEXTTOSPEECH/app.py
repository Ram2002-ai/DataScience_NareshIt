from tkinter import *
import pyttsx3
from nltk.corpus import wordnet
import nltk

# download wordnet data if data not already download
nltk.download('wordnet')

# function to speak the aduio

def speak(audio):
    # intialize the pyttsx3 engine
    engine=pyttsx3.init('sapi5')

    # set the voice property to  the default
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    # speak the given aduio text
    engine.say(audio)
    engine.runAndwait()

# function to find synonyms using nltk's wordnet

def find_synonyms(word):
    syn_words=set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            syn_words.add(lemma.name())
    return list(syn_words)