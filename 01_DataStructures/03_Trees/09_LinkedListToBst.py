
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
    

    #cur_node:  current node 
    #prev_node_list: in-order predecessor of cur_node is present in prev_node_list[0]
    #Return value:  True if the tree is a binary search tree, False otherwise
    @staticmethod
    def is_bst(cur_node, prev_node_list):
    
        if (not cur_node):
            return True

        if (not TreeNode.is_bst(cur_node.left, prev_node_list)): #Check if the left sub-tree is a BST
            return False

        #If data in cur_node is less than or equal to previous node then it is not a BST
        prev_node = prev_node_list[0]
        if (prev_node and cur_node.data <= prev_node.data):
            return False

        #Update previous node to current node
        prev_node_list[0] = cur_node

        return TreeNode.is_bst(cur_node.right, prev_node_list) #Check if the right sub-tree is a BST
    


    #node_list:  helper list of size 1 that contains a node. 
    #       this list is used for traversing the doubly linked list
    #start: index of node in linked list at beginning of region being operated on
    #end: index of node in linked list at end of region being operated on
    @staticmethod
    def construct_bst (node_list, start, end):
        if (start > end):
            return None

        middle = (start + end) // 2

        #Recursively construct the left subtree  using the nodes before the 
        #middle node and get the root of the left sub-tree
        left_child = TreeNode.construct_bst(node_list, start, middle - 1)

        #node_list[0] will now be refering to the middle node
        middle_node = node_list[0]

        #Connect the left sub-tree to the middle node
        middle_node.left = left_child

        #Advance to the next node after the middle node
        node_list[0] = middle_node.right

        #Recursively construct the right subtree using the nodes after the  
        #middle node and connect the root of right subtree to middle node
        middle_node.right = TreeNode.construct_bst(node_list, middle + 1, end)

        return middle_node


    





MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)



def print_linked_list(head) :
    cur_node = head

    while (cur_node) :
        print('{} '.format(cur_node.data) , end='')
        cur_node = cur_node.right
    
    print('\n')



def print_result(result) :
    if (result) :
        print('The tree is a Binary Search Tree') 
    else :
        print('The tree is NOT a Binary Search Tree')
    

if (__name__ == '__main__'):

    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
    
        #Construct a doubly linked list
        prev = None
        head = None
        for i in range(MAX_NUM_NODES_IN_TREE):
            new_node = TreeNode()
            new_node.left = prev
            new_node.right = None
            new_node.data = i

            if (prev):
                prev.right = new_node

            if (i == 0):
                head = new_node

            prev = new_node
    

        print('Printing the Doubly Linked List:')
        print_linked_list(head)

        #Convert the doubly linked list to a Binary Search Tree
        node_list = [head]
        root = TreeNode.construct_bst(node_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #Verify if the tree formed is a Binary Search Tree
        prev_node_list = [None]
        result = TreeNode.is_bst(root, prev_node_list)
        print_result(result)
        if (not result):
            handle_error()

        print('_____________________________________________________________')




    print('Test passed')
    













