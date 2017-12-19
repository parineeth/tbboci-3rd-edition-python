
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
    def handle_error(): 
        print('Test failed')
        sys.exit(1)


    @staticmethod
    def display(head): 
        cur_node = head

        while (cur_node): 
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        print('')
    
    @staticmethod
    def construct( num_elements, input_list): 
        head = None
        value = num_elements

        for i in range(num_elements):
            value = input_list[num_elements - 1 - i] 
            new_node = LinkedListNode(value)
            new_node.next = head
            head = new_node


        return head 

    @staticmethod
    def verify(head):

        cur_node = head
        prev_node = None

        while (cur_node): 
            if (prev_node): 
                if (cur_node.data < prev_node.data): 
                    handle_error()
        
            prev_node = cur_node
            cur_node = cur_node.next
    
    



    #n1: head of the first linked list
    #n2: head of the second linked list
    #Return value: head of the merged linked list
    @staticmethod
    def merge( n1, n2):
        if (not n1): 
            return n2 #If linked list1 is empty, return n2 

        if (not n2): 
            return n1 #If linked list2 is empty, return n1

        #make the result refer to the node with the smaller value 
        if (n1.data <= n2.data): 
            result = n1
            prev_merge_node = n1
            n1 = n1.next
        else: 
            result = n2
            prev_merge_node = n2
            n2 = n2.next

        #Process the two linked lists
        while (n1 and n2): 
            if (n1.data <= n2.data): 
                prev_merge_node.next = n1
                n1 = n1.next
                prev_merge_node = prev_merge_node.next
            else: 
                prev_merge_node.next = n2
                n2 = n2.next
                prev_merge_node = prev_merge_node.next
    

        #If there are still nodes present in the linked lists, then
        #append them to the result
        if (n1): 
            prev_merge_node.next = n1
        else: 
            prev_merge_node.next = n2

        return result


    

def handle_error(): 
    print('Test failed')
    sys.exit(1)





MAX_NUM_ELEMENTS = 10
MAX_NUM_LOOPS = 10
MAX_VALUE = 10


def test_merge_sort():


    #randomly decide the size of the linked lists
    num_elems1 = random.randint(0, MAX_NUM_ELEMENTS - 1)
    num_elems2 = random.randint(0, MAX_NUM_ELEMENTS - 1)

    #Store random values in the lists
    list1 = [random.randint(0, MAX_VALUE) for i in range(num_elems1)]
    list2 = [random.randint(0, MAX_VALUE) for i in range(num_elems2)]

    #Sort the lists
    list1.sort()
    list2.sort()

    #Construct the linked lists based on the elements in the list
    #The linked list will contain the elements in ascending order
    head1 = LinkedListNode.construct(num_elems1, list1)
    head2 = LinkedListNode.construct(num_elems2, list2)

    print('Input1 : ', end='')
    LinkedListNode.display(head1)

    print('Input2 : ', end='')
    LinkedListNode.display(head2)

    #Merge the lists
    result = LinkedListNode.merge(head1, head2)

    print('Output : ', end='')
    LinkedListNode.display(result)

    #Verify the result
    LinkedListNode.verify(result)

    print('____________________________________________')


        


if (__name__ == '__main__'):
    for num_loops in range(MAX_NUM_LOOPS):
        test_merge_sort()

    print('Test passed')

    













