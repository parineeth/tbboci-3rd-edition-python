
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



    @staticmethod
    def construct_unbalanced_tree(num_nodes) :

        root = prev_node = None
        for  i in range(num_nodes):
            new_node = TreeNode()
            new_node.data = i

            if (not root):
                root = new_node

            if (prev_node) :
                prev_node.right = new_node
            
            prev_node = new_node
        
    
        return root
    


    #cur_node: cur node of the binary tree being checked
    #Return values: 1. True if the tree is balanced, False otherwise
    #       2. height of the cur_node is also returned
    @staticmethod
    def is_balanced(cur_node) :
        if (not cur_node) :
            height = 0
            return True, height
    
        is_left_balanced, left_height = TreeNode.is_balanced(cur_node.left)
        is_right_balanced, right_height = TreeNode.is_balanced(cur_node.right)

        #To get the height of the current node, we find the maximum of the  
        #left subtree height and the right subtree height and add 1 to it
        height = max(left_height, right_height) + 1

        if (not is_left_balanced or not is_right_balanced):
            return False, height

        #If the difference between height of left subtree and height of
        #right subtree is more than 1, then the tree is unbalanced
        if (abs(left_height - right_height) > 1):
            return False, height
    
        return True, height 








MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)




def print_unbalanced_tree(root) :

    cur_node = root
    count = 0
    while (cur_node) :
        for  i in range(count):
            print('\t', end='')
        
    
        print(cur_node.data)

        count += 1
        cur_node = cur_node.right
    





def print_result(result) :
    if (result) :
        print('The tree is balanced\n\n') 
    else :
        print('The tree is NOT balanced\n')
    



if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in a balanced tree
    for  num_elems in range(1, MAX_NUM_NODES_IN_TREE+1):

        #Construct a balanced tree based on the data stored in the number list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree')
        PrintTreeHelper.print_tree(root, num_elems)

        result, height = TreeNode.is_balanced(root)

        print_result(result)

        if (result != True):
            handle_error()

        print('_____________________________________________________')



    #Test for different number of nodes in a unbalanced tree
    for  num_elems in range(3, MAX_NUM_NODES_IN_TREE+1):

        #Construct an unbalanced tree 
        root = TreeNode.construct_unbalanced_tree(num_elems)

        print_unbalanced_tree(root)

        result, height = TreeNode.is_balanced(root)

        print_result(result)

        if (result != False):
            handle_error()

        print('_____________________________________________________')



    print('Test passed')



