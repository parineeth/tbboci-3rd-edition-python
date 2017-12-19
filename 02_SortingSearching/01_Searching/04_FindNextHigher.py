
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100
MAX_INT = 999999

def handle_error() :
    print('Test failed')
    sys.exit(1)



#a: sorted list containing elements in non-decreasing order
#k: we are searching for the number immediately above k
#Returns: the number immediately greater than k in the list if it exists,
#       MAX_INT otherwise
def find_next_higher(a, k) :
    low = 0 
    high = len(a) - 1

    result = MAX_INT
    while (low <= high) :
        mid = (low + high) // 2

        if (a[mid] > k) :
            result = a[mid] #update the result and continue
            high = mid - 1
        else :
            low = mid + 1

    return result




def test() :

    #Randomly decide the number of elements
    length = random.randint(1, MAX_NUM_ELEMS)

    #Generate a list having random elements
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]

    #Sort the list in ascending order
    a.sort()

    print ('Input : ', end='')
    print(a)

    #choose a random element k in the list
    pos = random.randint(0, length - 1)
    k = a[pos]

    #Find the next higher element after k using binary search
    result = find_next_higher(a, k)

    print('Next element greater than {} is {}'.format(k, result) )

    #Find the next higher element after k using linear search
    expected_result = MAX_INT
    for  i in range(pos + 1, length):
        if (a[i] > k) :
            expected_result = a[i]
            break
                
    

    #The linear search and binary search results should match
    if (result != expected_result):
        handle_error()

    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed ')



