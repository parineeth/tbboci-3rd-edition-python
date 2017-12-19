
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Error occured ')
    sys.exit(1)



#x, y: two integers, x > 0, y >= 0
#Return value: x multiplied with itself y times
def power(x, y) :
    result = 1
    while (y > 0) :
        #look at the least significant bit of y
        if ((y & 0x1) == 0x1) :
            result = result * x
        y = y >> 1 #shift out the least significant bit of y
        x = x * x
    
    return result




def brute_force_power(x, y) :
    result = 1

    for  i in range(y):
        result = result * x
    

    return result




if (__name__ == '__main__'):

    for  x in range(2, 11):

        #Based on the value of x determine the maximum y value so that
        #x ^ y  does not overflow
        if (x == 2) :
            max_y = 30
        elif (x == 3):
            max_y = 18
        elif (x == 4):
            max_y = 15
        elif (x == 5):
            max_y = 12
        elif (x == 6):
            max_y = 11
        elif (x == 7):
            max_y = 10
        elif (x == 8):
            max_y = 10
        elif (x == 9):
            max_y = 9
        else  :
            max_y = 8
    

        for  y in range(max_y + 1):
            optimal_result = power(x, y)

            print('{} ^ {} = {}'.format(x, y, optimal_result) )

            brute_force_result = brute_force_power(x, y)

            if (optimal_result != brute_force_result) :
                handle_error()
        
    


    print('Test passed ')





