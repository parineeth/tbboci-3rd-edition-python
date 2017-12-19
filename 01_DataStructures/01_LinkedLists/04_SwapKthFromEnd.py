
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
    
    @staticmethod
    def construct( num_elements): 
        head = None
        value = num_elements

        for i in range(num_elements): 
            new_node = LinkedListNode(value)
            new_node.next = head
            head = new_node
            value -= 1


        return head

    @staticmethod   
    def find_kth_node_from_begin(head,  k):
        cur_node = head
        prev = None

        i = 1
        while (cur_node): 
            if (i == k) :
                return cur_node, prev

            prev = cur_node
            cur_node = cur_node.next
            i += 1


        return None


    @staticmethod   
    def find_kth_node_from_end(head,  k):
        cur_node = head
        length = 0
        while (cur_node):
            length += 1
            cur_node = cur_node.next

        i = 1
        cur_node = head
        prev = None
        while (cur_node): 
            if (i == length - k + 1) :
                return cur_node, prev

            prev = cur_node
            cur_node = cur_node.next
            i += 1


        return None


    @staticmethod
    def display(head): 
        cur_node = head

        while (cur_node): 
            print('{} '.format(cur_node.data) , end='')
            cur_node = cur_node.next

        print('\n')





    #Helper function which swaps two neighbors n1 and n2
    #head: first node in the linked list
    #prev: node previous to n1
    #n1: first node to be swapped
    #n2: second node to be swapped. n2 occurs immediately after n1
    #Return value: head of the result linked list after swapping neighbors
    @staticmethod
    def swap_neighbors(head, prev, n1, n2):
        #Swap n1 and n2
        n1.next = n2.next
        n2.next = n1

        if (prev): 
            prev.next = n2
        else: 
            head = n2 #If prev doesn't exist, update head to n2

        return head 




    #Main function for swapping the kth node from beginning and end
    #head: first node in the linked list. 
    #k: which node in the linked list should be swapped
    #length: number of nodes in the linked list
    #Return value: head of the result linked list on success, None on error
    @staticmethod
    def swap_kth_node(head,  k,  length):  
        if (not head or k < 1 or k > length):
            return None

        #k1 is the kth node from begining and prev1 is previous to k1
        k1, prev1 = LinkedListNode.find_kth_node_from_begin(head, k)
    
        #k2 is the kth node from end and prev2 is previous to k2
        k2, prev2 = LinkedListNode.find_kth_node_from_end(head, k)

        if (not k1 or not k2):
            return None #the k value is incorrect

        if (k1 == k2):
            return head #both nodes are the same. So no need to swap

        #If k1 and k2 are neighbors, then handle this case and return
        if (k1.next == k2): 
            return LinkedListNode.swap_neighbors(head, prev1, k1, k2)

        if (k2.next == k1): 
            return LinkedListNode.swap_neighbors(head, prev2, k2, k1)

        #k1 and k2 are not neighbors. So swap k1.next with k2.next
        k1.next, k2.next = k2.next, k1.next

        if (prev1): 
            prev1.next = k2 
        else:  
            head = k2 #After swap, k2 becomes new head

        if (prev2): 
            prev2.next = k1 
        else:  
            head = k1 #After swap, k1 becomes new head

        return head




def handle_error(): 
    print('Test failed')
    sys.exit(1)




MAX_NUM_ELEMENTS = 10

if (__name__ == '__main__'):

    #We test for different linked list lengths
    for num_elems in range(MAX_NUM_ELEMENTS + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 1, the linked list will be 1
        #If num_elems = 2, the linked list will be 1->2 
        head = LinkedListNode.construct(num_elems)

        #Passing k value of 0 should return in an error
        ret_val = LinkedListNode.swap_kth_node(head, 0, num_elems)
        if (ret_val):
            handle_error()

        #We test for different k values
        for k in range(1, num_elems + 1): 

            print('Size = {}, k = {}'.format(num_elems, k) )
            print('Input  : ', end='')
            LinkedListNode.display(head)

            #Swap the kth element
            head = LinkedListNode.swap_kth_node(head, k, num_elems)

            print('Output : ', end='')
            LinkedListNode.display(head)

            #Verify the result
            k_node, k_prev = LinkedListNode.find_kth_node_from_begin(head, k)
            if (k_node.data != num_elems - k + 1):
                handle_error()

            #Again swap the kth element to get back the original linked list
            head = LinkedListNode.swap_kth_node(head, num_elems - k + 1, num_elems)

            #Verify the result
            k_node, k_prev = LinkedListNode.find_kth_node_from_begin(head, k)
            if (k_node.data != k):
                handle_error()
    
            print('_______________________________________')

        #Passing a value of k that is greater than length of linked list should return an error
        ret_val = LinkedListNode.swap_kth_node(head, num_elems + 1, num_elems)

        if (ret_val):
            handle_error()


    print('Test passed')














