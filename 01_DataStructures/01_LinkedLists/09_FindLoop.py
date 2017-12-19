
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function

import sys
import random

class LinkedListNode(object):

    def __init__ (self, val=0): 
        self.data = val
        self.next = None
    

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
        value = num_elements - 1

        #If num_elems = 1, the linked list will be 0
        #If num_elems = 2, the linked list will be 0->1 
        for i in range(num_elements): 
            new_node = LinkedListNode(value)
            new_node.next = head
            head = new_node
            value -= 1


        return head


    #Adds a loop to the linked list at a random position
    @staticmethod
    def add_loop(head,  num_elems): 
        low = high = 0
        n1 = n2 = None

        #Randomly generate 2 values
        low = random.randint(0, num_elems - 1)
        high = random.randint(0, num_elems - 1)

        #Make sure that low <= high
        if (low > high): 
            low, high = high, low
        
        #Find the nodes at positions low and high
        cur_node = head
        i = 0
        while (cur_node): 
            if (i == low):
                n1 = cur_node

            if (i == high): 
                n2 = cur_node
                break
        

            i += 1
            cur_node = cur_node.next
    

        print('Adding loop from pos {} to pos {}'.format(high, low) )
        #Add loop from node at position high to node at position low
        n2.next = n1
        return n1

    
    #head: first node of the linked list 
    #Return value: first node in loop if loop exists, None otherwise
    @staticmethod
    def find_loop(head): 
        n1 = n2 = head
        found_loop = False

        #n1 moves fast. So advance it by two steps
        #n2 is slow. So advance it by one step
        while (n1): 
            n1 = n1.next
            if (n1): 
                n1 = n1.next
                n2 = n2.next
    
            #If n1 and n2 meet then there is a loop in the linked list
            if (n1 == n2): 
                found_loop = True
                break
    
        if (not found_loop):
            return None
    
        #Find the beginning of the loop
        n3 = head
        while (n1 != n3):
            n1 = n1.next
            n3 = n3.next

        return n1





def handle_error(): 
    print('Test failed')
    sys.exit(1)


    

MAX_NUM_ELEMENTS = 10

if (__name__ == '__main__'):

    #We test for different linked list lengths
    for num_elems in range (1, MAX_NUM_ELEMENTS + 1): 

        print('Number of elements = {}'.format(num_elems) )

        #Construct the linked list without any loops  
        #If num_elems = 2, the linked list will be 1->2
        head = LinkedListNode.construct(num_elems)

        #Currently there are no loops in the linked list. If we find a loop, report error
        if (LinkedListNode.find_loop(head)):
            handle_error()

        if (head):
            #Add a loop to the linked list 
            expected_result = LinkedListNode.add_loop(head, num_elems)

            #We should find a loop in the linked list. If we don't find a loop, report error
            result = LinkedListNode.find_loop(head)

            if (result != expected_result): 
                handle_error()

            print('Found loop in linked list at position {}'.format(result.data) )
    

        print('____________________________________________________')


    print('Test passed')

    













