import pyttsx3

decodeMap = {}
shift = False
num = False
CapsLock = False

engine  = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
talk("greater than")

def getCharacter(code):
    return decodeMap[map]

brailePatterns = [[0, [1, 0, 0, 0, 0, 0]],
                  [1, [1, 1, 0, 0, 0, 0]],
                  [2, [1, 0, 0, 1, 0, 0]],
                  [3, [1, 0, 0, 1, 1, 0]],
                  [4, [1, 0, 0, 0, 1, 0]],
                  [5, [1, 1, 0, 1, 0, 0]],
                  [6, [1, 1, 0, 1, 1, 0]],
                  [7, [1, 1, 0, 0, 1, 0]],
                  [8, [0, 1, 0, 1, 0, 0]],
                  [9, [0, 1, 0, 1, 1, 0]],
                  [10, [1, 0, 1, 0, 0, 0]],
                  [11, [1, 1, 1, 0, 0, 0]],
                  [12, [1, 0, 1, 1, 0, 0]],
                  [13, [1, 0, 1, 1, 1, 0]],
                  [14, [1, 0, 1, 0, 1, 0]],
                  [15, [1, 1, 1, 1, 0, 0]],
                  [16, [1, 1, 1, 1, 1, 0]],
                  [17, [1, 1, 1, 0, 1, 1]],
                  [18, [0, 1, 1, 1, 0, 0]],
                  [19, [0, 1, 1, 1, 1, 0]],
                  [20, [1, 0, 1, 0, 0, 1]],
                  [21, [1, 1, 1, 0, 0, 1]],
                  [22, [0, 1, 0, 1, 1, 1]],
                  [23, [1, 0, 1, 1, 0, 1]],
                  [24, [1, 0, 1, 1, 1, 1]],
                  [25, [1, 0, 1, 0, 1, 1]],
                  [-1, [0, 0, 0, 0, 0, 1]], #1 letter capitalize
                  [-2, [0, 0, 1, 1, 1, 1]], #number state on
                  [-3, [0, 0, 0, 0, 0, 0, 0, 0, 1]], #9 button ->space


]

def encode(ar):

    code = 0
    for i in range(len(ar)):
        code += (2**i)*ar[i]
    return code

def createHash():
    for ar in brailePatterns:
        code = encode(ar[1])
        decodeMap[code] = ar[0]

createHash()


#num = False
word = ""
def decode(arr):
    global num, shift, CapsLock, word
    code = decodeMap[encode(arr)]
    if code>=0:
        if num:
            if code<=9:
                s = str(code+1)
                talk(s)
                word += s
                return str(s)
            else:
                talk("not a valid digit")
        else:
            s = chr(ord('a')+code)
            talk(s)
            word += s
            if not shift:
                return chr(ord('a')+code)
            shift = False
            return chr(ord('A')+code)
    else:
        if code ==-1:
            if not shift:
                talk("shift")
                shift = True
            else:
                talk("capslock")
                CapsLock = True
        elif code == -2:
            talk("digit mode")
            num = True
        elif code == -3:
            shift = False
            num = False
            talk(word)
            word = ""
            
print(decode([1, 1, 1, 0, 0, 0]))
print(decode([0, 0, 1, 1, 1, 1]))
print(decode([1, 0, 0, 0, 0, 0]))
print(decode([1, 1, 0, 0, 0, 0]))
print(decode([0, 0, 0, 0, 0, 0, 0, 0, 1]))