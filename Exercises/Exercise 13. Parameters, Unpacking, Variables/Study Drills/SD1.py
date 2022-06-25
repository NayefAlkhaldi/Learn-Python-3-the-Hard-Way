# Ok I'll try it

# PowerShell 7.2.4
# Copyright (c) Microsoft Corporation.

# https://aka.ms/powershell
# Type 'help' to get help.

# PS C:\Windows\System32> cd ~
# PS C:\Users\Nayef> cd Downloads
# PS C:\Users\Nayef\Downloads> python3.10 ex13.py stuff things
# Traceback (most recent call last):
#   File "C:\Users\Nayef\Downloads\ex13.py", line 3, in <module>
#     script, first, second, third = argv
# ValueError: not enough values to unpack (expected 4, got 3)
# PS C:\Users\Nayef\Downloads>

# It's easy, that happend because argument variable given must be 3 (script is the file name).
# It won't work if we give it 2 variables