
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function


import sys

def handle_error(): 
    print('Test failed')
    sys.exit(1)


class LinkedListNode(object):

    def __init__ (self, val=0): 
        self.data = val
        self.next = None
        
    @staticmethod
    def handle_error(): 
        print('Test failed')
        System.exit(1)

    @staticmethod
    def display(head): 
        cur_node = head
        while (cur_node) :
            print('{}'.format(cur_node.data) , end='')
            cur_node = cur_node.next
        
        print('')
    

    @staticmethod
    def construct(num_elements):
        head = None
        value = num_elements

        #If num_elements is 2, then linked list will be 1->2 
        for i in range (num_elements) :
            new_node = LinkedListNode()
            new_node.data = value
            new_node.next = head
            head = new_node
            value -= 1
        

        return head
    

    #head: the first element of the linked list
    #k:  which element from the end.
    #length: number of elements in the linked list
    #Return value:   kth element from end if it exists and element previous the kth element
    @staticmethod
    def find_kth_node_from_end(head,  k,  length):
        n1 = head
        prev = None
        for i in range (1, length + 1) :
            if (i == length - k + 1) :
                return n1, prev #n1 is the kth element from end. So return it
            
            prev = n1
            n1 = n1.next
        

        #k value passed doesn't match with the linked list. So return None 
        return None, None
    


    #head: first node of the linked list
    #k: by how many positions the linked list should be rotated
    #length: number of nodes in the linked list
    #Return value: first node of the rotated linked list
    @staticmethod
    def rotate(head, k, length):
        #If there are 0 or 1 nodes in the linked list, then simply return
        if (length < 2):
            return head

        #If we shift by k times, then we get back the same linked list. 
        #So we just have to shift k % length times
        k = k % length

        #If k is 0, then no need to shift
        if (k == 0):
            return head

        #Find the kth node from the end. If k = 1, then pivot will have
        #the last node and prev will be the node previous to last node
        pivot, prev = LinkedListNode.find_kth_node_from_end(head, k, length)

        #Find the last node in the linked list
        last = pivot
        while (last.next):
            last = last.next

        #Make the last node point to head and the node previous to pivot
        #point to None
        last.next = head
        prev.next = None

        #pivot will be the new head
        return pivot


    @staticmethod
    def compare( head,  expected_result,  length):
        cur_node = head
    
        for i in range(length):
            if (not cur_node):
                handle_error()

            if (cur_node.data != expected_result[i]) :
                handle_error()
        
            cur_node = cur_node.next 
        

        if (cur_node):
            handle_error()
        







def perform_test( head,  length,  num_rotations,  expected_result): 
    print('Num Rotations = {}'.format(num_rotations) )

    print('Before Rotating: ', end='')
    LinkedListNode.display(head)

    head = LinkedListNode.rotate(head, num_rotations, length)
    LinkedListNode.compare(head, expected_result, length)

    print('After  Rotating: ', end='')
    LinkedListNode.display(head) 

    print('________________________________________')   



def test1(): 
    expected_result = [1]
    length = 1 
    num_rotations = 1

    #linked list initially contains 1->None 
    head = LinkedListNode.construct(length)
    perform_test(head, length, num_rotations, expected_result)



def test2():
    expected_result = [5, 1, 2, 3, 4]
    length = 5
    num_rotations = 1

    #linked list initially contains 1->2->3->4->5 
    head = LinkedListNode.construct(length)
    perform_test(head, length, num_rotations, expected_result)




def test3(): 
    expected_result = [4, 5, 1, 2, 3]
    length = 5 
    num_rotations = 2

    #linked list initially contains 1->2->3->4->5 
    head = LinkedListNode.construct(length)
    perform_test(head, length, num_rotations, expected_result)




def test4(): 
    expected_result = [2, 3, 4, 5, 1]
    length = 5
    num_rotations = 4

    #linked list initially contains 1->2->3->4->5 
    head = LinkedListNode.construct(length)
    perform_test(head, length, num_rotations, expected_result)



def test5():
    expected_result = [1, 2, 3, 4, 5]
    length = 5 
    num_rotations = 5

    #linked list initially contains 1->2->3->4->5 
    head = LinkedListNode.construct(length)
    perform_test(head, length, num_rotations, expected_result)


if (__name__ == '__main__'):
    test1()
    test2()
    test3()
    test4()
    test5()

    print('Test passed')




