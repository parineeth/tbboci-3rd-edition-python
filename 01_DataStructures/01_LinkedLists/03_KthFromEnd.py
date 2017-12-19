
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
    


     
    #head: the first node of the linked list
    #k: node position from the end. k starts from 1 onwards
    #Return value: kth node from end if it exists, None otherwise
    @staticmethod
    def find_kth_node_from_end(head, k):
        length = 0
        n1 = head
        while (n1): 
            length += 1
            n1 = n1.next

        n1 = head
        for i in range(1, length + 1): 
            if (i == length - k + 1): 
                return n1   #n1 is the kth node from end. So return it
    
            n1 = n1.next

        #k value passed doesn't match with the linked list. So return None
        return None


    @staticmethod
    def construct(num_elements): 
        head = None
        value = num_elements

        #If num_elems = 1, the linked list will be 1
        #If num_elems = 2, the linked list will be 1->2 
        for i in range(num_elements): 
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

    #We test for different linked list lengths ranging from 1 to MAX_NUM_ELEMENTS
    for num_elems in range (1, MAX_NUM_ELEMENTS + 1): 

        #Construct the linked list having num_elems. 
        #If num_elems = 1, the linked list will be 1
        #If num_elems = 2, the linked list will be 1->2 
        head = LinkedListNode.construct(num_elems)

        #We test for different k values ranging from 0 to MAX_NUM_ELEMENTS+1
        for k in range(num_elems + 2):

            print('Input  : ', end='')
            LinkedListNode.display(head)
     
            #Find the kth node from the end
            k_node = LinkedListNode.find_kth_node_from_end(head, k)

            print('Size = {}, {}th node from end is '.format(num_elems, k) , end='')

            if (k_node):
                print('{}'.format(k_node.data) )
            else:
                print('Empty') 

            #Verify the kth node from the end
            if (k > 0 and k <= num_elems): 
                if (k_node.data != num_elems - k + 1): 
                    handle_error()
            else: 
                if (k_node): 
                    handle_error()
            
        
            print('__________________________________________')


        print('Test passed')
    













