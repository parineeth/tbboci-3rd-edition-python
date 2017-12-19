
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_VALUE = 1000
MAX_NUM_TESTS = 100

def handle_error() :
    print('Error occured ')
    sys.exit(1)



#x, y: two integers >= 0
#Return value: x multiplied with y 
def multiply(x, y) :
    result = 0
    while (y != 0) :
        #if the least significant bit of y is 1, then add x to result
        if ( (y & 1) == 1) :
            result += x
        
        y = y >> 1 #shift out the least significant bit of y
        x = x << 1 #double the value of x
    
    return result





def test() :

    x = random.randint(0, MAX_VALUE)
    y = random.randint(0, MAX_VALUE)

    result = multiply(x, y)

    print('{}*{} = {}'.format(x, y, result) )

    if (result != (x * y) ) :
        handle_error()
    





if (__name__ == '__main__'):
    for  test_nr in range(MAX_NUM_TESTS):
        test()

    print('Test passed ')




