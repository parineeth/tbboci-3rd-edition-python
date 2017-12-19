
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



MAX_INT = 1000000

def handle_error() :
    print('Test failed ')
    sys.exit(1)






#a: a[i] contains the maximum number of locations we can jump from position i
#   list a should have at least 1 element
#Return value: minimum number of jumps needed to reach the end of the list
def find_min_jumps(a) :
    n = len(a)
    min_jumps = [MAX_INT] * n

    #Since we start from location 0, the number of jumps needed to 
    #reach it is 0
    min_jumps[0] = 0

    for  i in range(1, n):
        #Compute the minimum number of jumps to reach location i by looking
        #at the previous locations 0 to i - 1
        for  j in range(i):
            if (j + a[j] >= i and min_jumps[j] + 1 < min_jumps[i]) :
                min_jumps[i] = min_jumps[j] + 1
            
    return min_jumps[n-1]







def test() :
    a = [2, 0, 2, 3, 1, 4, 2, 1, 2, 1]

    print('Input: ', end='')
    print(a)

    result = find_min_jumps(a)
    expected_result = 4

    print('Minimum jumps = {}'.format(result) )

    if (result != expected_result):
        handle_error()

    print('')  



if (__name__ == '__main__'):
    test()
    print('Test passed')



