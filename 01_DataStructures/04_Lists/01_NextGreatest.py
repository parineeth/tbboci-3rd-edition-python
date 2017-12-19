
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function


import sys
import random



MAX_NUM_ITEMS  = 10
MAX_VALUE = 100
INVALID_NUMBER = -1


def handle_error() :
    print('Test failed')
    sys.exit(1)
    


#a: non-empty list in which each element should be replaced with next greatest
def replace_with_next_greatest(a) :
    n = len(a)

    next_greatest = a[n-1]
    a[n-1] = INVALID_NUMBER  

    #Process the list from the back
    for i in range(n-2, -1, -1) :
        temp = a[i]

        a[i] = next_greatest

        if (temp > next_greatest):
            next_greatest = temp
    




def test_01() :

    #Choose a random number of elements
    n = random.randint(1, MAX_NUM_ITEMS)

    #Generate n random values and store them in lists a and b
    a = [random.randint(1, MAX_VALUE) for i in range(n)]
    
    b = a[:] #copy contents of a into b
    

    print('Input: ', end=' ')
    print(a)

    #Replace with next greatest using the efficient algorithm. The result will be in list a
    replace_with_next_greatest(a)

    #Replace with next greatest using brute force approach. The result will be in list b
    for i in range(n - 1) :
        current_max = 0
        for j in range(i + 1, n) :
            if (b[j] > current_max):
                current_max = b[j]
        
        b[i] = current_max
    
    b[n - 1] = -1

    print('Output: ', end=' ')
    print(a)

    #Compare the efficient algorithm result with the brute force approach
    if (a == b):
        pass
    else:
        handle_error()
    


    
if (__name__ == '__main__'):
    for i in range(10):
        test_01()
        print('__________________________________')

    print('Test passed')
    



