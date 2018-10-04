"""
    Sample code for reading a number, and checking that it's an integer.
"""

while 1:
    try:
        number = int (input ('Enter a number: '))
        if number > 0:
            break
    except ValueError:
        print ('Enter a number, dammit.')