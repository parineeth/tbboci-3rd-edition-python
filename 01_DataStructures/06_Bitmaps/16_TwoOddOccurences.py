
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function


import sys



def handle_error() :
    print('Test failed')
    sys.exit(1)

#a: input list where 2 elements occur odd number of times and the remaining
#   occur even number of times
#Return value: the two numbers that occur odd number of times
def find_odd_occurrences(a):
    #XOR all the values
    all_xor = 0
    for val in a:
        all_xor = all_xor ^ val

    #Find the first bit in the XOR result that is set to 1. The two odd 
    #occuring numbers will differ at this bit position. So if difference 
    #is at bit position 3, then mask will be ...00001000 
    mask = all_xor & ~(all_xor - 1)

    #Separate out values in list a such that, values that have a 1 at the
    #different bit will be XORed with x and values that have a 0 at the 
    #different bit will be XORed with y 
    x = y = 0
    for val in a:
        if ( (val & mask) != 0):
            x = x ^ val
        else:
            y = y ^ val

    #x and y will now contain the two numbers that occur odd number of times
    return x, y


def test(a, expected_result1, expected_result2):
    print(a)

    result1, result2 = find_odd_occurrences(a)

    print('The odd occuring elements are {}, {}'.format(result1, result2) )

    if (min(result1, result2) != min(expected_result1, expected_result2)):
        handle_error()

    if (max(result1, result2) != max(expected_result1, expected_result2)):
        handle_error()

    print('_____________________________________________')


if (__name__ == '__main__'):
    a = [1, 2, 3, 2, 4, 3]
    test(a, 1, 4)
    print('Test passed')
      
