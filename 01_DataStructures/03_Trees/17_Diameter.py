
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper



class TreeNode(object):

    def __init__(self, val = 0): 
        data = val
        left = None
        right = None
        parent = None
    

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
    


    #cur_node: current node of the tree 
    #diameter: diameter of the tree computed till now is passed here
    #Return values: height of cur_node and diameter of the tree
    @staticmethod
    def find_diameter(cur_node, diameter):
        if (not cur_node) :
            height = 0
            return height, diameter 
    
        #Find the height of the left sub-tree
        left_height, diameter = TreeNode.find_diameter(cur_node.left, diameter)

        #Find the height of the right sub-tree
        right_height, diameter = TreeNode.find_diameter(cur_node.right, diameter)

        #Calculate height of cur_node
        height = 1 + max(left_height, right_height)

        #Calculate longest path between any two leafs passing through cur_node 
        longest_path = left_height + right_height + 1

        #If the length of longest path through cur_node is greater than 
        #the current diameter then assign it to the diameter
        if (longest_path > diameter):
            diameter = longest_path

        return height, diameter






MAX_NUM_NODES_IN_TREE = 10
MAX_NODE_VALUE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)




def test() :

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of elements in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :
        #Construct the tree from the list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #Find the diameter
        diameter = 0
        height, diameter = TreeNode.find_diameter(root, diameter)

        print('Height = {}, Diameter = {}'.format(height, diameter) )

        print('___________________________________________________')

    

    




if (__name__ == '__main__'):
    test()
    print('Test passed')














