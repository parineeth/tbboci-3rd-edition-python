
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





def handle_error() :
    print(  'Error occured ')
    sys.exit(1)


 

#Helper function to print the words present in the string
#str1: input string
#word_start: if the substring from position i to position j of the original 
#   string is a word in dictionary, then word_start[j] will be i
def print_result(str1, word_start) :
    pos = len(str1) - 1
    while (pos >= 0) :
        #The current word ends at pos in the input string and
        #starts at word_start[pos]
        start = word_start[pos] 
        print( str1[start : pos + 1] + ' ', end='')
        pos = word_start[pos] - 1
    


#str1: string that we need to check if it can be broken
#dictionary: permitted words are stored in the dictionary 
#Return value: True if we can break str1 into words in the dictionary
def word_break(str1, dictionary) :
    length = len(str1)

    if (length == 0):
        return False

    #if we can break the string from 0 to pos, then is_break_possible[pos] 
    #will be True
    is_break_possible = [False] * length

    #if the substring from position i to position j of the original string
    #is a word in dictionary, then word_start[j] will be i
    word_start = [-1] * length

    for  i in range(length):
        #Check if the substring from 0 to i is in the dictionary
        temp_str = str1[0:i+1]
        if (not is_break_possible[i] and temp_str in dictionary) :
            is_break_possible[i] = True
            word_start[i] = 0
        
        #If we can break the substring upto i into dictionary words, 
        #then check if all substrings starting from i+1 can be broken 
        #into dictionary words 
        if (is_break_possible[i]) :
            for  j in range(i + 1, length):
                temp_str = str1[i+1:j+1]
                if (not is_break_possible[j] 
                and temp_str in dictionary) :
                    #We can form a word from i+1 to j
                    is_break_possible[j] = True
                    word_start[j] = i+1
                
    #If is_break_possible[length-1] is True, then entire string can be
    #broken into dictionary words. If the word_start[length-1] is 0, then  
    #it means the entire input word is present in the dictionary. But we
    #want a compound word that has 2 or more dictionary words in it.
    #So modify the result condition to check word_start[length-1] != 0
    if (is_break_possible[length-1] and word_start[length-1] != 0): 
        print_result(str1, word_start)
        return True

    return False




def test(str1, expected_result) :

    dictionary = {}
    dictionary['i'] = 1
    dictionary['will'] = 1
    dictionary['play'] = 1
    dictionary['now'] = 1

    print(  str1 + ' => ', end='')

    result = word_break(str1, dictionary)

    print('')

    if (result) :
        print(  str1 + ' can be broken ')
    else :
        print(  str1 + ' cannot be broken ')
    

    if (result != expected_result):
        handle_error()

    print(  '________________________________________')



if (__name__ == '__main__'):
    test('iwilli', True)
    test('iwillplaynow', True)
    test('nowplayiwill', True)
    test('iiiiiiiiiii', True)
    test('iwpn', False)

    print(  'Test passed ')



