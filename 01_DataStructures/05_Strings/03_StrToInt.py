
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Test failed')
    sys.exit(1)

#str1: string to be converted to integer
#result: integer value of string
def str_to_int(str1):
    result = 0
    count = 0
    is_negative = False

    for c in str1:
        if (c == '-' and count == 0):
            is_negative = True

        if ('0' <= c and c <= '9'):
            result = (result * 10) + (ord(c) - ord('0'))

        count += 1

    if (is_negative):
        result = -1 * result 
        
    return result


def test(str1, expected_result):
    result = str_to_int(str1)

    print('{} => {}'.format(str1, result))

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    test('-47', -47)
    test('987', 987)
    test('', 0)
    
    print('Test passed')
