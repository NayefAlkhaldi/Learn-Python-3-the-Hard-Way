# extra chllenge
import lexicon

class ParserError(Exception):
    pass

class sentence(object):
    def __init__(self, sentence):
        self.sentence = sentence
        self.subject = 'player'
        self.verb = ''
        self.object = ''
        self.number = None
        self.full = True

    def cut(self, full=True):
        self.full = full
        if not self.full:
            self.subject = ''
        sentence_scanned = lexicon.scan(self.sentence)
        if sentence_scanned[0][0] == 'noun':
            self.subject = sentence_scanned[0][1]

        for set in sentence_scanned:
            if set[0] == 'verb':
                self.verb = set[1]

            elif set[0] == 'noun' or set[0] == 'direction':
                self.object = set[1]

            elif set[0] == 'number':
                self.number = set[1]
    
        if (self.verb == '' or \
            self.object == '') and self.full:
            raise ParserError

    def show(self):
        p_sentence = [self.subject, self.verb, self.object]
        scan = lexicon.scan(self.sentence)
        if self.number:
            p_sentence.insert(scan.index(('number', self.number)) + 1, str(self.number))
        return ' '.join(p_sentence).strip()