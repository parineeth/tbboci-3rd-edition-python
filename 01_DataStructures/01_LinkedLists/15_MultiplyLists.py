
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random

class LinkedListNode(object):

    
    def __init__ (self, val = 0): 
        self.data = val
        self.next = None
    

    @staticmethod
    def construct(num_elements): 
        head = None
        for i in range(num_elements) :
            value = random.randint(0, 9)
            new_node = LinkedListNode(value)
            new_node.next = head
            head = new_node
        

        return head
    


    @staticmethod
    def convert_to_value(head): 
        cur_node = head
        result = 0
        while (cur_node) :
            result = result*10 + cur_node.data
            cur_node = cur_node.next
        

        return result
        



    #head:  first element in the linked list 
    #Return value:  first element of the reversed linked list
    @staticmethod
    def reverse(head): 
        cur_node = head
        prev_node = None

        while (cur_node) :
            #Store the next node in a temporary variable
            temp_node = cur_node.next

            #Reverse the link so that current node refers to the previous node
            cur_node.next = prev_node

            #Update the previous node to the current node 
            prev_node = cur_node

            #Proceed to the next node in the original linked list
            cur_node = temp_node
        

        #Once the linked list has been reversed, prev_node will be
        #refering to the new head. So return it
        return prev_node
    



    @staticmethod
    def display(head): 
        cur_node = head

        while (cur_node) :
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        
    


    #n1, n2: head of the first and second linked lists
    #count1, count2: num elements in first and second linked lists
    #Return value: head of new linked list having result of multiplication
    @staticmethod
    def multiply(n1, n2, count1, count2):
        #Reverse the two input linked lists
        h1 = LinkedListNode.reverse(n1)
        h2 = LinkedListNode.reverse(n2)

        #Pre-create the result linked list
        i = 0
        result_head = None
        while (i < count1 + count2 ) :
            cur_res_node = LinkedListNode(0)
            cur_res_node.next = result_head
            result_head = cur_res_node
            i += 1
    
        #Perform the multiplication
        result_start_node = result_head
        p1 = h1
        while (p1) :
            cur_res_node = result_start_node
            p2 = h2
            carry = 0
            while (p2) :
                product = p1.data * p2.data
                current_sum = product + cur_res_node.data + carry
                cur_res_node.data = current_sum % 10
                carry = current_sum // 10

                p2 = p2.next
                cur_res_node = cur_res_node.next
        
            cur_res_node.data = carry

            p1 = p1.next
            result_start_node = result_start_node.next
    
        #Reverse back the two input linked lists
        LinkedListNode.reverse(h1)
        LinkedListNode.reverse(h2)

        #Reverse the result linked list
        result_head = LinkedListNode.reverse(result_head)

        return result_head
    

    




MAX_NUM_ELEMENTS = 5
MAX_NUM_TESTS = 100

def handle_error(): 
    print('Test failed')
    sys.exit(1)
    

if (__name__ == '__main__'):    

    #Try out several tests where the inputs are randomly generated
    for loop in range(MAX_NUM_TESTS):

        #Generate a random linked list with a random number of elements
        num_elems1 = random.randint(0, MAX_NUM_ELEMENTS - 1)
        head1 = LinkedListNode.construct(num_elems1)

        #Generate a random linked list with a random number of elements
        num_elems2 = random.randint(0, MAX_NUM_ELEMENTS - 1)
        head2 = LinkedListNode.construct(num_elems2)

        #Perform the multiplication
        result = LinkedListNode.multiply(head1, head2, num_elems1, num_elems2)

        #Obtain the integer value of the two input linked lists and the 
        #result linked list
        val1 = LinkedListNode.convert_to_value(head1)

        val2 = LinkedListNode.convert_to_value(head2)

        val3 = LinkedListNode.convert_to_value(result)

        print('{} * {} = {}'.format(val1, val2, val3) )

        #Verify the result
        if (val3 != (val1 * val2)) :
            handle_error()
    

    


    print('Test passed')

    













