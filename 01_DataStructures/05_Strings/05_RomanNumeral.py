
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print(  'Error occured ')
    sys.exit(1)


 
#str1: valid input string with Roman alphabets
#Return value: integer equivalent of the Roman string
def roman_to_int(str1) :
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    i = len(str1) - 1 #Process the string from the rear
    if (i < 0):
        return 0

    result = table[str1[i]]
    i -= 1
    while (i >= 0) :
        cur_digit_val = table[str1[i]]
        next_digit_val = table[str1[i+1]]
        if (cur_digit_val < next_digit_val):
            result -= cur_digit_val
        else:
            result += cur_digit_val     
        i -= 1
    
    return result






def test(s1, expected_result) :
    result = roman_to_int(s1)

    print('{}  =>  {}'.format(s1, result))

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__')  :
    test('MMCX', 2110)
    test('MMXC', 2090)
    test('LIX', 59)
    test('LVIIII', 59)
    test('X', 10)
    test('', 0)

    print(  'Test passed ')



