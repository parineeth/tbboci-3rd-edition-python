
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random
from heapq import heappush, heappop 


MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE     = 100
INITIAL_CAPACITY = 10


def handle_error() :
    print(  'Test failed')
    sys.exit(1)


#min_heap: heap for storing the larger half of numbers in the stream
#max_heap: heap for storing the smaller half of numbers in the stream
#cur_value: value of the current item in the stream 
#Return value: Median of the stream 
def get_median(min_heap, max_heap, cur_value):
    #If min_heap is empty, add the current value to min_heap.
    #If min_heap is non-empty, the top of min_heap will contain the smallest
    #among the larger half of numbers in the stream. If current value is 
    #larger than the top of min_heap, then add it to min_heap otherwise 
    #add it to max_heap
    if (len(min_heap) == 0) :
        heappush(min_heap, cur_value)
    elif (cur_value >= min_heap[0]):
        heappush(min_heap, cur_value)
    else:
        #Python has only a min heap implementation. So to mimic a 
        #max heap using a min heap we are multiplying -1 to cur_value
        #and adding it to the heap 
        heappush(max_heap, -1 * cur_value)


    #If min_heap has more than 1 element than the max_heap, move the top 
    #of min_heap into the max_heap and vice versa. 
    if (len(min_heap) > len(max_heap) + 1) :
        min_top = heappop(min_heap)
        heappush(max_heap, -1 * min_top)
    elif (len(max_heap) > len(min_heap) + 1):
        max_top = heappop(max_heap)
        heappush(min_heap, -1 * max_top)
    else:
        pass
    

    #If both heaps are of the same size, then the median will be the average 
    #of the top element in the two heaps. Otherwise the median is the top of 
    #the heap with more elements
    if (len(min_heap) == len(max_heap)) :
        median = (min_heap[0] + (-1 * max_heap[0])) / 2
    elif (len(min_heap) > len(max_heap)):
        median = min_heap[0]
    else :
        median = -1 * max_heap[0]
    

    return median




def sort_and_get_median(a, num_elems) :
    #Copy the values of a into b as we don't want to change the contents of a
    b = a[0:num_elems]

    b.sort()

    print(  'Sorted : ' , end='')
    print(b)

    middle_pos = num_elems // 2

    if (num_elems % 2 == 0) :
        median = (b[middle_pos - 1] + b[middle_pos]) / 2
    else :
        median = b[middle_pos]
    

    return median






def test() :
    min_heap = []
    max_heap = []

    #Randomly pick the number of elements
    length = random.randint(1, MAX_NUM_ELEMS)

    #Generate numbers in the list 
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]

    for  i in range(length):
        #Go on adding one element at a time and finding the median
        print(  'Stream : ', end='')
        print(a[0:i+1])

        #Find the median using the efficient technique
        median = get_median(min_heap, max_heap, a[i])

        #Find the median using sorting
        expected_result = sort_and_get_median(a, i+1)

        print('  Median = {}'.format(median) )

        if (median != expected_result):
            handle_error()

        print(  '_________________________________________________')
    
    



if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print(  'Test passed')





