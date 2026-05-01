from ast import literal_eval

def check_data(file):
    with open('ex45 - Room Escape/data.txt', 'r+') as file:
        content = file.read()

        try:
            literal_eval(content)
        except SyntaxError:
            file.write("{'visits': 0}")
            file.close()

def write_data(file):
    with open(file, 'r+') as file:
        content = file.read()
        data = literal_eval(content)
        data["visits"] = data["visits"] + 1

        file.seek(0)
        file.truncate()
        file.write(str(data))
        file.close()
    
def cut_line(line):
    """Removes all symbols and unwanted capital letters."""
    line = line.lower().strip()

    new_line = []
    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'g',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y',
                'z']
    
    words = line.split()
    for word in words:

        for letter in word:
            if letter not in alphabet:
                try:
                    int(letter)
                except ValueError:
                    # Removes the letter
                    word = word.replace(letter, '')

        # Finally combine all words into one sentence
        new_line.append(word + ' ')

    return''.join(new_line)


def intext(line, *keywords, mode="check_all"):
    """Finds if words exist in a sentence."""
    if type(keywords) != "<class 'list'>":
        keywords = list(keywords)

    if type(line) != "<class 'list'>":
        line = line.split()

    # clean lists
    for i in range(0, len(line)):
        line[i] = line[i].lower()
            
    for i in range(0, len(keywords)):
        keywords[i] = keywords[i].lower()


    line = [x for x in line if x != ' ' and x != '']
    keywords = [x for x in keywords if x != ' ' and x != '']


    if mode == "check_all":
        for word in keywords:
            if ' ' in word:
                # Check everything
                for piece in word.split():
                    if piece not in line:
                        return False

            elif word not in line:
                return False
        
        return True
        

    elif mode == "check_one":
        # Check if there are any spaces
        if ' ' in ''.join(keywords):
            for word in keywords:
                words_set = word.split()
                if set(words_set).issubset(line):
                    return True

            return False

        # if not, then it would be much simpler.
        else:
            for word in keywords:
                if word in line:
                    return True

        return False

    else:
        raise AttributeError (f"'{mode}' mode does not exist for this function.")