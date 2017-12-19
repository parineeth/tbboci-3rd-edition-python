
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random


MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)


#a: list being searched
#x: element being searched
#Return value: first position of x in a, if x is absent -1 is returned
def find_first(a, x) :
    start = 0
    end = len(a) - 1

    while (start <= end) :
        mid = (start + end) // 2

        if (a[mid] == x) :
            if (mid == 0 or a[mid - 1] != x):
                 return mid
            else:
                 end = mid - 1

        elif (a[mid] > x) :
            end = mid - 1
        else :
            start = mid + 1
        
    return -1






def print_result(result, x):
    print('The position of first occurence of {} is {}'.format(x, result) )


def test01()    :

    #Number of elements in the list
    n = random.randint(1, MAX_NUM_ELEMS)

    a = [random.randint(0, MAX_VALUE) for  i in range(n)]
    

    a.sort()

    print('Input : ', end='')
    print(a)

    #Search all elements that are present and verify the result 
    for  x in a:
        result = find_first(a, x)

        print_result(result, x)

        #Python index function returns the index of the first occurence of x 
        expected_result = a.index(x)
        if (expected_result != result):
            handle_error()
    



    #Search for a non-existent item. Result should be -1
    x = MAX_VALUE + 1
    result = find_first(a, x)
    print_result(result, x)
    if (result != -1) :
        handle_error()

    print('_____________________________________________')



if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test01()

    print('Test passed')






