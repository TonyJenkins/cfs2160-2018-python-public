#!/usr/bin/env python3

"""
    Process five student marks to find the average.

    Display average along with the student's name.
"""

__author__  = "Tony Jenkins"
__email__   = "tony.jenkins@elder-studios.co.uk"
__date__    = "2018-09-30"
__license__ = "Unlicense"

NUMBER_OF_MARKS = 5

name = input ("Enter the student's name: ")

total_marks = 0
for count in range (NUMBER_OF_MARKS):
    while 1:
        try:
            total_marks += int (input ('Enter result #' + str (count + 1) + ': '))
            break
        except ValueError:
            print ('Please enter a number.')

average_mark = total_marks / NUMBER_OF_MARKS

print ()
print ('Final Mark for {} is {:.2f}.'.format (name, average_mark))
