
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Error occured ')
    sys.exit(1)




#value: input value which has to be circularly shifted left
#n: number of positions to shift
#Return value: result after circularly left shifting input value
def circular_left_shift(value, n) :
    num_bits_in_int = 32
    n = n % num_bits_in_int
    mask = (1 << num_bits_in_int) - 1
    result = (value << n) | (value >> (num_bits_in_int - n))
    result = result & mask
    return result


#value: input value which has to be circularly shifted right
#n: number of positions to shift
#Return value: result after circularly right shifting input
def circular_right_shift(value, n) :
    num_bits_in_int = 32
    n = n % num_bits_in_int
    mask = (1 << num_bits_in_int) - 1
    result = (value >> n) | (value << (num_bits_in_int - n))
    result = result & mask
    return result




if (__name__ == '__main__'):

    result = circular_right_shift(0x1, 1)
    if (result != 0x80000000):
        handle_error()


    result = circular_right_shift(0xFEDCBA98, 32)
    if (result != 0xFEDCBA98):
        handle_error()

    result = circular_right_shift(0xFEDCBA98, 16)
    if (result != 0xBA98FEDC):
        handle_error()


    result = circular_left_shift(0x1, 0x80000000)
    if (result != 1):
        handle_error()


    result = circular_left_shift(0xFEDCBA98, 32)
    if (result != 0xFEDCBA98):
        handle_error()

    result = circular_left_shift(0xFEDCBA98, 16)
    if (result != 0xBA98FEDC):
        handle_error()


    print('Test passed ')




