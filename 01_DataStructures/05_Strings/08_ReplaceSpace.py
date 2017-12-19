
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys


def handle_error() :
    print('Test failed')
    sys.exit(1)


#str1: input string
#Return value: string where spaces in input string are replaces with %20
def replace_space(str1) :
    #Count the number of spaces
    num_spaces = 0
    for c in str1:
        if (c == ' '):
            num_spaces += 1

    new_length = len(str1) + (2 * num_spaces)

    #Since result will be longer, create a bigger list
    result = [' '] * new_length

    #Keep copying characters from rear of original string to fill_pos
    fill_pos = new_length - 1
    for c in reversed(str1) :
        if (c == ' ') :
            result[fill_pos] = '0'
            result[fill_pos - 1] = '2'
            result[fill_pos - 2] = '%'
            fill_pos -= 3
        else :
            result[fill_pos] = c
            fill_pos -= 1
        
    
    #convert the list to a string
    return ''.join(result)




def test(str1, expected_result):
    print(str1, end='')

    result = replace_space(str1)

    print(' =>  ' + result)

    if (result != expected_result):
        handle_error()






if (__name__ == '__main__'):
    test('', '')
    test('a', 'a')
    test(' Hello  how are you ', '%20Hello%20%20how%20are%20you%20')

    print('Test passed')




