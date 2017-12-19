
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


def handle_error() :
    print(  'Test failed')
    sys.exit(1)





#a: almost sorted list that should be fully sorted
#k: max distance that any element should be moved so that list becomes sorted
def sort_almost_sorted_list(a, k) :
    min_heap = []

    read_pos = write_pos = 0

    #Fill in the first k values into the min_heap. If length is less than k
    #then we have to fill in only length number of elements 
    while (read_pos < min(k, len(a))):
        heappush(min_heap, a[read_pos])
        read_pos += 1
    
    #Add the element a[read_pos] to the heap and then pop out a value. 
    #Value popped from heap will contain the next smallest value. Add the   
    #value popped from the heap back into the list at the write position
    while (read_pos < len(a)) :
        heappush(min_heap, a[read_pos])
        a[write_pos] = heappop(min_heap)

        read_pos += 1
        write_pos += 1
    
    #Pop out the remaining elements in the heap and store them back into 
    #the list
    while (len(min_heap) > 0) :
        a[write_pos] = heappop(min_heap)
        write_pos += 1



def generate_list(length, k) :

    #We have to generate values in the list, so that it is almost sorted
    #The maximum distance that any element should be moved so that list becomes
    #sorted is k.
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]
    

    #First completely sort the list
    a.sort()

    #Divide the list into regions of the size k
    max_num_regions = (length + k - 1) // k

    for  region_nr in range(max_num_regions):
        #Within each region of the list, perform k random swaps
        for  num_swaps in range(k):
            index1 = (region_nr * k) + random.randint(0, k-1)
            index2 = (region_nr * k) + random.randint(0, k-1)

            if (index1 < length and index2 < length) :
                a[index1], a[index2] = a[index2], a[index1]
    
    return a


def test() :
    length = random.randint(1, MAX_NUM_ELEMS)
    k = random.randint(1, length)

    a = generate_list(length, k)

    print('K = {}'.format(k) )
    print('Input  : ', end='')
    print(a)

    #Copy values of a into b
    b = a[:]


    #Sort the almost sorted list using the efficient technique
    sort_almost_sorted_list(a, k)

    print(  'Output : ', end='')
    print(a)



    #Perform normal sort on b
    b.sort()

    #a and b should match
    if (a != b):
        handle_error()
    

    print(  '_________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')




