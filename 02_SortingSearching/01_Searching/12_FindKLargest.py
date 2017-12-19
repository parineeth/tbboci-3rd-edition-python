
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

import random 


MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 20
MAX_K_VALUE = 10 
MAX_VALUE  = 100

def handle_error() :
    print('Test failed')
    sys.exit(1)




#Helper function to perform heapify
#heap: min heap.  Maximum number of elements in heap is k
#pos: position of the heap that may need to be fixed
#heap_size: current number of nodes in the heap
def heapify(heap, pos, heap_size) :
    left = 2 * pos
    right = (2 * pos) + 1
    ix_of_smallest = pos

    #Find which of the three are the smallest - value at pos OR left child
    #OR right child
    if (left < heap_size and heap[pos] > heap[left]):
        ix_of_smallest = left
    if (right < heap_size and heap[ix_of_smallest] > heap[right]):
        ix_of_smallest = right


    if (ix_of_smallest != pos) :
        #If pos doesn't contain the smallest value,
        #then swap the smallest value into pos 
        heap[pos], heap[ix_of_smallest] = heap[ix_of_smallest], heap[pos]

        #Recursively readjust the heap
        heapify(heap, ix_of_smallest, heap_size)
    


#Main function to find the k largest elements
#a: non-empty list in which we have to find the k largest elements
#k: the number of largest elements that we need to find. k <= len(a)
#Return value: the k largest elements will be returned in a list
def find_k_largest(a, k):
    heap = []

    #Store the first k elements of the list in the heap
    for  i in range(k):
        heap.append(a[i])

    #Construct the initial min-heap
    for  i in range(k - 1, -1,-1):
        heapify(heap, i, k)

    for  i in range(k, len(a)):
        #The root of heap will have the smallest item in the heap
        #If current item in list is greater than root of the heap, then
        #place current item into root of the heap and re-adjust the heap
        if (a[i] > heap[0]) :
            heap[0] = a[i]
            heapify(heap, 0, k)
        
    return heap


def test01() :
    #Randomly generate the k value
    k = random.randint(1, MAX_K_VALUE)

    print('K = {}'.format(k) )

    #randomly generate the numbers in the list
    a = [random.randint(0, MAX_VALUE) for i in range(MAX_NUM_ELEMS) ]

    print('Input  : ', end='')
    print(a)

    #Find the k largest elements using the heap
    heap = find_k_largest(a, k)

    #Sort the list in descending order
    a.sort(key = lambda x: -1 * x)

    #Print the top k elements in the heap. Note that elements in the heap will themselves 
    #NOT be in sorted order
    print('Output : ', end='')
    print(heap)

    #Verify that each element in the heap is present in the top k elements in the sorted list 
    for  cur_heap_val in heap:
        found = False
        for  j in range(k):
            if (cur_heap_val == a[j] ) :
                found = True
                break

        if (not found):
            handle_error()
    




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test01()
        print('_________________________________________________\n\n')

    print('Test passed')




