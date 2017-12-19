
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper

try: 
    import queue
except ImportError:
    import Queue as queue


MAX_NUM_NODES_IN_TREE = 10


class TreeNode(object):
    nr_result_list = [0] * MAX_NUM_NODES_IN_TREE
    nr_index = 0

    def __init__ (self, val = 0): 
        self.data = val
        self.left = None
        self.right = None
        self.parent = None  



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

    

    @staticmethod
    def handle_error() :
        print('Test failed')
        sys.exit(1)
    


    @staticmethod
    def process(cur_node) :
        TreeNode.nr_result_list[TreeNode.nr_index] = cur_node.data
        TreeNode.nr_index += 1
        print('{} '.format(cur_node.data) , end='')
    

    #root: root node of the binary tree
    #s: stack for storing the nodes for in-order traversal
    @staticmethod
    def non_recursive_in_order(root, s) :
        cur_node = root
        while (cur_node or not s.empty()) :
            if (cur_node) :
                #push the current node onto stack
                s.put(cur_node)

                #Traverse to the left sub-tree
                cur_node = cur_node.left

            else :
                #pop the node from stack and process it
                cur_node = s.get()

                #process or print the node in-order
                TreeNode.process(cur_node)

                #Traverse to the right sub-tree
                cur_node = cur_node.right
        
        

    

    @staticmethod
    def recursive_in_order(node) :
        if (not node):
            return

        TreeNode.recursive_in_order(node.left)

        if (TreeNode.nr_result_list[TreeNode.nr_index] != node.data):
            handle_error()

        TreeNode.nr_index += 1

        TreeNode.recursive_in_order(node.right)
    






def test01() :

    s = queue.LifoQueue()

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]
    

    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        #Construct the tree
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #Perform the non-recursive in-order traversal. Store the node data
        #in nr_result_list during the traversal
        TreeNode.nr_index = 0
        print('Non Recursive In-order : ', end='')
        TreeNode.non_recursive_in_order(root, s)

        #Verify the non-recursive in-order result stored in nr_result_list
        #by comparing it with the recursive in-order traversal
        TreeNode.nr_index = 0
        TreeNode.recursive_in_order(root)

        print('\n__________________________________________________')

    

    

    



if (__name__ == '__main__'):
    test01()
    print('Test passed')
    


