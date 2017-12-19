
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper


class Int(object): 
    def __init__(self, init_val=0): 
        self.value = init_val
    
    



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
    


    #pre_order: list containing the data of nodes of the binary tree in pre-order
    #in_order: list containing the data of nodes of the binary tree in in-order
    #in_start: starting index of current region in the in_order list 
    #in_end: ending index of current region in the in_order list 
    #pre_pos: it is an object. pre_pos.value has the index in the pre-order list 
    #Return value: newly created binary tree node
    @staticmethod
    def construct_tree(pre_order, in_order, in_start, in_end, pre_pos) :
        #Termination condition for recursion
        if (in_start > in_end):
            return None

        # Assign the pivot from pre-order list
        pivot = pre_order[pre_pos.value]

        #Find pivot in in-order list
        for in_location in range(in_start,  in_end + 1) :
            if (in_order[in_location] == pivot) :
                break
        
        #Create the new node and assign the pivot data
        new_node = TreeNode()
        new_node.data = pivot

        #Advance to the next member in the pre-order list
        pre_pos.value += 1

        #First recursively construct the left sub-tree 
        new_node.left = TreeNode.construct_tree(pre_order, in_order, 
                        in_start, in_location - 1, pre_pos)

        #Recursively construct the right sub-tree
        new_node.right = TreeNode.construct_tree(pre_order, in_order, 
                        in_location + 1, in_end, pre_pos)

        return new_node


    




MAX_NUM_NODES_IN_TREE = 10
MAX_NODE_VALUE = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)




def traverse_pre_order(cur_node, in_list, pos) :
    if (not cur_node):
        return

    in_list[pos.value] = cur_node.data
    pos.value += 1

    traverse_pre_order(cur_node.left, in_list, pos)
    traverse_pre_order(cur_node.right, in_list, pos)




def traverse_in_order(cur_node, in_list, pos) :
    if (not cur_node):
        return

    traverse_in_order(cur_node.left, in_list, pos)

    in_list[pos.value] = cur_node.data
    pos.value += 1

    traverse_in_order(cur_node.right, in_list, pos)




def verify_trees(n1, n2) :
    if (not n1 and not n2):
        return

    if ( (not n1 and n2) or (n1 and not n2)):
        handle_error()

    if (n1.data != n2.data):
        handle_error()

    verify_trees(n1.left, n2.left)
    verify_trees(n1.right, n2.right)




def test_01() :

    pos = Int()
    pre_pos = Int()

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of elements in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        #Construct the original tree
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        pre_order = [0] * num_elems 
        in_order = [0] * num_elems

        #Traverse the original tree in pre-order and store the result in list pre_order
        pos.value = 0
        traverse_pre_order(root, pre_order, pos)

        print('Pre-order is : ', end='')
        print(pre_order)

        #Traverse the original tree in in-order and store the result in list in_order
        pos.value = 0
        traverse_in_order(root, in_order, pos)

        print('In-order is : ', end='')
        print(in_order)

        #Re-construct the tree using the pre_order and in_order lists
        in_start = 0
        in_end = num_elems - 1
        pre_pos.value = 0
        assembled_root = TreeNode.construct_tree(pre_order, in_order, in_start, in_end, pre_pos)

        print('Printing tree:\n', end='')
        PrintTreeHelper.print_tree(root, num_elems)

        #Verify if the original tree and reconstructed tree match
        verify_trees(root, assembled_root)

        print('___________________________________________________________________')

    

        


if (__name__ == '__main__'):
    test_01()
    print('Test passed')
    













