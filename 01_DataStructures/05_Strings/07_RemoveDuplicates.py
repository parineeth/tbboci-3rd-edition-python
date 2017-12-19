
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

NUM_CHARACTERS = 256


def handle_error() :
    print('Test failed')
    sys.exit(1)




#str1: input string from which duplicate characters should be removed
#Returns: output string which doesn't contain any duplicates
def remove_duplicates(str1) :
    if (not str1):
        return str1

    result = []
    was_char_observed = [False] * NUM_CHARACTERS #NUM_CHARACTERS is 256

    for  c in str1:
        #Only if the current character was not observed so far, add the 
        #current character to fill position and advance the fill position   
        if (not was_char_observed[ord(c)]) :
            result.append(c)

        was_char_observed[ord(c)] = True
    
    #convert list to string
    return ''.join(result)



def test(str1, expected_result) :
    print(str1, end='')

    result = remove_duplicates(str1)

    print(' => ' + result)

    if (result != expected_result):
        handle_error()




if (__name__ == '__main__'):
    test('', '')
    test('a', 'a')
    test('1aaaaaa2bbbaaaaa3cccccaaaabbb', '1a2b3c')
    print('Test passed')



