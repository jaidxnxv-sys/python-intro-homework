Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\lyons> python
Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(not True and False)
... print(True or False and False)
... print(not (5 > 3))
... print(10 == 10 and 4 != 4)
... print(not False or not True)
...
False
True
False
False
True
>>> print(not True and False) #not true = false, and false is false.
... print(True or False and False) #python picks true from false and false.
... print(not (5 > 3)) #returns fasle because 5 is greater than 3.
... print(10 == 10 and 4 != 4) #prints false because 4 is equal to 4.
... print(not False or not True) #returns true because not false is true.
