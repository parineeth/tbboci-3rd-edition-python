
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper



class TreeNode(object):


    def __init__(self, val=0): 
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
    



    #n: root of the binary search tree
    #Returns - The maximum element of the binary search tree
    @staticmethod
    def get_max(n) :
        if (not n):
            return None

        #The rightmost node has the maximum value
        while (n.right):
            n = n.right

        return n
    



    #x: any node in the binary search tree 
    #Return value: the node previous to node x
    @staticmethod
    def get_previous(x) :
        #Handle Case-1, left child exists
        if (x.left) :
            y = x.left
            while (y.right) :
                y = y.right
        
            return y
    
        #Handle Case-2, left child doesn't exist
        y = x.parent
        while (y and y.left == x) :
            x = y
            y = y.parent
    
        return y






    #x: any node in the binary search tree
    #Return value: the node after node x
    @staticmethod
    def get_next(x) :
        #Handle Case-1: right child exists
        if (x.right) :
            y = x.right
            while (y.left) :
                y = y.left
        
            return y
    
        #Handle Case-2: right child doesn't exist
        y = x.parent
        while (y and y.right == x) :
            x = y
            y = y.parent
    
        return y



    






MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)



def print_node (n) :
    if (n):
        print(n.data, end='')
    else:
        print('None', end='')


#Verify the previous and next functions
def verify_previous_next(cur_node, num_elems) :

    if (not cur_node):
        return

    #Get the previous and next node for the current node
    prev_node = TreeNode.get_previous(cur_node)
    next_node = TreeNode.get_next(cur_node)

    print('Cur node = ', end='')
    print_node(cur_node)

    print(': Prev node = ', end='')
    print_node(prev_node)

    print(', Next node = ', end='')
    print_node(next_node)
    print('')

    if (cur_node.data == 0) :
        #If cur_node has data = 0, it is the first node
        #The previous node should be None
        if (prev_node):
            handle_error()
    else :
        #cur_node->data should be prev_node->data + 1
        if (prev_node.data + 1 != cur_node.data):
            handle_error()
    

    if (cur_node.data == num_elems - 1) :
        #If cur_node has data = num_elems - 1, it is the last node
        #The next node should be None
        if (next_node) :
            handle_error()
    else :
        #next_node->data should be cur_node->data + 1 
        if (cur_node.data + 1 != next_node.data):
            handle_error()
    

    verify_previous_next(cur_node.left, num_elems)
    verify_previous_next(cur_node.right, num_elems)

        

if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):

        #construct the Binary Search Tree
        root1 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root1, num_elems)

        #verify the get_previous and get_next functions
        verify_previous_next(root1, num_elems)

        print('____________________________________________________')


    print('Test passed')














