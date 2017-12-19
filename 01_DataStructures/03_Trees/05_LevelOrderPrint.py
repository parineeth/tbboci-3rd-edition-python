
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
    def print_data(data): 
        print('{} '.format(data) , end='')
    

    #root: root node of the tree 
    #q: python Queue object used for printing the tree
    @staticmethod
    def print_level_order(root, q):
        if (not root):
            return

        #Add the root node to the empty queue
        q.put(root)
        num_nodes_in_cur_level = 1
        num_nodes_in_next_level = 0

        #Process the nodes in the queue in Breadth First manner
        while (not q.empty()) :
            #Remove the node at the head of the queue
            n = q.get()

            TreeNode.print_data(n.data) #print the data in the node

            #Add the left child to the queue
            if (n.left) :
                q.put(n.left)
                num_nodes_in_next_level += 1
        
            #Add the right child to the queue
            if (n.right) :
                q.put(n.right)
                num_nodes_in_next_level += 1
        
            num_nodes_in_cur_level -= 1

            #go to next line, if all nodes in current level are processed
            if (num_nodes_in_cur_level == 0) :
                print('')
                num_nodes_in_cur_level = num_nodes_in_next_level
                num_nodes_in_next_level = 0
        
    
    


    





MAX_NUM_NODES_IN_TREE = 10


def handle_error(): 
    print('Test failed')
    sys.exit(1)


if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)] 

    #Test for different number of nodes in the tree:
    for num_elems in range (1, MAX_NUM_NODES_IN_TREE + 1) :

        #Construct the tree based on the data stored in the number list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree')
        PrintTreeHelper.print_tree(root, num_elems)

        #Use the queue provided by python
        q = queue.Queue()

        print('Level order is:')
        TreeNode.print_level_order(root, q)

        print('_________________________________________________________')




    print('Test passed')
    













