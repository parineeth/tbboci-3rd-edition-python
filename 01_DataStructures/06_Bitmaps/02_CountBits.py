
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Error occured ')
    sys.exit(1)



#Returns the number of bits set to 1 in n
def count_num_bits_set(n) :
    count = 0

    while (n != 0) :
        n &= n - 1
        count += 1
    
    return count






if (__name__ == '__main__'):
    num_bits_set = count_num_bits_set(0)
    if (num_bits_set != 0):
        handle_error()

    num_bits_set = count_num_bits_set(0xffffffff)
    if (num_bits_set != 32):
        handle_error()


    num_bits_set = count_num_bits_set(0x70ff00f)
    if (num_bits_set != 15):
        handle_error()

    print('Test passed')




