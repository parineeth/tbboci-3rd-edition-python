
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Error occured ')
    sys.exit(1)


#a, b: the two input integers
#Return value: Number of bits that have different values in a and b
def count_different_bits( a,  b) :
    c = a ^ b
    count = 0

    #Since c = a xor b, the positions where a and b are different will 
    #be set to 1 in c. So by counting the number of 1's in c, we will get the
    #number of bits that are different between a and b
    while (c != 0) :
        count += 1
        c = c & (c - 1)
    
    return count




if (__name__ == '__main__'):
    a = 0xF0F
    b = 0x0F0
    result = count_different_bits(a, b)
    if (result != 12):
        handle_error()

    a = 4
    b = 5
    result = count_different_bits(a, b)
    if (result != 1):
        handle_error()


    print('Test passed')




