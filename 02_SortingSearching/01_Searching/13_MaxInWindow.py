
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

from collections import deque


MAX_NUM_STACK_ELEMS = 100
MAX_VALUE = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)




def compare(result, expected) :
    if (result != expected) :
        handle_error()
    

def peekleft(dq):
    result = dq.popleft()
    dq.appendleft(result)
    return result

def peek(dq):
    result = dq.pop()
    dq.append(result)
    return result


#a: list for which we have to find the maximum in every window of size k
#k: size of the window
#dq: double ended queue that stores list indices
#Return value: list that contains the result (maximum in every window of size k)
def find_window_max(a, k, dq) :
    result = []
    for  i in range(len(a)):
        #Remove the elements outside the current window from 
        #front of dequeue
        while (len(dq) > 0 and (peekleft(dq) + k <= i)):
            dq.popleft()

        #Remove all elements that are smaller than or equal to current
        #element from the rear of the dequeue
        while (len(dq) > 0 and a[i] >= a[peek(dq)] ):
            dq.pop()

        #Push the index of the current element into the end of dequeue
        dq.append(i)

        if (i >= k-1) :
            #Front of dequeue has index of maximum element for the
            #current window
            pos = peekleft(dq)
            result.append(a[pos])

    return result
    




def test01() :
    a = [2, -1, 4, 3, 2, 6, 0, 7, 8, 10, 3, 2]
    expected1 = [2, -1, 4, 3, 2, 6, 0, 7, 8, 10, 3, 2]
    expected2 = [2, 4, 4, 3, 6, 6, 7, 8, 10, 10, 3]
    expected3 = [4, 4, 4, 6, 6, 7, 8, 10, 10, 10]
    dq = deque()

    print(  'Input                  : ', end='')
    print(a)

    for  k in range(1, 4):
        result = find_window_max(a, k, dq)

        print('Max in window of size {}: '.format(k) , end='')
        print(result)

        if (k == 1):
            compare(result, expected1)
        elif (k == 2):
            compare(result, expected2)
        elif (k == 3):
            compare(result, expected3) 
    





if (__name__ == '__main__'):
    test01()
    print('Test passed')



