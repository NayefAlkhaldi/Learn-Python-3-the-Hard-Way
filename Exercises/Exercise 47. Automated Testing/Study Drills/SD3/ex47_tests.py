from nose.tools import *
from game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees,", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_remove_paths():
    gold_room = Room("Gold Room", "This room has gold in it. Grab some.")
    win = Room("Win", 'You win!')
    death = Room("Death", "You died!")

    gold_room.add_paths({'take all': death, 'take some': win})
    gold_room.remove_paths('take some')

    assert_equal(len(gold_room.paths), 1)
    assert_equal(gold_room.go('take some'), None)

def test_correct_paths():
    dark_room = Room("Dark room", "You can't see anything here.")
    win = Room("Win", 'You win!')
    death = Room("Death", "You died!")

    dark_room.add_paths({'Turn on the light': death, 'Search for hidden doors': win})
    correct_paths = dark_room.correct_paths(death)

    assert_equal(dark_room.go(correct_paths[0]), win)
    
test_correct_paths()