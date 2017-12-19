
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper

class TreeNode(object):


    def __init__(self, val = 0): 
        self.data = val
        self.left = None
        self.right = None
        self.parent = None
    


    #Recursively Construct a Binary Search Tree from the input list sorted in ascending order
    @staticmethod
    def construct_bst (parent, values, low, high): 
        if (low > high) :
            return None
        

        middle = (low + high) // 2

        new_node = TreeNode()

        new_node.data = values[middle]

        new_node.parent = parent

        new_node.left = TreeNode.construct_bst(new_node, values, low, middle - 1)

        new_node.right = TreeNode.construct_bst(new_node, values, middle + 1, high)

        return new_node
    


    #cur_node: current node 
    #prev_node_list: prev_node_list[0] has in-order predecessor of cur_node 
    #Return values: True if the tree is a binary search tree, False otherwise
    @staticmethod
    def is_bst(cur_node, prev_node_list):
        if (not cur_node):
            return True

        #Check if the left sub-tree is a BST
        if (not TreeNode.is_bst(cur_node.left, prev_node_list)): 
            return False

        #If data in cur_node is <= previous node then it is not a BST
        prev_node = prev_node_list[0]
        if (prev_node and cur_node.data <= prev_node.data):
            return False

        #Update previous node to current node
        prev_node_list[0] = cur_node

        #Check if the right sub-tree is a BST
        return TreeNode.is_bst(cur_node.right, prev_node_list) 

    






MAX_NUM_NODES_IN_TREE = 10


def handle_error(): 
    print('Test failed')
    sys.exit(1)



def print_result(result): 
    if (result) :
        print('The tree is a Binary Search Tree\n\n') 
    else :
        print('The tree is NOT a Binary Search Tree\n')
    



def swap_children(cur_node): 
    if (not cur_node):
        return

    cur_node.left, cur_node.right = cur_node.right, cur_node.left

    swap_children(cur_node.left)
    swap_children(cur_node.right)




if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree:
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :
        #Construct the tree based on the data stored in the number list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree')
        PrintTreeHelper.print_tree(root, num_elems)

        #Verify if the tree is binary search tree. Verification should pass:
        prev_node_list = [None]
        result = TreeNode.is_bst(root, prev_node_list)
        print_result(result)
        if (not result):
            handle_error()

        #Swap the left and right child of the root
        swap_children(root)

        print('Printing tree')
        PrintTreeHelper.print_tree(root, num_elems)

        #Verify if the tree is binary search tree. Verification should fail if num_elems > 1:
        #since we have swapped the left and right child of the root
        prev_node_list = [None]
        result = TreeNode.is_bst(root, prev_node_list)
        print_result(result)
        if (result and num_elems > 1):
            handle_error()

        print('_____________________________________________________')



    print('Test passed')
    













