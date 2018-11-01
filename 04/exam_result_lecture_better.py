#!/usr/bin/env python3

"""
    Process five student marks to find the average.

    Display average along with the student's name.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__date__    = "2018-09-30"
__license__ = "Unlicense"

NUMBER_OF_MARKS = 8

name = input ('Enter the student\'s name: ')

mark_list = []

for mark in range (NUMBER_OF_MARKS):
    while 1:
        try:
            next_mark = int (input ('Enter the next mark: '))
            if next_mark in range (0, 101):
                mark_list.append (next_mark)
                break
            else:
                print('Out of range. Ignoring...')
        except ValueError:
            print ('Please enter an integer.')

average_mark = sum (mark_list) / len (mark_list)

print ()
print ('Final Mark for ' + name + ' is ' + str (average_mark) + '.')
