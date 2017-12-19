
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

import random



class LinkedListNode(object): 
    

    def __init__(self, val=0):  
        self.data = val
        self.next = None

    @staticmethod
    def handle_error() :
        print('Test failed')
        sys.exit(1)
    



    #head: list having head nodes of all the separated linked lists
    #tail: list having tail nodes of all the separated linked lists
    #cur_node: current node being processed
    #i: data value of the node
    @staticmethod
    def add_node(head, tail, cur_node, i) :
        cur_node.next = head[i]
        head[i] = cur_node
        if (not tail[i]):
            tail[i] = cur_node

    

    #first_node:  first node in the linked list to be sorted
    #num_distinct_values: number of distinct values 
    #Return value: head of the sorted linked list
    @staticmethod
    def sort_linked_list(first_node, num_distinct_values) :
        head = [None] * num_distinct_values 
        tail = [None] * num_distinct_values
        result = None

        if (not first_node):
            return None

        #Partition the input linked list into separate linked lists 
        #(0-list, 1-list and 2-list) based on the data in the node
        cur_node = first_node
        while (cur_node) :
            next_node = cur_node.next
            LinkedListNode.add_node(head, tail, cur_node, cur_node.data)
            cur_node = next_node
    
        #Connect the tail of first linked list with head of second linked list
        #and so on
        result = head[0]
        last_element = tail[0]
        for  i in range(1, num_distinct_values):
            if (not result):
                result = head[i]

            #Link last element of previous linked list with head of 
            #current linked list
            if (last_element):
                last_element.next = head[i]

            #update the last element to the tail of current linked list
            if (tail[i]):
                last_element = tail[i]
    

        return result
    

    @staticmethod
    def construct_list(num_elements, max_val) :
        head = None

        for  i in range(num_elements):
            new_node = LinkedListNode()
            new_node.data = random.randint(0, max_val - 1)
            new_node.next = head
            head = new_node
        

        return head
    

    @staticmethod
    def verify_list(head) :
        cur_node = head
        prev_node = None

        while (cur_node) :
            if (prev_node) :
                if (cur_node.data < prev_node.data) :
                    handle_error()

            prev_node = cur_node
            cur_node = cur_node.next
        
    

    @staticmethod
    def print_list(head) :
        cur_node = head

        while (cur_node) :
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        print('')
    







MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10
MAX_VALUE = 3

def test() :

    num_elems1 = random.randint(1, MAX_NUM_ELEMENTS)

    list1 = LinkedListNode.construct_list(num_elems1, MAX_VALUE)

    print('Input  : ', end='')
    LinkedListNode.print_list(list1)

    list1 = LinkedListNode.sort_linked_list(list1, MAX_VALUE)

    print('Output : ', end='')
    LinkedListNode.print_list(list1)

    LinkedListNode.verify_list(list1)

    print('__________________________________________________')

    return 0



if (__name__ == '__main__'):
    for  num_loops in range(MAX_NUM_LOOPS):
        test()

    print('Test passed')




