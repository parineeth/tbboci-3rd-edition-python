
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function

import sys

class LinkedListNode(object):

    def __init__(self, val=0): 
        self.data = val
        self.next = None
    
    @staticmethod
    def display(head): 
        cur_node = head

        while (cur_node): 
            print(cur_node.data, end='')
            cur_node = cur_node.next
        

    @staticmethod
    def construct(str1): 
        head = None

        for c in reversed(str1):
            new_node = LinkedListNode(c)
            new_node.next = head
            head = new_node

        return head


    #head:  first element in the linked list 
    #Return value:  first element of the reversed linked list
    @staticmethod
    def reverse(head):

        cur_node = head
        prev_node = None

        while (cur_node):
            #Store the next node in a temporary variable
            temp_node = cur_node.next

            #Reverse the link so that current node pos to the previous node
            cur_node.next = prev_node

            #Update the previous node to the current node
            prev_node = cur_node

            #Proceed to the next node in the original linked list
            cur_node = temp_node
    

        #Once the linked list has been reversed, prev_node will be
        #refering to the new head. So return it
        return prev_node


    



    #head: first element of linked list.
    #Returns: True if list is a palindrome, False otherwise
    @staticmethod
    def is_palindrome(head):
        if (not head):
            return False

        #Advance p by two nodes and q by one node in each loop.
        #So when p reaches the end of list, q will refer to middle of 
        #the linked list
        p = q = head
        length = 0
        while (p): 
            length += 1
            p = p.next
            if (p): 
                length += 1
                p = p.next
    
            if (p): 
                q = q.next
    
        #Reverse the second half of the linked list
        temp = r = LinkedListNode.reverse(q.next)
        p = head

        #Compare first half with reverse of second half
        is_palindrome = True
        for i in range(length // 2):
            if (p.data != r.data):
                is_palindrome = False
                break
    
            p = p.next
            r = r.next

        #Reverse the second half of linked list to get back original 
        #linked list
        LinkedListNode.reverse(temp) 
    
        return is_palindrome


    



def handle_error(): 
    print('Test failed')
    sys.exit(1)
    







def test(str1, expected_result): 

    #Construct the linked list based on the given string
    head = LinkedListNode.construct(str1) 

    #Check if linked list is palindrome
    result = LinkedListNode.is_palindrome(head)

    LinkedListNode.display(head)
    if (result):
        print(' ----> is palindrome ')
    else:
        print(' ----> is not palindrome ')

    #Verify the result
    if (result != expected_result):
        handle_error()

    print('______________________________________')


    
if (__name__ == '__main__'):
    test('a', True)
    test('abba', True)
    test('level', True)
    test('Hello', False) 

    print('Test passed')












