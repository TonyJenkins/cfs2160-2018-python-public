"""
    Sample code for reading a number, and checking that it's an integer.
"""

while 1:
    try:
        number = int (input ('Enter a positive integer: '))
        if number > 0:
            break
        print ('Positive integer, please.')
    except ValueError:
        print ('Enter an integer, dammit.')

print ('The number you entered was', number)
