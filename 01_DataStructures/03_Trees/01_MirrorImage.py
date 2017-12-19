
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
    #cur_node: current node of the tree whose mirror image should be computed
    def compute_mirror_image(cur_node): 
        if (cur_node) :
            #Swap the left child and right child of the current node
            cur_node.left, cur_node.right = cur_node.right, cur_node.left

            #Recursively compute the mirror image 
            TreeNode.compute_mirror_image(cur_node.left)
            TreeNode.compute_mirror_image(cur_node.right)
    
    


    @staticmethod
    def compare_nodes(n1, n2): 
        if (not n1 and not n2):  #If both the nodes are None
            return True  # return symmetric

        #If one node is None and the other is not None
        if ( (n1 and not n2) or (not n1 and n2)):  
            return False #return not symmetric

        if (n1.data != n2.data): #If data of two nodes don't match
            return False # return not symmetric 
    
        if (not TreeNode.compare_nodes(n1.left, n2.right)): 
            return False

        if (not TreeNode.compare_nodes(n1.right, n2.left)): 
            return False

        return True #Return symmetric


    @staticmethod
    #Returns True if the tree is symmetric, False otherwise
    def is_symmetric(root): 
        if (not root):
            return True

        return TreeNode.compare_nodes(root.left, root.right)
        

    





MAX_NUM_NODES_IN_TREE = 10

def handle_error(): 
    print('Test failed')
    sys.exit(1)
    


if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree:
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :

        #Construct the tree based on the data stored in the number list
        root1 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        #Construct an identical tree and store root in root2
        root2 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Original Tree:')         
        PrintTreeHelper.print_tree(root1, num_elems)

        #Compute the mirror image
        TreeNode.compute_mirror_image(root2)

        print('Mirror Image:')          
        PrintTreeHelper.print_tree(root2, num_elems)

        #Root1 and Root2 have trees that are mirror images of each other.
        #So if we now have a main_root whose left child is root1 and right child is root2:
        #then main_root should be symmetric
        main_root = TreeNode()
        main_root.left = root1
        main_root.right = root2

        if (not TreeNode.is_symmetric(main_root)):
            handle_error()

        print('___________________________________________')



        
    print('Test passed')
    













