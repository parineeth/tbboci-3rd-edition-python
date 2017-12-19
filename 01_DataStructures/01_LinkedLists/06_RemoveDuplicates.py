
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

import random

MAX_NUM_ELEMENTS = 10
MAX_VALUE = 10

class LinkedListNode(object):

    def __init__(self, val=0): 
        data = val
        next = None
    

    @staticmethod
    def handle_error(): 
        print('Test failed')
        sys.exit(1)
    

    #head: first node in the linked list
    @staticmethod
    def remove_duplicates(head): 
        #If there are 0 or 1 nodes in linked list, then simply return
        if (not head or not head.next):
            return
        
        cur_node = head
        while (cur_node) :
            #Iterate from node after cur_node to the end of the linked list
            iter_node = cur_node.next
            prev_node = cur_node

            while (iter_node) :
                if (cur_node.data == iter_node.data) :
                    #iter_node is a duplicate of cur_node. so 
                    #remove it
                    prev_node.next = iter_node.next
                    iter_node = iter_node.next
                else :
                    prev_node = iter_node
                    iter_node = iter_node.next

            
            cur_node = cur_node.next
    




    @staticmethod
    def construct(num_elements): 
        head = None

        for i in range (num_elements) :
            new_node = LinkedListNode()
            new_node.data = random.randint(0, MAX_VALUE - 1)
            new_node.next = head
            head = new_node
        

        return head
    


    @staticmethod
    def display(head): 
        cur_node = head
        while (cur_node) :
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        print('')
    

    @staticmethod
    def verify(head): 
        #If there are 0 or 1 elements in linked list, then simply return 
        if (not head or not head.next):
            return

            
        cur_node = head
        while (cur_node) :
            #Iterate from node after cur_node to the end of the linked list
            iter_node = cur_node.next
            while (iter_node) :
                #If there is a duplicate, then flag an error
                if (cur_node.data == iter_node.data) :
                    handle_error()
            
                iter_node = iter_node.next
            
            cur_node = cur_node.next
        

    





if (__name__ == '__main__'):

    #Test for different linked list lengths:
    for num_elems in range (MAX_NUM_ELEMENTS + 1) :
        #Construct a linked list with random elements. The linked list can contain duplicates
        head = LinkedListNode.construct(num_elems)

        print('Input  : ', end='')
        LinkedListNode.display(head)

        #Remove the duplicates
        LinkedListNode.remove_duplicates(head)

        print('Output : ', end='')
        LinkedListNode.display(head)

        #Verify the linked list
        LinkedListNode.verify(head)

        print('__________________________________________________________')


    print('Test passed ')




