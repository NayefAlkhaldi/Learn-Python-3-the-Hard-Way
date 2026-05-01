# from nose.tools import * (NOSE DOES NOT SUPPORT PYTHON 3.10 AND HIGHER)
# INSTEAD, I USED PYTEST WHICH IS A MORE MODERN VERSION. YOU DO NOT NEED TO IMPORT NOSE.TOOLS ANYMORE!!
# IF YOU GET iter_entry points ALONGSIDE WITH IMPORTEROOR, YOU WILL NEED TO 'pip install "setuptools<82.0.0"' IN POWERSHELL/TERMINAL (SYNTAX FOR WINDOWS)
# IF YOU GET AN ERROR, REPLACE THE SENTENCE IN THE FILE THAT CONTAINS (ollections.Callable) WITH (collections.abc.Callable)

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")



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