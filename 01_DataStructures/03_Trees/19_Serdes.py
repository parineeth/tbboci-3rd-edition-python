
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

SPECIAL_VALUE = -1

class TreeNode(object): 

    

    def __init__ (self, val=0): 
        data = val
        left = None
        right = None
        parent = None
    

    #cur_node: current node of the binary tree
    #fo: file object to store the binary tree
    #Return value: 0 on sucess 
    @staticmethod
    def serialize_tree(cur_node, fo) :
        #If cur_node is None, then store the special value and return
        if (not cur_node) :
            fo.write(str(SPECIAL_VALUE) + '\n')
            return 0
    

        #Traverse the nodes in pre-order
        #First write the data of the node into the file
        fo.write(str(cur_node.data) + '\n')

        #Traverse the left subtree
        TreeNode.serialize_tree(cur_node.left, fo)

        #Traverse the right subtree
        TreeNode.serialize_tree(cur_node.right, fo)

        return 0


    #fo: file object to read the binary tree data
    #Return value: the reconstructed node of the binary tree
    @staticmethod
    def deserialize_tree(fo):
        #Read the data from the line in the file
        value = int(fo.readline())

        #If the special value is read, then return None 
        if (value == SPECIAL_VALUE):
            return None

        #Traverse in pre-order
        #Store the value read from the file in the new_node
        new_node = TreeNode()
        new_node.data = value

        new_node.left = TreeNode.deserialize_tree(fo) #Construct left subtree

        new_node.right = TreeNode.deserialize_tree(fo) #Construct right sub-tree

        return new_node



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
    

    @staticmethod
    def are_trees_identical(n1, n2) :
        if (not n1 and not n2):
            return True

        if ( (n1 and not n2) or (not n1 and n2)):
            return False

        if (n1.data != n2.data):
            return False

        if (not TreeNode.are_trees_identical(n1.left, n2.left)):
            return False

        if (not TreeNode.are_trees_identical(n1.right, n2.right)):
            return False

        return True
    







MAX_NUM_NODES_IN_TREE = 10



def handle_error() :
    print('Test failed')
    sys.exit(0)


if (__name__ == '__main__'):
    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    for  num_elems in range(1, MAX_NUM_NODES_IN_TREE+1):

        root1 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        fout = open('serial_tree.txt', 'w')
        TreeNode.serialize_tree(root1, fout)
        fout.close()


        fin = open('serial_tree.txt', 'r')
        root2 = TreeNode.deserialize_tree(fin)
        fin.close()

        if (not TreeNode.are_trees_identical(root1, root2)):
            handle_error()


    print('Test passed ')














