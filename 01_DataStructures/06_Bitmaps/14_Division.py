
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys






MAX_NUMERATOR = 100
MAX_DENOMINATOR = 20


def handle_error() :
    print('Error occured ')
    sys.exit(1)


#a, b: a is an integer >= 0. b is an integer > 0
#Return values: quotient and remainder 
def integer_division(a, b) :
    max_bit_pos = 31 

    if (b == 0) :
        raise ZeroDivisionError 
    
    quotient = 0
    remainder = 0
    for  i in range(max_bit_pos, -1, -1):
        remainder = remainder << 1 #Double the remainder

        #Find the value of the next bit in the dividend a. 
        #In first iteration, we find value of the Most Significant Bit.
        next_bit = 0
        if ((a & (1 << i)) != 0) :
            next_bit = 1
        
        #Copy the value of the next bit into the least significant 
        #bit of remainder   
        if (next_bit == 1):
            remainder = remainder | 1
    
        #If the remainder is now greater than the divisor b, 
        #then subtract the divisor b from the remainder and 
        #set the appropriate quotient bit
        if (remainder >= b) :
            remainder = remainder - b
            quotient = quotient | (1 << i)
        
    return quotient, remainder




if (__name__ == '__main__'):
    for  a in range(MAX_NUMERATOR):
        for  b in range(1, MAX_DENOMINATOR):
            quotient, remainder = integer_division(a, b)

            print('{} / {} => quotient = {}, remainder = {}  '.format(a, b, quotient, remainder) )

            expected_quotient = a // b
            expected_remainder = a % b

            if (quotient != expected_quotient):
                handle_error()

            if (remainder != expected_remainder) :
                handle_error()
    

    print('Test passed ')






