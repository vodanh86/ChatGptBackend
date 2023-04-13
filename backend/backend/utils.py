from django.core.cache import cache
try:
    import cPickle as pickle
except:
    import pickle

DUMP_FILE = "ChatGpt.dat"
CACHED_GPT = {}
try:
    CACHED_GPT = pickle.load(open(DUMP_FILE,'rb'))
except FileNotFoundError:
    pass

def makeKey(input1, input2, input3):
    key1 = ''.join(char for char in input1 if char.isalnum())
    key2 = ''.join(char for char in input2 if char.isalnum())
    key3 = ''.join(char for char in input3 if char.isalnum())
    return key1 + ":" + key2 + ":" + key3

def checkChatCache(input1, input2, input3):
    key = makeKey(input1, input2, input3)
    print("key: " + key)
    if CACHED_GPT.get(key):
        print ("found: " + CACHED_GPT.get(key))
    return CACHED_GPT.get(key)

def setChatCache(input1, input2, input3, value):
    key = makeKey(input1, input2, input3)
    print("key: " + key)
    CACHED_GPT[key] = value
    pickle.dump(CACHED_GPT,  open(DUMP_FILE, 'wb'))

def checkImageCache(input):
    key = ''.join(char for char in input if char.isalnum())
    print("key: " + key)
    if CACHED_GPT.get(key):
        print ("found: " + CACHED_GPT.get(key))
    return CACHED_GPT.get(key)

def setImageCache(input, value):
    key = ''.join(char for char in input if char.isalnum())
    print("key: " + key)
    CACHED_GPT[key] = value
    pickle.dump(CACHED_GPT,  open(DUMP_FILE, 'wb'))