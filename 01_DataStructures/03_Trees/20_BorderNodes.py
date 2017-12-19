
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper




class TreeNode(object):


    def __init__ (self, val = 0): 
        self.data = val
        self.left = None
        self.right = None
        self.parent = None
    


    @staticmethod
    def construct_bst (parent, values, low, high) :
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
    


    @staticmethod
    def print_data(data)    :
        print('{} '.format(data) , end='')
    

    #Print the left border
    @staticmethod
    def print_left_border(cur_node) :
        #Keep traversing left and print the non-leaf nodes
        while (cur_node) :
            #If node has a left or right child, then it is a non-leaf node  
            if (cur_node.left or cur_node.right):
                TreeNode.print_data( cur_node.data)

            cur_node = cur_node.left
    


    #Print the leaf nodes of the tree
    @staticmethod
    def print_leaf_nodes(cur_node) :
        if (not cur_node):
            return

        if (not cur_node.left and not cur_node.right):
            TreeNode.print_data(cur_node.data)

        TreeNode.print_leaf_nodes(cur_node.left)
        TreeNode.print_leaf_nodes(cur_node.right)


    # Print the right border nodes of the tree
    @staticmethod
    def print_right_border(cur_node) :
        if (not cur_node):
            return

        #First reach the deepest right node and then start printing bottom-up
        TreeNode.print_right_border(cur_node.right)

        #If the node has a left or right child, then it is a non-leaf node.
        #So print it
        if (cur_node.left or cur_node.right):
            TreeNode.print_data(cur_node.data)




    #Main function that prints the border nodes of a binary tree
    @staticmethod
    def print_border_nodes(root):
        if (not root):
            return

        TreeNode.print_left_border(root)
        TreeNode.print_leaf_nodes(root)
        TreeNode.print_right_border(root)




    


MAX_NUM_NODES_IN_TREE = 10
    


def handle_error() :
    print('Test failed')
    sys.exit(1)


if (__name__ == '__main__'):
    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):

        #construct the tree using the number_list
        root1 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root1, num_elems)

        #Print the border nodes
        print('The border nodes are : ', end='')

        TreeNode.print_border_nodes(root1)

        print('\n__________________________________________')




    print('Test passed')














