
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
    

    #parent: parent of the BST node currently being constructed
    #values: sorted list to be converted into BST
    #low, high: lower and upper indexes of the list region being operated on
    #Return value: BST node created that corresponds to values[(low+high)//2]
    @staticmethod
    def construct_bst(parent, values, low, high):
        middle = (low + high) // 2

        if (low > high):
            return None

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



    #cur_node:  current node 
    #prev_node_list: in-order predecessor of cur_node is present in prev_node_list[0]
    #Return value:  True if the tree is a binary search tree, False otherwise
    @staticmethod
    def is_bst(cur_node, prev_node_list) :
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
    
    





MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)
    


def print_result(result) :
    if (result) :
        print('The tree is a Binary Search Tree') 
    else :
        print('The tree is NOT a Binary Search Tree')
        
    
if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]


    #Test for different number of nodes in the tree
    for num_elems in range (1, MAX_NUM_NODES_IN_TREE + 1):
        #Construct the tree based on the data stored in the number list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree: ')
        PrintTreeHelper.print_tree(root, num_elems)

        #Verify if the tree is binary search tree. Verification should pass
        prev_node_list = [None]
        result = TreeNode.is_bst(root, prev_node_list)
        print_result(result)
        if (not result):
            handle_error()


        print('_____________________________________________________')



    print('Test passed')
    














