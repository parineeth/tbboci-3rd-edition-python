
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



NUM_CHARS = 256

def handle_error() :
    print('Error occured')
    sys.exit(1)


#str1: string to be searched
#Return value: first unique character if it exists, '\0' otherwise
def find_first_unique_char(str1) :
    count = [0] * NUM_CHARS #NUM_CHARS is 256

    #count the number of occurrences of each character
    for  c in str1:
        count[ord(c)] += 1
    

    #traverse str1 and find first character which occurs only once
    first_unique_char = '\0'
    for  c in str1:
        if (count[ord(c)] == 1) :
            first_unique_char = c
            break

    return first_unique_char



def test(str1, expected_result) :
    result = find_first_unique_char(str1)

    print('First unique in \'' + str1 + '\' is ' + result) 

    if (result != expected_result):
        handle_error()




if (__name__ == '__main__'):
    test('aabbbccccddeffffgg', 'e')
    test('abcdefab', 'c')
    test('abab', '\0')

    print('Test passed')



