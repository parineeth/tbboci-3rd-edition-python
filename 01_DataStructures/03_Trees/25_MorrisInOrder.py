
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper



MAX_NUM_NODES_IN_TREE = 10


class TreeNode(object):
    morris_result_list = [0] * MAX_NUM_NODES_IN_TREE
    morris_index = 0

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
    def print_morris(cur_node) :
        TreeNode.morris_result_list[TreeNode.morris_index] = cur_node.data
        TreeNode.morris_index += 1
        print('{} '.format(cur_node.data) , end='')
    

    #root: root node of the tree
    @staticmethod
    def morris_in_order(root):
        cur_node = root
        while (cur_node) :
            #If cur_node has no left sub_tree, then print/process the 
            #cur_node then move over to cur_node.right and continue
            if (not cur_node.left) :
                TreeNode.print_morris(cur_node)
                cur_node = cur_node.right
                continue
             

            #The cur_node has a left sub-tree. First store the left  
            #predecessor of current node in left_pre. The left predecessor 
            #can be found by traversing to the left of current node and 
            #then repeatedly going to the right till we hit a leaf node
            left_pre = cur_node.left
            while (left_pre.right and left_pre.right != cur_node) :
                left_pre = left_pre.right


            if (not left_pre.right) :
                #If left predecessor is None, it means we have   
                #not yet traversed the left sub-tree of current node.  
                #So create a thread from left_pre.right to the current 
                #node to remember that on reaching left_pre the next
                #in-order node is cur_node. Then proceed to cur_node.left
                left_pre.right = cur_node
                cur_node = cur_node.left
            else :
                #If left predecessor is not None, then it  
                #means that we have finished traversing the left 
                #sub-tree of current node. So remove the thread from 
                #left_pre.right to current node. The current node is 
                #the in-order node to be processed. So process it and 
                #then move to right sub-tree of cur_node
                left_pre.right = None
                TreeNode.print_morris(cur_node)
                cur_node = cur_node.right
    
    

    @staticmethod
    def recursive_in_order(node) :
        if (not node):
            return

        TreeNode.recursive_in_order(node.left)

        if (TreeNode.morris_result_list[TreeNode.morris_index] != node.data):
            handle_error()

        TreeNode.morris_index += 1

        TreeNode.recursive_in_order(node.right)
    






def test01() :

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]
    

    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
        #Construct the tree
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #Perform the morris in-order traversal. Store the node data
        #in morris_result_list during the traversal
        TreeNode.morris_index = 0
        print('Morris In-order : ', end='')
        TreeNode.morris_in_order(root)

        #Verify the morris in-order result stored in morris_result_list
        #by comparing it with the recursive in-order traversal
        TreeNode.morris_index = 0
        TreeNode.recursive_in_order(root)

        print('\n__________________________________________________')

    






if (__name__ == '__main__'):
    test01()
    print('Test passed')
    


