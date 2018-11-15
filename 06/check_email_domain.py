#!/usr/bin/env python3

"""
   Check if an email address looks valid.
"""

__author__    = "Tony Jenkins"
__email__     = "tony.jenkins@elder-studios.co.uk"
__date__      = "2018-11-15"

def valid_email (email, domain):

    if email.count ('@') != 1:
        return False

    if email [0] == '@':
        return False

    if email [(email.find ('@') + 1):] != domain:
        return False

    return True

if __name__ == '__main__':
    print (valid_email ("fred@pop.ac.uk", "pop.ac.uk"))
    print (valid_email ("fredpop.ac.uk", "pop.ac.uk"))
    print (valid_email ("fred@pop.ac.uk", "pop.co.uk"))
