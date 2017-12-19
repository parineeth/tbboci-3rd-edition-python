
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
    

    @staticmethod
    def print_data(data) :
        print('{} '.format(data) , end='')
    

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




    #cur_node: current node in the tree being processed
    #cur_level: the depth of the current node. Root node of tree has a level of 0
    #max_level_list: max_level_list[0] has the maximum level seen in the tree so
    #   far. We pass -1 for the root node
    @staticmethod
    def print_right_view(cur_node, cur_level, max_level_list) :
        if (not cur_node):
            return

        #If the current node is the first node we have observed in current level,
        #then print it
        if (max_level_list[0] < cur_level) :
            TreeNode.print_data(cur_node.data)
            max_level_list[0] = cur_level

        #First expand the right child and then the left child   
        TreeNode.print_right_view(cur_node.right, cur_level + 1, max_level_list)
        TreeNode.print_right_view(cur_node.left, cur_level + 1, max_level_list)







MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)


if (__name__ == '__main__'):
    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree
    for  num_elems in range(1, MAX_NUM_NODES_IN_TREE+1):

        #construct the tree using the number_list
        root1 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root1, num_elems)

        #Print the right view nodes
        max_level_list = [-1]
        print('The right view nodes are : ', end='')
        TreeNode.print_right_view(root1, 0, max_level_list)

        print('\n__________________________________________\n')




    print('Test passed')




