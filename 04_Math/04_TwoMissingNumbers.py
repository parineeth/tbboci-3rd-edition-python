
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import math


def handle_error() :
    print('Test failed')
    sys.exit(1)


#values: list of unique numbers. A number can have a value between 1 to n
#n: maximum value in the list is n. list has n-2 elements
#Return value: the missing elements in the list are returned 
def find_missing(values, n) :
    #Since 2 elements are missing, there are only n-2 elements in the list
    actual_normal_sum = 0
    actual_square_sum = 0
    for  i in range(n - 2):
        actual_normal_sum += values[i]
        actual_square_sum += values[i] * values[i]
    

    expected_normal_sum = n * (n+1) // 2
    expected_square_sum = n * (n+1) * (2*n + 1) // 6

    a_plus_b = expected_normal_sum - actual_normal_sum
    a_square_plus_b_square = (expected_square_sum - actual_square_sum)
    two_a_b =  ((a_plus_b * a_plus_b) - a_square_plus_b_square)
    a_minus_b = int (math.sqrt(a_square_plus_b_square - two_a_b))

    a = (a_plus_b + a_minus_b) // 2
    b = (a_plus_b - a)
     
    return a, b



def test() :
    values = [1, 3, 4, 6, 7, 8, 9, 10]
    length = 8 #Number of elements in the list
    result = [0] * 2

    print('Input : ', end='')
    print(values)

    result[0], result[1] = find_missing(values, length+2)

    print('Missing elements are = {} and {}'.format(result[0], result[1]) )

    if ( (result[0] == 2 and result[1] == 5) or
        (result[0] == 5 and result[1] == 2) ) :
        #Do nothing
        pass
    else :
        handle_error()
    




if (__name__ == '__main__'):
    test()
    print('Test passed ')



