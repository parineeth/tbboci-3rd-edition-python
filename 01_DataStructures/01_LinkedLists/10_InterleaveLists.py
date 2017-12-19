
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
    def construct( num_elements, input_list): 
        head = None
        value = num_elements

        #Construct linked list based on elements in the list    
        for i in range(num_elements):
            value = input_list[num_elements - 1 - i] 
            new_node = LinkedListNode(value)
            new_node.next = head
            head = new_node


        return head


    @staticmethod
    def display(head): 
        cur_node = head

        while (cur_node): 
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        print('')
    


    #n1: head of the first linked list
    #n2: head of the second linked list
    #Return value: head of the result interleaved linked list
    @staticmethod
    def interleave(n1, n2):
        if (not n1): 
            return n2 #If linked list1 is empty, return n2 

        if (not n2): 
            return n1 #If linked list2 is empty, return n1

        #Process the two linked lists
        result = n1
        while (n1 and n2): 
            temp1 = n1.next
            temp2 = n2.next

            #Place node of second linked list next to the node of 
            #the first linked list
            if (n1.next):
                n2.next = n1.next
        
            n1.next = n2

            n1 = temp1
            n2 = temp2

        return result





def handle_error(): 
    print('Test failed')
    sys.exit(1)






    

MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10

def test_interleave():
    list1 = []
    list2 = []
    
    num_elems1 = random.randint(0, MAX_NUM_ELEMENTS - 1)
    num_elems2 = random.randint(0, MAX_NUM_ELEMENTS - 1)

    #If num_elems1 = 5, list1 will contain 1, 2, 3, 4, 5
    list1 = [i+1 for i in range(num_elems1)]
    
    #If num_elems2 = 5, list2 will contain 101, 102, 103, 104, 105 
    list2 = [i+101 for i in range(num_elems2)]
    
    #Use the lists to construct the two linked lists
    #If num_elems1 = 5, linked list1 will contain 1->2->3->4->5
    #If num_elems2 = 5. linked list2 will contain 101->102->103->104->105
    head1 = LinkedListNode.construct(num_elems1, list1)
    head2 = LinkedListNode.construct(num_elems2, list2)

    print('Input 1: ', end='')
    LinkedListNode.display(head1)

    print('Input 2: ', end='')
    LinkedListNode.display(head2)

    #Interleave the linked lists
    result = LinkedListNode.interleave(head1, head2)

    i = 0
    cur_node = result
    while (cur_node):
        #If index is even, then the element should be less than 100 
        if (i % 2 == 0 and i < 2 * num_elems1): 
            if (cur_node.data >= 100):
                handle_error()
        
        #If index is odd, then the element should be more than 100
        if (i % 2 == 1 and i < 2 * num_elems2): 
            if (cur_node.data < 100):
                handle_error()
        
        i += 1
        cur_node = cur_node.next
    

    if (i != (num_elems1 + num_elems2)):
        handle_error()

    print('Output : ', end='')
    LinkedListNode.display(result)

    print('__________________________________________')
    


    

if (__name__ == '__main__'):
    for num_loops in range(MAX_NUM_LOOPS): 
        test_interleave()

    print('Test passed')

    













