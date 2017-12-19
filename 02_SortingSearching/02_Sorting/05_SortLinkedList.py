
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
    

    #n1:  head of the first linked list
    #n2:  head of the second linked list
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

    



    #first_node: head of the linked list to be sorted
    #num_elements: number of elements in the linked list
    #Return value: head of the merged and sorted linked list
    @staticmethod
    def sort_linked_list(first_node, num_elements) :
        if (num_elements == 0):
            return None

        #If there is only a single node in linked list, then disconnect next 
        #and return the node as the result without any further recursive calls
        if (num_elements == 1) :
            first_node.next = None
            return first_node
    
        #Divide into two linked lists. linked list1 has count1 elements and
        #linked list2 has count2 elements 
        linked_list1 = first_node
        count1 = num_elements // 2

        cur_node = first_node
        for  i in range(count1):
            cur_node = cur_node.next

        linked_list2 = cur_node
        count2 = num_elements - count1

        #Call sort_linked_list recursively on the two linked lists
        linked_list1 = LinkedListNode.sort_linked_list(linked_list1, count1)
        linked_list2 = LinkedListNode.sort_linked_list(linked_list2, count2)

        #The two linked lists are now sorted. So merge them into a single
        #sorted linked list and return its head node
        return LinkedListNode.merge(linked_list1, linked_list2)
    

    

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
MAX_VALUE = 100

def test() :

    num_elems1 = random.randint(1, MAX_NUM_ELEMENTS)

    list1 = LinkedListNode.construct_list(num_elems1, MAX_VALUE)

    print('Input  : ', end='')
    LinkedListNode.print_list(list1)

    list1 = LinkedListNode.sort_linked_list(list1, num_elems1)

    print('Output : ', end='')
    LinkedListNode.print_list(list1)

    LinkedListNode.verify_list(list1)

    print('__________________________________________________')

    return 0



if (__name__ == '__main__'):
    for  num_loops in range(MAX_NUM_LOOPS):
        test()

    print('Test passed')




