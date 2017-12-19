
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
    


     
    #head: first node of the linked list
    #k: how many nodes should be reversed
    #Return value: first node of the new linked list after reversing every k nodes
    @staticmethod
    def  k_reverse(head, k):
        if (not head or k == 0):
            return head

        cur_node = head
        prev_node = None
        i = 0
        while (cur_node and i < k): 
            #Store the next node in a temporary variable
            temp_node = cur_node.next

            #Reverse the link 
            cur_node.next = prev_node

            #Update the previous node to the current node
            prev_node = cur_node

            #Proceed to the next node in the original linked list
            cur_node = temp_node

            i += 1

        #We have reversed k nodes. So cur_node refers to the (k+1)th node
        #and head refers to the kth node.
        #Now recursively reverse the remaining nodes from cur_node onwards 
        #and assign the result to head.next.
        if (cur_node):
            head.next = LinkedListNode.k_reverse(cur_node, k)

        #prev_node will refer to first node in the linked list after reversal
        return prev_node


    @staticmethod
    def construct(num_elements): 
        head = None
        value = num_elements

        #If num_elems = 1, the linked list will be 1
        #If num_elems = 2, the linked list will be 1->2 
        for i in range (num_elements): 
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
    

    




def handle_error(): 
    print('Test failed')
    sys.exit(1)






MAX_NUM_ELEMENTS = 10


if (__name__ == '__main__'):

    #We test for different linked list lengths ranging from 0 to MAX_NUM_ELEMENTS
    for num_elems in range(MAX_NUM_ELEMENTS + 1): 
    
        #We test for different k values ranging from 0 to MAX_NUM_ELEMENTS+1
        for k in range(MAX_NUM_ELEMENTS + 2):  

            #Construct the linked list having num_elems. 
            #If num_elems = 1, the linked list will be 1
            #If num_elems = 2, the linked list will be 1->2
            head = LinkedListNode.construct(num_elems)

            print('Size = {}, K = {}'.format(num_elems, k) )

            LinkedListNode.display(head)

            head = LinkedListNode.k_reverse(head, k)

            LinkedListNode.display(head)

            print('_________________________________')
    


    print('Test passed')














