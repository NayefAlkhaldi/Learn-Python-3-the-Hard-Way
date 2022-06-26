from nose.tools import *
from parser import *
from lexicon import *

def test_peek():
    # Test ability to recongize blank tuples
    blank_tuple = ([])
    assert_equal(None, peek(blank_tuple))

    # Test 2 tuples
    sentence = ([('verb', 'run'),
                 ('direction', 'west')])

    assert_equal('verb', peek(sentence))
    

def test_match():
    sentence = ([('noun', 'nose')])
    assert_equal(None, match(sentence, 'verb'))

    word_list = [('stop','the'),
                 ('direction', 'north')]

    assert_equal(('stop', 'the'), match(word_list, 'stop'))

def test_skip():
    word_list = [('direction','left'),
                 ('direction', 'west'),
                 ('verb', 'go')]

    skip(word_list, peek(word_list))
    assert_equal([('verb', 'go')], word_list)

def test_parse_verb():

    # First word is a verb
    word_list = [('verb', 'smack'),
                 ('noun', 'bear')]

    assert_equal(('verb','smack'),  parse_verb(word_list))

    # Test removing stop words
    word_list = [('verb', 'smack'),
                 ('stop', 'the'),
                 ('noun', 'door')]

    assert_equal(('verb', 'smack'), parse_verb(word_list))

    # Handle ParserException error
    # First word is a noun
    word_list = [('stop', 'the'),
                 ('noun', 'nose'),
                 ('stop', 'of'),
                 ('stop', 'the'),
                 ('verb', 'princess')]

    assert_raises(ParserException, parse_verb, word_list)

    # This sentence doesn't make any sense
    BrokenWordList = [('THE', 'DIRECTION')]
    assert_raises(ParserException, parse_verb, BrokenWordList)

def test_parse_object():
    # It'll work now
    word_list = [('stop', 'the'),
                 ('noun', 'nose')]
    assert_equal(word_list[1], parse_object(word_list))

    # Test handling errors + removing stops correctly
    word_list = [('stop', 'the'),
                 ('verb', 'smack')]
    assert_raises(ParserException, parse_object, word_list)


def test_parse_subject():
    word_list = [('noun', 'princess'),
                 ('verb', 'go'),
                 ('direction', 'right')]
    assert_equal(word_list[0], parse_subject(word_list))

    # Testing handling errors
    word_list = [('stop', 'the'),
                 ('direction', 'south')]
    assert_raises(ParserException, parse_subject, word_list)

def test_parse_sentence():
    # Wrong sentence
    assert_raises(ParserException, parse_sentence, ([('noun', 'The'),
                                                     ('noun', 'door'),
                                                     ('verb', 'open')]))

    # I used here lexicon and parser
    word_list = scan("smack the nose in cabinet")
    assert_equal([('verb', 'smack'),
                  ('stop', 'the'),
                  ('noun', 'nose'),
                  ('stop', 'in'),
                  ('noun', 'cabinet')], word_list)

    parsed_sentence = parse_sentence(word_list)
    scanned_word_list = scan(' '.join((parsed_sentence.subject,
                                       parsed_sentence.verb,
                                       parsed_sentence.object)))

    sentence = Sentence(scanned_word_list[0],
                        scanned_word_list[1],
                        scanned_word_list[2])

    assert_equal((sentence.subject,
                  sentence.verb,
                  sentence.object),

                 (parsed_sentence.subject,
                  parsed_sentence.verb,
                  parsed_sentence.object))


# Uncomment to start testing

"""
test_peek()
test_match()
test_skip()
test_parse_verb()
test_parse_object()
test_parse_subject()
test_parse_sentence()
"""

# Exercise 49. Done!