
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import math




def handle_error() :
    print('Error occured ')
    sys.exit(1)




#n: number >= 1 whose square root has to be computed
#accuracy: how accurate should the result be
#Return value: square root of n
def find_sqrt(n, accuracy)  :
    low = 1.0
    high = n * 1.0

    if (n == 1):
        return 1.0

    mid = (low + high) / 2

    while (low < high) :
        square = mid * mid

        #Find absolute difference between (mid * mid) and n
        difference =  square - n
        if (difference < 0):
            difference = difference * -1
    
        #If the absolute difference is within the required accuracy
        #then mid contains the square root. So break out of the loop
        if (difference < accuracy):
            break
        
        if (square > n) :
            high = mid
        else:
            low = mid

        mid = (low + high) / 2

        
    return mid #Return the square root




if (__name__ == '__main__'):
    for  i in range(1, 1000):

        computed_sqrt = find_sqrt(i, 0.001)

        print('Square root of {} = {}'.format(i, computed_sqrt) )

        expected_sqrt = math.sqrt(i)

        difference = abs(computed_sqrt - expected_sqrt)

        if (difference > 0.1) :
            handle_error()



    print('Test passed ')






