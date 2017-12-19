
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function


import sys



def handle_error() :
    print('Test failed')
    sys.exit(1)

#writes the bit_value (0/1) into position pos in x and returns the result
def write_bit(x, bit_value, pos):
    mask = 1 << pos
    if (bit_value == 1):
        x = x | mask
    else:
        x = x & ~mask

    return x

#x: integer in which the bits should be swapped
#pos1: position of first bit to be swapped
#pos2: position of the second bit to be swapped
def swap_bits(x, pos1, pos2):
    #get the bits at position pos1 and pos2
    bit1 = (x >> pos1) & 1
    bit2 = (x >> pos2) & 1

    #swap the bits
    if (bit1 != bit2) :
        x = write_bit(x, bit1, pos2)
        x = write_bit(x, bit2, pos1)

    return x


def test(x, pos1, pos2, expected_result):

    result = swap_bits(x, pos1, pos2)

    print('Swapping bit {} and bit {} on  + hex(x) =  + hex(result)'.format(pos1, pos2) )

    if (result != expected_result):
        handle_error()


if (__name__ == '__main__'):
    test(0xB, 1, 2, 0xD)
    print('Test passed')
  
