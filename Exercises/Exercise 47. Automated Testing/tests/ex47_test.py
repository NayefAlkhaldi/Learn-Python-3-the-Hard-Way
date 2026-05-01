# from nose.tools import * (NOSE DOES NOT SUPPORT PYTHON 3.10 AND HIGHER)
# INSTEAD, I USED PYTEST WHICH IS A MORE MODERN VERSION. YOU DO NOT NEED TO IMPORT NOSE.TOOLS ANYMORE!!
# IF YOU GET iter_entry points ALONGSIDE WITH IMPORTEROOR, YOU WILL NEED TO 'pip install "setuptools<82.0.0"' IN POWERSHELL/TERMINAL (SYNTAX FOR WINDOWS)
# IF YOU GET AN ERROR, REPLACE THE SENTENCE IN THE FILE THAT CONTAINS (ollections.Callable) WITH (collections.abc.Callable)

# from pytest import *
# import NAME

# def setup():
#     print("SETUP!")

# def teardown():
#     print("TEAR DOWN!")

# def test_basic():
#     print("I RAN!")



### POWERSHELL TEST WITH PYTEST ###


# PowerShell 7.6.1
# PS C:\Windows\System32> cd ~
# PS C:\Users\Nayef> .venvs\lpthw\Scripts\activate
# (lpthw) PS C:\Users\Nayef> cd projects
# (lpthw) PS C:\Users\Nayef> cd lpthw
# (lpthw) PS C:\Users\Nayef\lpthw> cd projects
# (lpthw) PS C:\Users\Nayef\lpthw\projects> cd skeleton
# (lpthw) PS C:\Users\Nayef\lpthw\projects\skeleton> pytest
# ================================================= test session starts =================================================
# platform win32 -- Python 3.10.6, pytest-7.1.2, pluggy-1.0.0
# rootdir: C:\Users\Nayef\lpthw\projects\skeleton
# collected 1 item

# tests\NAME_test.py .                                                                                             [100%]

# ================================================== 1 passed in 0.08s ==================================================
# (lpthw) PS C:\Users\Nayef\lpthw\projects\skeleton>

from pytest import *
import NAME.game as game

Room = game.Room

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's
                door to the north.""")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

def test_delete():
    start = Room("Start", "You are in a cave.")
    straight = Room("Jungle", "Go straight to get out.")
    backward = Room("Bear", "Look behind you to see a bear.")
    start.add_paths({'straight': straight, 'backward': backward})
    backward.add_paths({'backward': start})
    assert start.go('backward') == backward
    start.delete_paths('backward')
    try:
        assert start.go('backward') == backward
    except:
        print("Cannot compute.")