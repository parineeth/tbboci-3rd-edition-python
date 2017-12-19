
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

        if (low > high):
            return None

        middle = (low + high) // 2

        new_node = TreeNode()
        if (not new_node):
            return None

        #Construct the new node using the middle value
        new_node.data = values[middle]
        new_node.parent = parent

        if (parent):
            new_node.depth = parent.depth + 1
        else:
            new_node.depth = 0

        #Construct the left sub-tree using values[low] to values[middle-1]
        new_node.left = TreeNode.construct_bst(new_node, values, low, middle - 1)

        #Construct the right sub-tree using values[middle+1] to values[high]
        new_node.right = TreeNode.construct_bst(new_node, values, middle + 1, high)

        return new_node
    

    #Helper function that compares the nodes 
    #n1: node belonging to the main tree
    #n2: node belonging to sub-tree being searched
    #Return value: True if sub-tree of n1 matches sub-tree of n2. False otherwise
    @staticmethod
    def compare_nodes(n1, n2) :
        if (not n1 and not n2):
            return True

        if (not n1 or not n2):
            return False

        if (n1.data != n2.data):
            return False

        return (TreeNode.compare_nodes(n1.left, n2.left) 
            and TreeNode.compare_nodes(n1.right, n2.right))




    #Main function that checks if tree under root2 is a subtree of tree under root1
    #root1: main tree node
    #root2: root of the sub-tree being searched
    #Return value: True if tree under root2 is present in tree under root1
    @staticmethod
    def is_sub_tree(root1, root2) :
        #empty tree is treated as a sub-tree of the main tree
        if(not root2):
            return True

        if (not root1):
            return False

        if (TreeNode.compare_nodes(root1, root2)):
            return True

        #Check if tree of root2 is present in left sub-tree of root1 
        #or right sub-tree of root1
        return (TreeNode.is_sub_tree(root1.left, root2) 
            or TreeNode.is_sub_tree(root1.right, root2))

     








MAX_NUM_NODES_IN_TREE = 10
INVALID_VALUE = 100

def handle_error() :
    print('Error occured')
    sys.exit(1)
    

if (__name__ == '__main__'):
    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :

        #Construct the sub_tree to be searched
        sub_tree_root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        #Create the main tree node
        main_tree_root = TreeNode()
        main_tree_root.data =  INVALID_VALUE
        main_tree_root.left = None
        main_tree_root.right = None

        #main tree root has an invalid value and won't match with any of the 
        #sub-tree nodes. So checking for sub-tree should fail
        if (TreeNode.is_sub_tree(main_tree_root, sub_tree_root)):
            handle_error()

        #Connect the sub-tree root to the left of the main-tree. We should
        #now find the sub-tree in the main tree
        main_tree_root.left = sub_tree_root 
        main_tree_root.right = None
        if (not TreeNode.is_sub_tree(main_tree_root, sub_tree_root)):
            handle_error()

        #Connect the sub-tree root to the right of the main-tree. We should
        #now find the sub-tree in the main tree
        main_tree_root.left = None 
        main_tree_root.right = sub_tree_root
        if (not TreeNode.is_sub_tree(main_tree_root, sub_tree_root)):
            handle_error()

        #We should find the sub-tree in the sub-tree itself
        if (not TreeNode.is_sub_tree(sub_tree_root, sub_tree_root)):
            handle_error()

        #If sub-tree is None, then we should still treat it as a sub-tree of main tree
        if (not TreeNode.is_sub_tree(main_tree_root, None)):
            handle_error()

        #If main-tree is None, then we shouldn't find the sub-tree
        if (TreeNode.is_sub_tree(None, sub_tree_root)):
            handle_error()



    print('Test passed')

    


