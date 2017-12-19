
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



#str1: input string
#Returns: True if there is at least one permutation of string str1 which is 
#   a palindrome, False otherwise
def is_permutation_palindrome(str1) :
    count = [0] * NUM_CHARACTERS

    #Find out how many times a character appears in the string
    for c in str1:
        count[ord(c)] += 1

    num_odd_char = 0
    for  cur_count in count:
        if (cur_count % 2 == 1):
            num_odd_char += 1

        #If there are 2 or more characters that appear odd number 
        #of times, then we can't form a palindrome with any permutation
        #of the string 
        if (num_odd_char >= 2):
            return False
    
    return True



def test(str1, expected_result) :

    result = is_permutation_palindrome(str1)

    if (result):
        print('Permutation of ' + str1 + ' is a palindrome')
    else:
        print('Permutation of ' + str1 + ' is NOT a palindrome')

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    test('elelv', True) #level is a palindrome 
    test('ab', False)

    print('Test passed')



