
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys






def handle_error() :
    print('Test failed')
    sys.exit(1)


#Returns the maximum of x and y without using if-else and comparison
# Maximum value of x and y should not exceed 31 bits
def find_max(x, y) :
    difference = x - y
    sign_bit = (difference >> 31) & 0x1
    
    #Sign bit can be 0 or 1
    #If sign bit is 0, max = x - (0 * difference) = x
    #If sign bit is 1, max = x - (1 * (x-y)) = x - x + y = y 
    max_value = x  - (sign_bit * difference)
    return max_value




def test(x, y) :
    result = find_max(x, y)

    print('maximum of {}, {} = {}'.format(x, y, result) )

    expected_result = x
    if (x < y): 
        expected_result = y

    if (result != expected_result):
        handle_error()




if (__name__ == '__main__'):
    test(-10, -20)
    test(-10, 20)
    test(10, -20)
    test(10, 20)
    test(0, 10)
    test(0, -20)

    print('Test passed ')



