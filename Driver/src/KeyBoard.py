# Author : Dasun Theekshana, Lahiru Manikdikwela
# Date : 20/09/2023
# File : SerialReader.py

import pynput.keyboard as kb
import pyttsx3

class KeyBoard():
    def __init__(self):
        self.keyboard = kb.Controller()
        self.engine = pyttsx3.init()
        self.configure()
        
    def configure(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        
    def addtobuffer(self, key):
        """
            Sends a character to the keyboard input buffer.
        """
        self.keyboard.press(key)
        self.keyboard.release(key)
        
    def voice(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        
    def keypress(self, key):
        self.addtobuffer(key)
        self.voice(key)