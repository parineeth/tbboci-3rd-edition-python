
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random

class LinkedListNode(object): 


    def __init__(self, data=0): 
        self.data = data
        self.next = None
    

    @staticmethod
    def construct(num_elements, start_value) :
        head = None
        value = start_value

        prev = None
        for  i in range(num_elements):
            new_node = LinkedListNode()

            if (not prev):
                head = new_node
            else :
                prev.next = new_node
        
            new_node.data = value
            new_node.next = None
            prev = new_node     
            value += 1
        

        return head
    



    @staticmethod
    def display(head) :
        cur_node = head

        while (cur_node) :
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        print('')
    

    @staticmethod
    def find_length(n1) :
        length = 0
        while (n1) :
            n1 = n1.next
            length += 1
        
        return length
    

    #head1: first node of linked list1
    #head2: first node of linked list2
    #Return value: first common node between the two linked lists 
    @staticmethod
    def find_intersection_node(head1, head2):
        #Find the length of the two linked lists
        length1 = LinkedListNode.find_length(head1)
        length2 = LinkedListNode.find_length(head2)

        #store head of the longer linked list in n1 and head of 
        #shorter linked list in n2
        if (length1 >= length2) :
            n1 = head1
            n2 = head2
        else :
            n1 = head2
            n2 = head1
    
        #Find the difference in length of the two linked lists. Then advance
        #n1 by the difference
        diff = abs(length1 - length2)
        while (diff > 0) :
            n1 = n1.next
            diff -= 1
    
        #Go on comparing the nodes in linked list1 starting from n1 and
        #linked list2 starting from n2 till n1 and n2 match
        while (n1 and n2 and n1 != n2) :
            n1 = n1.next
            n2 = n2.next
    
        #n1 will have the common node if it exists, otherwise n1 will be None
        return n1







MAX_NUM_ELEMS = 10
MAX_NUM_TESTS = 10



def handle_error() :
    print('Test failed')
    sys.exit(1)





def test() :

    #Randomly generate the length of linked list1 and generate the elements of the list
    #If there are two elements in the linked list, then list is 0->1
    length1 = random.randint(0, MAX_NUM_ELEMS)
    start_value = 0
    head1 = LinkedListNode.construct(length1, start_value)

    #Randomly generate the length of linked list2 and generate the elements of the list
    #If there are two elements in the linked list, then list is 100->101
    length2 = random.randint(0, MAX_NUM_ELEMS)
    start_value = 100
    head2 = LinkedListNode.construct(length2, start_value)

    #Randomly generate the length of linked list3 and generate the elements of the list
    #If there are two elements in the linked list, then list is 200->201
    length3 = random.randint(0, MAX_NUM_ELEMS)
    start_value = 200
    head3 = LinkedListNode.construct(length3, start_value)

    #Find the last element in linked list1 and store it in n1
    n1 = head1
    while (n1 and n1.next) :
        n1 = n1.next
    

    #Find the last element in linked list2 and store it in n2
    n2 = head2
    while (n2 and n2.next) :
        n2 = n2.next
    

    #Connect the last element of linked list1 to first element of linked list3
    if (n1):
        n1.next = head3

    #Connect the last element of linked list2 to first element of linked list3
    if (n2):
        n2.next = head3


    print('Linked List 1 : ', end='')
    LinkedListNode.display(head1)

    print('Linked List 2 : ', end='')
    LinkedListNode.display(head2)

    #Find the first common node between linked list1 and linked list2
    result = LinkedListNode.find_intersection_node(head1, head2)

    if (result):
        print('Intersection node = {}'.format(result.data) )
    else :
        print('No intersection node')

    #The expected result is the first element in linked list3
    expected_result = None
    if (n1 and n2):
        expected_result = head3

    if (result != expected_result):
        handle_error()

    print('________________________________________________')



if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed ')



