
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Test failed')
    sys.exit(1)


#str1: string in which the number of words have to be counted
#Return value: number of words in the string
def count_words(str1) :
    if (not str1):
        return 0

    num_words = 0
    is_prev_char_alphabet = False
    for c in str1 :
        is_cur_char_alphabet = c.isalpha()

        #If previous character is not an alphabet and current character is 
        #an alphabet then we have found a new word
        if (not is_prev_char_alphabet and is_cur_char_alphabet) :
            num_words += 1
        
        is_prev_char_alphabet = is_cur_char_alphabet
    
    return num_words



def test(s1, expected_result) :
    result = count_words(s1)

    if (result != expected_result):
        handle_error()

    print('Word count = {}, for string: {}'.format(result, s1) )



if (__name__ == '__main__'):
    expected_word_count = 1
    test('hello', expected_word_count)

    expected_word_count = 0
    test('', expected_word_count)

    expected_word_count = 5
    test('   hello,how are    you doing?', expected_word_count)

    print('Test passed')



