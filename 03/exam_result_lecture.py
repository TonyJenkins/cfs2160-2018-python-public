#!/usr/bin/env python3

"""
    Process five student marks to find the average.

    Display average along with the student's name.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__date__    = "2018-09-30"
__license__ = "Unlicense"

name = input ('Enter the student\'s name: ')

total_mark = 0

for i in range (5):
    while 1:
        try:
            mark = int (input ('Enter a mark: '))
            total_mark += mark
            break
        except ValueError:
            print ('Enter a number, please')

average_mark = total_mark / 5

print ()
print ('Final Mark for ' + name + ' is ' + str (average_mark))
