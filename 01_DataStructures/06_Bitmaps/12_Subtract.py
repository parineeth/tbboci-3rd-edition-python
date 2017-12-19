
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Test failed')
    sys.exit(1)



#Returns the sum bit and carry bit on adding the bits a,b
def compute_sum(a, b):
    return a ^ b, a & b 


#x, y: two integers, can be negative. x may be bigger, equal or smaller than y
#   Maximum value of x and y should not exceed 31 bits
#Return value: x + y using bit wise operators
def add(x, y) :
    result = 0
    carry_bit = 0
    #x and y can be represented within 32 bits in 2's complement format
    for cur_pos in range(32) :
        #extract the last bit of x and y
        x_last_bit = x & 1
        y_last_bit = y & 1

        #compute the sum of last bit of x and y 
        sum_bit, carry_1 = compute_sum(x_last_bit, y_last_bit)

        #now add the carry_bit to the sum_bit
        sum_bit, carry_2 = compute_sum(sum_bit, carry_bit)

        #compute the carry bit for the next bit position
        carry_bit = carry_1 | carry_2

        #store the sum bit at cur_pos in the result
        result = result | (sum_bit << cur_pos)

        #shift out the last bit of x and y
        x = x >> 1      
        y = y >> 1

    #Python doesn't have an upper limit on the number of bits in an integer. 
    #So if the result of addition is negative, we have to do the sign 
    #extension. Since we are dealing with only 32 bit integers, bit 31 will 
    #serve as the sign bit. If the sign bit is 1, then it means the result 
    #is negative.  
    if (result & (1 << 31)):
        #Propagate the negative sign bit. (~0) will give a continuous 
        #set of 1's. Then stitch in the 32 bit result into the continuous
        #set of 1's 
        result = ((~0) << 32) | result
    
    return result



#x, y: two integers, can be negative. x may be bigger, equal or smaller than y
#   Maximum value of x and y should not exceed 31 bits
#Return value: x - y using bit wise operators
def subtract(x, y):
    #Find the 2's complement of y
    y = (~y) + 1

    #Add the 2's complement of y to x. This will give us x - y
    result = add(x, y)

    return result


def test(x, y) :
    result = subtract(x, y)

    print('{} - {} = {}'.format(x, y, result) )

    #Verify the result
    if (result != (x - y)):
        handle_error()



if (__name__ == '__main__'):
    test(20, 13)

    test(20, 20)

    test(78, 100)

    test(50, -7)

    test(-8, 17)

    test(-8, -17)

    test(-25, -25)


    print('Test passed')







