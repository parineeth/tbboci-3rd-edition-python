
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys


def handle_error() :
    print('Test failed')
    sys.exit(1)



#str1 and str2 are the two strings which need to be checked
#Return value: True if the strings are rotations of each other, False otherwise
def is_string_rotation(str1, str2) :
    #If lengths of two strings are not equal, then they can't be rotations
    if (len(str1) != len(str2)):
        return False

    str3 = str1 + str1

    #find returns -1 if it can't find str2 in str3
    result = str3.find(str2)

    is_rotation = True
    if (result == -1):
        is_rotation = False

    return is_rotation



def test(str1, str2, expected_result) :
    result = is_string_rotation(str1, str2)

    print(str1 + ' and ' + str2, end='')
    if (result):
        print(' are rotations of each other')
    else :
        print(' are NOT rotations of each other')


    if (result != expected_result):
        handle_error()




if (__name__ == '__main__'):
    test('', '', True)
    test('ABCDE', 'CDEAB', True)
    test('ABCDE', 'EABCD', True)
    test('AAA', 'AAB', False)

    print('Test passed ')



