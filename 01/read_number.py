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
        print ('Please enter an integer.')

print ('The number you entered was', number)
