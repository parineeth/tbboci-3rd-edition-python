
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random

class Node(object):

    def __init__(self, value=0, list_no=0):
        self.value = value
        self.list_no = list_no







MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100
MAX_NUM_LISTS = 5
MAX_INT = 99999

def handle_error() :
    print('Test failed')
    sys.exit(1)




#heap:  min heap of nodes. 
#pos: position of the heap that may need to be fixed
#heap_size: current number of nodes in the heap

def heapify(heap, pos, heap_size) :
    left = 2 * pos
    right = (2 * pos) + 1
    ix_of_smallest = pos

    #Find which of the three are the smallest - heap[pos] OR left child
    #OR right child
    if (left < heap_size and heap[pos].value > heap[left].value):
        ix_of_smallest = left

    if (right < heap_size and heap[ix_of_smallest].value > heap[right].value):
        ix_of_smallest = right

    if (ix_of_smallest != pos) :
        #If pos doesn't contain the smallest node,
        #then swap the smallest node into pos 
        heap[pos], heap[ix_of_smallest] = heap[ix_of_smallest], heap[pos]

        heapify(heap, ix_of_smallest, heap_size)
    



#lists:  the lists to be merged. lists[0] has the first list, lists[1] has 
#       the second list and so on
#Return value:  the merged results are passed back in this list
def merge_k_sorted_lists(lists) :
    k = len(lists)  #number of lists
    n = len(lists[0]) #number of elements in each list
    heap = []
    arr_pos = []

    #Store the first element in each list into the heap
    for  i in range(k):
        new_node = Node()
        new_node.value = lists[i][0]
        new_node.list_no = i
        heap.append(new_node)
        arr_pos.append(1)
    
    #Construct the initial heap using the heapify procedure
    for  i in range(k - 1, -1,-1):
        heapify(heap, i, k)

    #Process the remaining elements in the lists. When all elements in  
    #the lists have been processed, MAX_INT will be present at root of heap
    result = [] 
    while (heap[0].value != MAX_INT) :
        #root of the heap will have the lowest value. So store
        #it into the result
        result.append(heap[0].value)

        list_no = heap[0].list_no
        pos = arr_pos[list_no]

        #If the root belongs to list x, then replace the root with
        #the next element in list x
        if (pos >= n) :
            #If we have exhausted all elements in the list, 
            #then insert MAX_INT into the heap
            heap[0].value = MAX_INT
            heap[0].list_no = list_no
        else :
            heap[0].value = lists[list_no][pos]
            heap[0].list_no = list_no
        

        #Re-adjust the heap after replacing the root
        heapify(heap, 0, k)

        arr_pos[list_no] += 1
    
    return result





def test01(num_lists, num_elements) :

    lists = [[random.randint(0, MAX_VALUE) for j in range(num_elements)] for i in range(num_lists)]
    

    for  i in range(num_lists):
        lists[i].sort()
        print('List {}: '.format(i) , end='')
        print(lists[i])
    

    result = merge_k_sorted_lists(lists)

    print('Output : ', end='')
    print(result)

    expected_result = []
    for  inner_list in lists:
        for  cur_value in inner_list:
            expected_result.append(cur_value)
        
    expected_result.sort()

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        num_lists = random.randint(2, MAX_NUM_LISTS)

        num_elements = random.randint(1, MAX_NUM_ELEMS)

        test01(num_lists, num_elements)

        print('_________________________________________________')

    print('Test passed')



