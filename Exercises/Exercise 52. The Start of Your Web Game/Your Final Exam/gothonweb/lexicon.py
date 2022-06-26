# Dictionary of words
lexicon = {
    "direction": ['north', 'south', 'east',
                  'west', 'down', 'up',
                  'left', 'right', 'back'],

    "stop":      ['in', 'the', 'of',
                  'on', 'at', 'a',
                  'or', 'if', 'is',
                  'are'],

    "verb":      ['dodge', 'shoot', 'tell', 
                  'slowly', 'place', 'throw',
                  'go', 'stop', 'kill',
                  'eat', 'open', 'smack'],
        
    "noun":      ['joke', 'bomb', 'door', 
                  'bear', 'princess', 'cabinet', 
                  'nose']

}


# Search lexicon
def search_lexicon(word):
    global lexicon

    def check_same_contents(first_word, second_word):

        for part in set(first_word + second_word):

            if first_word.count(part) != second_word.count(part):
                return False

        return ''.join(second_word)

    lexicon_copy = lexicon.copy()

    for key in lexicon_copy.keys():

        if word.lower() in lexicon_copy[key]:

            return key, word

        else:

            for element in lexicon_copy[key]:
                test = check_same_contents(word, element)

                if test:
                    return key, element


def scan(user_input):
    words = user_input.split()
    result = []

    for word in words:
        try:
            result.append(('number', int(word)))
        
        except ValueError:
            sentence = search_lexicon(word)
            
            result.append(('error', word)) if not sentence else \
                result.append(sentence)

    return result
