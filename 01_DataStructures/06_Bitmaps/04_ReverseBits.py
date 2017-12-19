
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 1000


def get_rand_byte() :
    return random.randint(0, 255)   



def handle_error() :
    print('Error occured ')
    sys.exit(1)


#input_value: the integer that has to be reversed
#reverse_table: lookup table that has the reversed values for every byte.
#   Example: reverse_table[0x1] = 0x80, since reverse of 00000001 is 1000000
#Return value:  integer that is the reverse of the input integer
def reverse_integer(input_value,  reverse_table) :
    result = 0
    num_bytes = 4
    for  i in range(num_bytes):
        #Get the least significant byte from the input
        cur_byte_value = input_value & 0xFF
        
        #Left shift the result by 8 and append the reverse of the 
        #least significant byte of input        
        result = (result << 8) | reverse_table[cur_byte_value]

        #Right shift out the least significant byte from the input
        input_value = input_value >> 8
    
    return result


def normal_reverse_integer( input_value) :
    size_in_bits = 32

    result = 0
    j = size_in_bits - 1
    for  i in range(size_in_bits):
        if ( (input_value & (1 << i)) != 0 ) :
            result = result | (1 << j)
        
        j -= 1
    

    return result



def normal_reverse_char(input_value) :
    size_in_bits =  8 

    result = 0
    j = size_in_bits - 1
    for  i in range(size_in_bits):
        if ( (input_value & (1 << i)) != 0) :
            result = (result | (1 << j))
        
        j -= 1
    

    return result



if (__name__ == '__main__'):
    lookup_table = [0] * 256

    for  i in range(256):
        lookup_table[i] = normal_reverse_char(i)


    for  test_nr in range(MAX_NUM_TESTS):
        rand_num =  (get_rand_byte() << 24) | get_rand_byte() << 16 | get_rand_byte() << 8 | get_rand_byte()

        normal_result = normal_reverse_integer(rand_num)

        lookup_result = reverse_integer(rand_num, lookup_table)

        if (normal_result != lookup_result) :
            handle_error()


    rand_num = 0
    if (rand_num != reverse_integer(rand_num, lookup_table)):
        handle_error()

    rand_num = 0xffffffff
    if (rand_num != reverse_integer(rand_num, lookup_table)):
        handle_error()


    print('Test passed')




