
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





#str1, str2: the two strings which we want to compare
#Return value: True if the two strings are anagrams, False otherwise
def are_anagrams(str1, str2) :
    count1 = [0] * NUM_CHARACTERS #NUM_CHARACTERS is 256
    count2 = [0] * NUM_CHARACTERS

    #Compute the character counts for str1 and str2
    for  c in str1:
        count1[ord(c)] += 1
    
    for  c in str2:
        count2[ord(c)] += 1
    
    #Compare the counts
    is_anagram = True
    if (count1 != count2):
        is_anagram = False
        
    return is_anagram


def test(s1, s2, expected_result) :
    result = are_anagrams(s1, s2)

    print(s1 + ' and ' + s2 + ' are ', end='')
    if (result):
        print('anagrams')
    else:
        print('not anagrams')

    if (result != expected_result) :
        handle_error()
    
    

if (__name__ == '__main__'):
    test('ABCDE', 'CDBAE', True)
    test('AAAAA', 'BBBBB', False)

    print('Test passed ')




