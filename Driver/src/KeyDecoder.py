# Author : Lahiru Menikdiwela
# Date : 19/09/2023
# File : patterndetect.py

import pyttsx3

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    """
    data structure to store special characters and perform seaching of the required special characters
    """
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        """add new special character to Trie"""
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c] 
        curr.word = True
    def dfs(self, curr, word):
        """ 
        looks for possible special character and if there is only one return it
        """
        if curr.word:
            return word
        if len(curr.children) >1:
            return "404"
        letter = next(iter(curr.children.keys()))
        #print(letter)
        word += letter
        word = self.dfs(curr.children[letter[0]], word)
        return word        

    def search(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return self.dfs(curr, prefix)
        
specialChMap = { "asterisk":'*', "at":'@', "ampersand": '&', "dollar": '$', "backslash": '\\',"slash": '/',
                "colon": ':', "semicolon": ';', "caret": '^', "tilde": '~', "sharp": '#', "greaterthan": '>', "lessthan": '>',
                 'plus': '+', "add": '+', "subtract": "-", "negative": '-', "equal": '=', "openbracket": '(', "closebracket": ')' }


decodeMap = {}


engine  = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    """
    generate voice feedback
    """
    engine.say(text)
    engine.runAndWait()
talk("welcome")

def getCharacter(code):
    return decodeMap[map]


#store braile paterns
brailePatterns = [[0, [1, 0, 0, 0, 0, 0]], #a
                  [1, [1, 1, 0, 0, 0, 0]], #b
                  [2, [1, 0, 0, 1, 0, 0]], #c
                  [3, [1, 0, 0, 1, 1, 0]], #d
                  [4, [1, 0, 0, 0, 1, 0]], #e
                  [5, [1, 1, 0, 1, 0, 0]], #f
                  [6, [1, 1, 0, 1, 1, 0]], #g
                  [7, [1, 1, 0, 0, 1, 0]], #h
                  [8, [0, 1, 0, 1, 0, 0]], #i
                  [9, [0, 1, 0, 1, 1, 0]], #j
                  [10, [1, 0, 1, 0, 0, 0]], #k
                  [11, [1, 1, 1, 0, 0, 0]], #l
                  [12, [1, 0, 1, 1, 0, 0]], #m
                  [13, [1, 0, 1, 1, 1, 0]], #n
                  [14, [1, 0, 1, 0, 1, 0]], #o
                  [15, [1, 1, 1, 1, 0, 0]], #p
                  [16, [1, 1, 1, 1, 1, 0]], #q
                  [17, [1, 1, 1, 0, 1, 1]], #r
                  [18, [0, 1, 1, 1, 0, 0]], #s
                  [19, [0, 1, 1, 1, 1, 0]], #t
                  [20, [1, 0, 1, 0, 0, 1]], #u
                  [21, [1, 1, 1, 0, 0, 1]], #v
                  [22, [0, 1, 0, 1, 1, 1]], #w
                  [23, [1, 0, 1, 1, 0, 1]], #x
                  [24, [1, 0, 1, 1, 1, 1]], #y
                  [25, [1, 0, 1, 0, 1, 1]], #z
                  [-1, [0, 0, 0, 0, 0, 1]], #1 letter capitalize
                  [-2, [0, 0, 1, 1, 1, 1]], #number state on
                  [-3, [0, 0, 0, 0, 0, 0, 0, 0, 1]], #9 gbutton ->space
                  [-4, [0, 0, 0, 0, 0, 0, 1, 0, 0]], # special character mode on


]

def encode(ar):
    """
    function to encode pattern in to a integer
    """

    code = 0
    for i in range(len(ar)):
        code += (2**i)*ar[i]
    return code

def createHash():
    """ create encoded integer for all keys and stored in a hash"""
    for ar in brailePatterns:
        code = encode(ar[1])
        decodeMap[code] = ar[0]


class KeyDecoder:
    def __init__(self):
        createHash()
        self.word = ""
        self.specialCh = ""
        self.shift = False
        self.num = False
        self.CapsLock = False
        self.speciaclChMode = False
        self.trie = Trie()
        for w in specialChMap.keys():
            self.trie.insert(w)
        



    def decode(self, code):
        
        """"
        decode the integer in to a key and generate voice feedback
        """
        if code>=0:
            if self.speciaclChMode:
                s = chr(ord('a')+code)
                talk(s)
                self.specialCh += s
                response = self.trie.search(self.specialCh)
                if response != '404':
                    self.word += specialChMap[response]
                    talk(response)
                    self.specialCh = ""
                    speciaclChMode = False
                    return specialChMap[response]


                
            elif self.num:
                if code<=9:
                    if code != 9:
                        s = str(code+1)
                    else:
                        s = '0'
                    talk(s)
                    self.word += s
                    return str(s)
                else:
                    talk("not a valid digit")
            else:
                s = chr(ord('a')+code)
                talk(s)
                self.word += s
                if not self.shift:
                    return chr(ord('a')+code)
                self.shift = False
                return chr(ord('A')+code)
        else:
            if code ==-1:
                if not self.shift:
                    talk("shift")
                    self.shift = True
                else:
                    talk("capslock")
                    CapsLock = True
            elif code == -2:
                talk("digit mode")
                self.num = True
            elif code == -3:
                self.shift = False
                self.num = False
                self.speciaclChMode = False
                talk(self.word)
                self.word = ""
                return " "
            elif code == -4:
                talk("Special character mode")
                self.speciaclChMode = True
            
def test():
    
    test_decoder = KeyDecoder()
    assert test_decoder.decode(0) =="a"
    assert test_decoder.decode(1)=="b"
    assert test_decoder.decode(2)=="c"
    test_decoder.decode(-1)
    assert test_decoder.decode(0) == "A"

