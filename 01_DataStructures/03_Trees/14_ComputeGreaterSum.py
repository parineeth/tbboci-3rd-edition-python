
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper



class TreeNode(object):



    def __init__(self, val=0): 
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
    


    #cur_node: current node of the binary search tree 
    #bst_sum_list: has single element that stores the sum of nodes greater 
    #       than current node
    @staticmethod
    def compute_sum_of_greater_nodes(cur_node, bst_sum_list):
        if (not cur_node):
            return

        #Since greater elements are in the right sub-tree, first process the
        #right sub-tree
        TreeNode.compute_sum_of_greater_nodes(cur_node.right, bst_sum_list)

        #Assign the sum of the greater nodes
        cur_node.sum = bst_sum_list[0]

        #Add the current node's data to the sum
        bst_sum_list[0] += cur_node.data

        #Process the left sub-tree
        TreeNode.compute_sum_of_greater_nodes(cur_node.left, bst_sum_list)

    




MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)




def verify_sum (cur_node, sum_list, index_list) :

    if (not cur_node):
        return

    verify_sum(cur_node.left, sum_list, index_list)

    print('Node data = {}, Greater Sum = {}'.format(cur_node.data, cur_node.sum) )

    current_index = index_list[0]
    if (sum_list[current_index] != cur_node.sum):
        handle_error()

    index_list[0] += 1

    verify_sum(cur_node.right, sum_list, index_list)


if (__name__ == '__main__'):

    sum_list = [0] * MAX_NUM_NODES_IN_TREE
    bst_sum_list = [0]
    index_list = [0]

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]


    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :

        #construct the tree using the number_list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #For each node, compute the sum of greater nodes and store in the node itself 
        bst_sum_list[0] = 0
        TreeNode.compute_sum_of_greater_nodes(root, bst_sum_list)

        #Compute the greater sum of the number list and store it in sum_list
        totalSoFar = 0
        for i in range(num_elems - 1, -1, -1) :
            sum_list[i] = totalSoFar
            totalSoFar += number_list[i] 
    

        #Verify the greater sum stored in the nodes of the tree with the sum_list
        index_list[0] = 0
        verify_sum(root, sum_list, index_list)

        print('___________________________________________________')





    print('Test passed successfully')














