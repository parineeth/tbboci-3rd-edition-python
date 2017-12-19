
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper



class TreeNode(object):

    
    def __init__(self, val=0): 
        self.data = val
        self.left = None
        self.right = None
        self.parent = None



    @staticmethod
    def construct_bst (parent, values, low, high) :
        if (low > high) :
            return None
        

        middle = (low + high) // 2

        new_node = TreeNode()

        new_node.data = values[middle]

        new_node.parent = parent

        new_node.left = TreeNode.construct_bst(new_node, values, low, middle - 1)

        new_node.right = TreeNode.construct_bst(new_node, values, middle + 1, high)

        return new_node

    


    @staticmethod
    def print_data(data) :
        print('{} '.format(data) , end='')
    

    #cur_node: current BST node being processed
    #prev_node_list: prev_node_list[0] has node that is previous to cur_node in 
    #       linked list
    #head_list: head of the result linked list will be passed in head_list[0]
    #Returns: 0 on success
    @staticmethod
    def bst_to_linked_list(cur_node, prev_node_list, head_list) :
        if (not cur_node):
            return 0

        #In-Order Traversal of the BST

        #Convert the left sub-tree of node to linked list
        TreeNode.bst_to_linked_list(cur_node.left, prev_node_list, head_list)

        #Link the previous node with the current node
        prev_node = prev_node_list[0]
        cur_node.left = prev_node

        if (prev_node) :
            prev_node.right = cur_node
        else :
            #Since previous node is None, this is the first node 
            #of the linked list. So make head refer to it
            head_list[0] = cur_node
    

        #Make the current node the previous node
        prev_node_list[0] = cur_node

        #Convert the right sub-tree of node to linked list
        TreeNode.bst_to_linked_list(cur_node.right, prev_node_list, head_list)

        return 0 #return success



    




MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)



def print_linked_list(head) :
    cur_node = head

    while (cur_node) :
        print('{} '.format(cur_node.data) , end='')
        cur_node = cur_node.right
    
    print('')



def verify_list(head) :

    if (not head):
        return

    #Traverse the doubly linked list from left to right
    prev_node = head
    iter_node = head.right
    last_node = head
    while (iter_node) :
        #The data should be arranged in increasing order
        if (prev_node.data >= iter_node.data) :
            handle_error()
        

        #Find the last node in the doubly linked list
        if (not iter_node.right):
            last_node = iter_node

        prev_node = iter_node
        iter_node = iter_node.right
    

    #Traverse the doubly linked list from right to left
    prev_node = last_node
    iter_node = last_node.left
    while (iter_node) :
        #The data should be arranged in decreasing order
        if (prev_node.data <= iter_node.data) :
            handle_error()
        

        prev_node = iter_node
        iter_node = iter_node.left
    



if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]


    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :

        #construct the Binary Search Tree
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #Convert the Binary Search Tree to Doubly Linked List
        prev_list = [None]
        head_list = [None]
        TreeNode.bst_to_linked_list(root, prev_list, head_list)

        print('Printing the Doubly Linked List:')
        print_linked_list(head_list[0])

        #Verify the Doubly Linked List
        verify_list(head_list[0])

        print('___________________________________________________')



    print('Test passed')
    













