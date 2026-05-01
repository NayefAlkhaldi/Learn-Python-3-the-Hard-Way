import re


def scan(text):
    """Checks for words in text."""
    data = {
        'direction': ['north', 'east', 'west', 'south'],
        'verb': ['go', 'kill', 'eat'],
        'stop': ['in', 'on', 'at', 'of', 'the'],
        'noun': ['bear', 'princess', 'bears', 'princesses']
    }

    result = []
    text = re.sub(' +', ' ', text.strip()).split()

    for word in text:
        found = False
        for type, words in data.items():
            if word.lower() in words:
                result.append((type, word))
                found = True

        if not found:
            if word.isdigit():
                result.append(('number', int(word)))
            else:
                result.append(('error', word))
        

    return result