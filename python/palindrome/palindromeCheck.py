# Copyright © 2018 byte
#
# Distributed under terms of the MIT license.

"""
Check whether a string is a palindrome
"""

def palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    s = input('Enter a string: ')
    if palindrome(s):
        print("String '%s' is a palindrome"% s)
    else:
        print("String '%s' is not a palindrome"% s)
