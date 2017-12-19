
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
        for i in range (num_elements):
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
            print(cur_node.data + ' ', end='')
            cur_node = cur_node.next
        
        
    


    #n1: head of the first linked list 
    #n2: head of the second linked list
    #Return value: head of new linked list having the result of addition
    @staticmethod
    def add(n1, n2):
        #Reverse the two input linked lists
        h1 = p1 = LinkedListNode.reverse(n1)
        h2 = p2 = LinkedListNode.reverse(n2)

        #Add the nodes of the two linked lists
        current_sum = 0
        carry = 0
        result_node = None
        while (p1 and p2) :
            new_node = LinkedListNode()
            new_node.next = result_node
            result_node = new_node

            current_sum = p1.data + p2.data + carry
            new_node.data = current_sum % 10
            carry = current_sum // 10

            p1 = p1.next
            p2 = p2.next
    
        #If one of the two input linked lists still has nodes to be processed 
        #then make p1 refer to the leftover input linked list
        if (p2):
            p1 = p2

        #Process the remaining input linked list
        while (p1) :
            new_node = LinkedListNode()
            new_node.next = result_node
            result_node = new_node

            current_sum = p1.data + carry
            new_node.data = current_sum % 10
            carry = current_sum // 10
            p1 = p1.next
    
        #If carry is non-zero, then store the carry in the result linked list
        if (carry != 0) :
            new_node = LinkedListNode()
            new_node.next = result_node
            result_node = new_node
            new_node.data = carry
    
        #Reverse back the two input linked lists
        LinkedListNode.reverse(h1)
        LinkedListNode.reverse(h2)

        #The result  node already refers to MS node.  So no need to reverse 
        #result linked list
        return result_node


    





MAX_NUM_ELEMENTS = 10
MAX_NUM_TESTS = 100


def handle_error(): 
    print('Test failed')
    sys.exit(1)




 
if (__name__ == '__main__'):

    #Try out several tests where the inputs are randomly generated
    for loop in range(MAX_NUM_TESTS) :

        #Generate a random linked list with a random number of elements
        num_elems1 = random.randint(0, MAX_NUM_ELEMENTS - 1)
        head1 = LinkedListNode.construct(num_elems1)

        #Generate a random linked list with a random number of elements
        num_elems2 = random.randint(0, MAX_NUM_ELEMENTS - 1)
        head2 = LinkedListNode.construct(num_elems2)

        #Perform the addition
        result = LinkedListNode.add(head1, head2)

        #Obtain the integer value of the two input linked lists and the 
        #result linked list
        val1 = LinkedListNode.convert_to_value(head1)

        val2 = LinkedListNode.convert_to_value(head2)

        val3 = LinkedListNode.convert_to_value(result)

        print('{} + {} = {}'.format(val1, val2, val3) )

        #Verify the result
        if (val3 != (val1 + val2)) :
            handle_error()
    


    print('Test passed')

    













