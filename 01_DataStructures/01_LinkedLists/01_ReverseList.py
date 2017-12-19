
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


from __future__ import print_function

import sys

class LinkedListNode(object):

    def __init__ (self, val): 
        self.data = val
        self.next = None
    
    #Reverses the linked list without using recursion
    #head: first node in the original linked list 
    #Return value: the first node of the reversed linked list
    @staticmethod
    def reverse(head):
        cur_node = head
        prev_node = None

        while (cur_node):
            #Store the next node in a temporary variable
            next_node = cur_node.next

            #Reverse the link 
            cur_node.next = prev_node

            #Update the previous node to the current node
            prev_node = cur_node

            #Proceed to the next node in the original linked list
            cur_node = next_node


        #Once the linked list has been reversed, prev_node will be
        #referring to the new head. So return it
        return prev_node

    
    #Recursively reverses the linked list
    #cur_node: current node of the linked list being processed
    #Return value: first node of the reversed linked list
    @staticmethod
    def reverse_r(cur_node):
        if (not cur_node or not cur_node.next):
            return cur_node #Return last node in original linked list as new head

        #Recursively reverses the remaining nodes in the linked list
        new_head = LinkedListNode.reverse_r(cur_node.next)

        #connect up the current node to the reversed linked list
        cur_node.next.next = cur_node
        cur_node.next = None

        return new_head
        

    @staticmethod
    def construct(num_elements):
        head = None
        value = num_elements

        #If num_elems = 1, the linked list will be 1->NULL
        #If num_elems = 2, the linked list will be 1->2->NULL
        for i in range(num_elements): 
            new_node = LinkedListNode(value)
            new_node.next = head
            head = new_node
            value -= 1
    

        return head

    @staticmethod
    def display (head): 
        cur_node = head

        while (cur_node): 
            print('{} '.format(cur_node.data), end='')
            cur_node = cur_node.next

        print('')






def handle_error(): 
    print('Test failed')
    sys.exit(1)




MAX_NUM_ELEMENTS_IN_LIST = 10

def test_reverse(reverse_fn):
    #Test Non-Recursive Linked List Reversal
    #We test for different linked list lengths ranging from 0 to MAX_NUM_ELEMENTS_IN_LIST
    for num_elems in range(MAX_NUM_ELEMENTS_IN_LIST + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 1, the linked list will be 1->NULL
        #If num_elems = 2, the linked list will be 1->2->NULL
        head = LinkedListNode.construct(num_elems)

        print('Input  : ', end='')
        LinkedListNode.display(head)

        head = reverse_fn(head)

        print('Output : ', end='')
        LinkedListNode.display(head)

        #Iterate the reversed linked list and check if it is in reverse order
        cur_node = head
        for j in range(num_elems): 
            if (cur_node.data != num_elems - j): 
                handle_error()
        
            cur_node = cur_node.next
    
        print('_______________________________________________')





if (__name__ == '__main__'):
    test_reverse(LinkedListNode.reverse)
    test_reverse(LinkedListNode.reverse_r)
    print('Test passed ')














