import re

lexicon = {
    'direction': ["north", "south", "east", 
                  "west", "down", "up", 
                  "left", "right", "back"],

    'verb':      ["go", "stop", "kill", 
                  "eat"],

    'stop':     ["the", "in", "of", 
                 "from", "at", "it",
                 "is", "on", "and"],

    'noun':     ["door", "bear", "princess", 
                 "cabinet"]
}

def search_lexicon(word):
    if word.isdigit():
        return ('number', int(word))

    for key in lexicon.keys():
        if word.lower() in lexicon[key]:
            return (key, word)

    return ('error', word) 

def scan(user_input):
    user_input = re.sub(r'[^\w]', ' ', user_input)
    user_input = re.sub(' +', ' ', user_input)
    words = user_input.split()
    result = []

    for word in words:
        result.append(search_lexicon(word))

    return result