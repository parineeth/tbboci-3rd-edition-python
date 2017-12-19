
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
    



    #Helper function to find the vertical sum
    #cur_node: current node being processed in the binary tree
    #col: column of the current node
    #sum_list: list containing the sum of nodes in each column
    @staticmethod
    def process_sum(cur_node, col, sum_list):

        if (not cur_node):
            return

        sum_list[col] += cur_node.data

        #column number of left child is col - 1
        TreeNode.process_sum(cur_node.left, col - 1, sum_list)

        #column number of right child is col+1
        TreeNode.process_sum(cur_node.right, col +  1, sum_list)


    #Main function to find the vertical sum
    #root: root of the binary tree 
    #Return values: list which contains the vertical sum 
    @staticmethod
    def compute_vertical_sum(root):
        if (not root):
            return None

        #Compute the number of left columns
        cur_node = root.left
        num_left_cols= 0
        while (cur_node) :
            num_left_cols += 1
            cur_node = cur_node.left
    
        #Compute the number of right columns
        cur_node = root.right
        num_right_cols = 0
        while (cur_node) :
            num_right_cols += 1
            cur_node = cur_node.right
    

        total_num_cols = num_left_cols + num_right_cols + 1

        #Dynamically create the list for storing the column sum based on total 
        #columns
        sum_list = [0] * total_num_cols

        root_col = num_left_cols

        #Compute the vertical sum starting with the root
        TreeNode.process_sum(root, root_col, sum_list)

        return sum_list





MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)
    

if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]


    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :

        #construct the tree
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        #Compute the vertical sum
        sum_list = TreeNode.compute_vertical_sum(root)

        print('Vertical sum is:', end='')

        for vsum in sum_list :
            print('{} '.format(vsum) , end='')
    

        print('\n___________________________________________________')



    print('Test passed')
    













