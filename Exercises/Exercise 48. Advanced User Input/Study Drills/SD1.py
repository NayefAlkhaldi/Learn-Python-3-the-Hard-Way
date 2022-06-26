from nose.tools import *
import lexicon


def test_symbol_remove():
    word_list = lexicon.scan("bear is @princess.")
    assert_equal(word_list, [('noun', 'bear'), ('stop', 'is'), ('noun', 'princess')])

    word_list = lexicon.scan("(door) and &bear&")
    assert_equal(word_list, [('noun', 'door'), ('stop', 'and'), ('noun', 'bear')])