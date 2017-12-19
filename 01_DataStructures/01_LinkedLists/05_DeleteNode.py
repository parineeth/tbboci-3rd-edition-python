
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function

import sys
import random

class LinkedListNode(object):

    def __init__ (self, val): 
        self.data = val
        self.next = None
    
    @staticmethod
    def construct( num_elements): 
        head = None
        value = num_elements

        #If num_elems = 1, the linked list will be 1
        #If num_elems = 2, the linked list will be 1->2 
        for i in range(num_elements): 
            new_node = LinkedListNode(value)
            new_node.next = head
            head = new_node
            value -= 1


        return head


    @staticmethod
    def display(head): 
        cur_node = head

        while (cur_node): 
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next

        print('\n')

 
    #n1: the node to be deleted
    #Return value: True on success, False on failure
    @staticmethod
    def delete_node(n1):
        if (n1.next): 
            #Get the next node
            n2 = n1.next

            #Copy the contents of the next node into the current node
            n1.data = n2.data
            n1.next = n2.next

            #Return indicating the operation is successful
            return True

        #return indicating the operation failed
        return False





def handle_error(): 
    print('Test failed')
    sys.exit(1)
    


    



MAX_NUM_ELEMENTS = 10

if (__name__ == '__main__'):

    #We test for different linked list lengths
    for num_elems in range(2, MAX_NUM_ELEMENTS + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 2, the linked list will be 1->2 
        head = LinkedListNode.construct(num_elems)

        #Choose a random position to delete. It should not be the last element
        k = random.randint(0, num_elems - 2)

        print('Deleting {}th node '.format(k) )
        print('Input  : ', end='')
        LinkedListNode.display(head)

        #Find the node at position k
        cur_node = head
        for i in range(k): 
            cur_node = cur_node.next
    
        #delete the node
        ret_val = LinkedListNode.delete_node(cur_node)

        print('Output  : ', end='')
        LinkedListNode.display(head)

        #Verify the result
        if (not ret_val):
            handle_error()

        print('_____________________________________________')



    print('Test passed')

    













