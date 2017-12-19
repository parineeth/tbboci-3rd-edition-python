
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper


import random

class TreeNode(object):

    def __init__(self, val=0): 
        data = val
        left = None
        right = None
        parent = None
    
    
    @staticmethod
    def construct_bst (parent, values, low, high) :

        if (low > high):
            return None

        middle = (low + high) // 2

        new_node = TreeNode()
        if (not new_node):
            return None

        #Construct the new node using the middle value
        new_node.data = values[middle]
        new_node.parent = parent

        #Construct the left sub-tree using values[low] to values[middle-1]
        new_node.left = TreeNode.construct_bst(new_node, values, low, middle - 1)

        #Construct the right sub-tree using values[middle+1] to values[high]
        new_node.right = TreeNode.construct_bst(new_node, values, middle + 1, high)

        return new_node
    


    #Helper function for finding the error nodes in a Binary Search Tree
    #cur_node: current tree node
    #prev_node_list: contains node that is the in-order predecessor of cur_node
    #error1: list in which the first error node is returned
    #error2: list in which the second error node is returned
    @staticmethod
    def find_error_nodes(cur_node, prev_node_list, error1, error2):
        if (not cur_node):
            return

        #Check for error node in the left sub-tree
        TreeNode.find_error_nodes(cur_node.left, prev_node_list, error1, error2) 

        #cur_node should be greater than previous node. So if data in cur_node 
        #is less than or equal to previous node then we have found an error
        prev_node = prev_node_list[0]
        if (prev_node and cur_node.data <= prev_node.data) :
            if (not error1[0] ) :
                error1[0] = prev_node
                error2[0] = cur_node
            else :
                error2[0] = cur_node
                return
        
        #Update previous node to current node
        prev_node_list[0] = cur_node

        #Check for error node in the right sub-tree
        TreeNode.find_error_nodes(cur_node.right, prev_node_list, error1, error2)


    #Main function for correcting the Binary Search Tree
    #root: root node of the Binary Search Tree in which two nodes have been swapped
    @staticmethod
    def correct_bst(root):
        error1 = [None] 
        error2 = [None]
        prev_node_list = [None]

        #Find the two error nodes
        TreeNode.find_error_nodes(root, prev_node_list, error1, error2)

        #If we found two error nodes, then swap their data
        if (error1[0]  and error2[0] ) :
            error1[0].data, error2[0].data = error2[0].data, error1[0].data 



    #cur_node:   node whose left and right sub-trees need to be checked
    #prev_node_list:  contains the node that is the in-order predecessor of cur_node
    #Return value:  True if the tree is a binary search tree, False otherwise
    @staticmethod
    def is_bst(cur_node, prev_node_list) :

        if (not cur_node):
            return True

        if (not TreeNode.is_bst(cur_node.left, prev_node_list)): #Check if the left sub-tree is a BST
            return False

        #If data in cur_node is less than or equal to previous node then it is not a BST
        prev_node = prev_node_list[0]
        if ( prev_node and cur_node.data <= prev_node.data):
            return False

        #Update previous node to current node
        prev_node_list[0] = cur_node

        return TreeNode.is_bst(cur_node.right, prev_node_list) #Check if the right sub-tree is a BST
    








MAX_NUM_NODES_IN_TREE = 10

def handle_error() :
    print('Error occured')
    sys.exit(1)
    

if (__name__ == '__main__'):

    #Test for different number of nodes in the tree
    for num_elems in range(2, MAX_NUM_NODES_IN_TREE + 1) :

        #Construct a sorted list
        number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]
    

        #Choose two random indexes
        index1 = random.randint(0, num_elems - 1)
        index2 = random.randint(0, num_elems - 1)

        print('Num elements = {}, Swapping node at {} with node at {}'.format(num_elems,
                index1, index2)) 

        #Swap two locations in the sorted list
        number_list[index1], number_list[index2] = number_list[index2], number_list[index1]

        #Construct the Incorrect Binary Search Tree based on the number_list
        #Since two locations in the number_list are incorrect, two nodes in the 
        #Binary Search Tree will be incorrect.
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing the Incorrect tree: ')      
        PrintTreeHelper.print_tree(root, num_elems)

        #Correct the Binary Search Tree
        TreeNode.correct_bst(root)

        print('Printing the Corrected tree: ')      
        PrintTreeHelper.print_tree(root, num_elems)

        #Verify if the Binary Search Tree is proper
        prev_node_list = [None]
        if (not TreeNode.is_bst(root, prev_node_list) ):
            handle_error()

        print('______________________________________________________')



    print('Test passed')

    


