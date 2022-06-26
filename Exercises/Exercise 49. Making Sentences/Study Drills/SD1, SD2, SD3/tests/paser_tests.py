from nose.tools import *
from lexicon import *
from parser import *

def test_parse_number():
    parser = Parser()
    word_list = scan("princess age is 17")
    assert_equal(('number', 17), parser.parse_number(word_list))

    # Test errors
    word_list = scan('chef')
    assert_raises(ParserException, parser.parse_number, word_list)


## Uncomment to begin testing
"""

test_parse_number()

"""