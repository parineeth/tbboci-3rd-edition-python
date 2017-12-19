
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function

import sys
import random

class LinkedListNode(object):

    def __init__ (self, val=0): 
        data = val
        next = None
        random = None
    

    @staticmethod
    def display(head): 
        cur_node = head

        while (cur_node): 
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        print('\n')


    @staticmethod
    def construct( num_elements): 
        head = None
        value = num_elements
        node_list = []

        #If num_elements is 2, the linked list created will be 1->2
        for i in range (num_elements): 
            new_node = LinkedListNode()
            new_node.data = value
            new_node.next = head
            node_list.insert(0, new_node)
            head = new_node
            value -= 1
    
        #Connect each node in the linked list to a random node
        new_node = head
        for i in range(num_elements): 
            rand_val = random.randint(0, num_elements - 1) 
            new_node.random = node_list[rand_val]
            new_node = new_node.next
    

        return head



    #original_head: head of the original linked list
    #Return value: head of the newly cloned linked list
    @staticmethod
    def clone(original_head):
        new_head = None

        #For each node in original linked list, create a new node. The new node
        #initially will be placed next to the original node
        n1 = original_head
        while (n1): 
            next_node = n1.next

            n2 = LinkedListNode()
            if (not n2):
                    return None
    
            n2.data = n1.data

            if (not new_head): 
                new_head = n2
            n1.next = n2
            n2.next = next_node
            n1 = next_node

        #Set the random value correctly for the new nodes
        n1 = original_head
        while (n1): 
            n1.next.random = n1.random.next
            n1 = n1.next.next

        #Disconnect the new nodes from the original linked list and 
        #form a new linked list for them
        n1 = original_head
        while (n1): 
            n2 = n1.next
            n1.next = n1.next.next
            if (n2.next):
                n2.next = n2.next.next

            n1 = n1.next

        return new_head



def handle_error(): 
    print('Test failed')
    sys.exit(1)
    




MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10
MAX_VALUE = 10

if (__name__ == '__main__'):

    #We test for different linked list lengths
    for num_elems in range(MAX_NUM_ELEMENTS + 1):

        #create a linked list with num_elems, where each node refers to the next node and a
        #random node
        head = LinkedListNode.construct(num_elems)

        #Clone the original linked list to create another copy 
        clone = LinkedListNode.clone(head)

        #Verify if the clone is a proper copy of the original linked list
        n1 = head
        n2 = clone
        while (n1 and n2):
            if ( (n1.data != n2.data) or (n1.random.data != n2.random.data)):
                handle_error()
    
            n1 = n1.next
            n2 = n2.next
    
        #If the original linked list or the clone is longer than the other then return an error
        if (n1 or n2):
            handle_error()


    print('Test passed')

    













