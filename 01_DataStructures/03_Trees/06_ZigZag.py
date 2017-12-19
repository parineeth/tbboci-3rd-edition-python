
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


class TreeNode(object):


    def __init__(self, val = 0): 
        self.data = val
        self.left = None
        self.right = None
        self.parent = None
        self.next = None
    
    

    #Recursively Construct a Binary Search Tree from the input list sorted in ascending order
    @staticmethod
    def construct_bst (parent, values, low, high) :

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
    def print_data(data) :
        print('{} '.format(data) , end='')
    


    #Helper function for printing in zig zag order:
    #print_stack: stack used for printing the nodes:
    #store_stack: stack that stores the children of nodes in print_stack
    #left_to_right: if set to 1, left child is stored first followed by right child
    @staticmethod
    def process_stacks(print_stack, store_stack, left_to_right):
        while (not print_stack.empty()) :
            cur_node = print_stack.get()
            TreeNode.print_data(cur_node.data)

            if (left_to_right) :
                if (cur_node.left):
                    store_stack.put(cur_node.left)
                if (cur_node.right):
                    store_stack.put(cur_node.right)
            else :
                if (cur_node.right):
                    store_stack.put(cur_node.right)
                if (cur_node.left):
                    store_stack.put(cur_node.left)
        

    #root: root of the binary tree to be printed spirally
    #s0, s1: stacks used for storing nodes of the binary tree
    @staticmethod
    def print_zig_zag(root, s0, s1):
        if (not root):
            return

        #Push root into stack s0 and start processing
        s0.put(root)

        while (not s0.empty()) :
            #s0 is used for printing. The children of nodes in s0 are
            #stored in s1 in left to right direction
            TreeNode.process_stacks(s0, s1, True)
            print('')

            #s1 is used for printing. The children of nodes in s1 are
            #stored in s0 in right to left direction
            TreeNode.process_stacks(s1, s0, False)
            print('')
    



    





MAX_NUM_NODES_IN_TREE = 10

MAX_NODE_VALUE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)
    


if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree:
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):

        #Construct the tree based on the data stored in the number list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #Use the stack provided by python
        s1 = queue.LifoQueue()
        s2 = queue.LifoQueue()

        print('Zig Zag order is:')
        TreeNode.print_zig_zag(root, s1, s2)

        print('___________________________________________________\n')




    print('Test passed')
    













