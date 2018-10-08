"""
    Sample code for reading a number, and checking that it's an integer.
"""

while 1:
    try:
        number = int (input ('Enter a positive integer: '))
        if number > 0:
            break
        else:
            print ('Positive number, please.')
    except ValueError:
        print ('Enter a number, dammit.')

print ('The number you entered was', number)