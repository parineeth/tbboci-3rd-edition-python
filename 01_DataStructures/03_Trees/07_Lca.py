
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
        self.depth = 0
        self.left = None
        self.right = None
        self.parent = None
    

    
    @staticmethod
    def construct_bst(parent, values, low, high, node_list) :

        if (low > high) :
            return None
        
        middle = (low + high) // 2

        new_node = TreeNode()

        new_node.data = values[middle]

        new_node.parent = parent

        if (not parent):
            new_node.depth = 0
        else:
            new_node.depth = parent.depth + 1

        new_node.left = TreeNode.construct_bst(new_node, values, low, middle - 1, node_list)

        new_node.right = TreeNode.construct_bst(new_node, values, middle + 1, high, node_list)

        node_list[middle] = new_node

        return new_node

    


    #Find the Least Common Ancestor of a BINARY SEARCH TREE
    #ancestor: the current ancestor node (root node is passed by the caller for first time)
    #n1 and n2 are two nodes in the tree whose least common ancestor should be found
    #Return value - least common ancestor node of n1 and n2
    @staticmethod
    def bst_lca(ancestor, n1, n2) :
        if (not ancestor or not n1 or not n2):
            return None

        #If the ancestor data is between n1 data and n2 data, then the
        #ancestor is the least common ancestor
        if (n1.data <= ancestor.data and ancestor.data <= n2.data):
            return ancestor

        if (n2.data <= ancestor.data and ancestor.data <= n1.data):
            return ancestor

        #If the ancestor data is greater than n1 data and n2 data, then
        #the LCA will be in the left subtrie of the ancestor
        if (ancestor.data > n1.data and ancestor.data > n2.data):
            return TreeNode.bst_lca(ancestor.left, n1, n2)

        #The ancestor data is less than n1 data and n2 data. So
        #the LCA will be in the right subtrie of the ancestor
        return TreeNode.bst_lca(ancestor.right, n1, n2)
    


    #n: node in the binary tree
    #Return value: depth of the node
    @staticmethod
    def find_depth(n) :
        depth = 0

        while (n.parent) :
            n = n.parent
            depth += 1
    
        return depth
    

    #Find the Least Common Ancestor of a BINARY TREE
    #n1 and n2 are two nodes in the tree
    #Return value: least common ancestor node of n1 and n2
    @staticmethod
    def lca(n1, n2):
        depth1 = TreeNode.find_depth(n1)
        depth2 = TreeNode.find_depth(n2)

        # If n1 is deeper than n2, then move n1 up the tree
        #till the depth of n1 and n2 match
        while (depth1 > depth2) :
            n1 = n1.parent
            depth1 -= 1
    
        # If n2 is deeper than n1, then move n2 up the tree
        #till the depth of n1 and n2 match
        while (depth2 > depth1) :
            n2 = n2.parent
            depth2 -= 1
    
        #Move n1 and n2 up the tree until a common node is found
        while (n1 != n2 ) :
            n1 = n1.parent
            n2 = n2.parent
    
        return n1
    
    





MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)



if (__name__ == '__main__'):

    node_list = [None] * MAX_NUM_NODES_IN_TREE

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree
    for num_elems in range(MAX_NUM_NODES_IN_TREE + 1) :
        #Construct the tree based on the data stored in the number list
        #the nodes will also be stored in the node_list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1, node_list)

        print('Printing the tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        #Generate all pairs of nodes in the tree using the node_list
        for i in range(num_elems):
            for j in range(i+1, num_elems) :

                #Find the Least Common Ancestor for the two nodes
                #using the algorithm for the BINARY TREE.
                #We have created a Binary Search Tree which is also a Binary Tree
                #So we can apply the BINARY TREE algo for a BST
                lca1 = TreeNode.lca(node_list[i], node_list[j])

                #There is a different algo to find the LCA that is 
                #applicable only for BINARY SEARCH TREE. 
                #Since we have created a Binary Search Tree, use the algo for BST 
                lca2 = TreeNode.bst_lca(root, node_list[i], node_list[j])

                #The two results should match
                if (lca1 != lca2):
                    handle_error()

                print('Least Common Ancestor of {} and {} = {}'.format(node_list[i].data,
                    node_list[j].data, lca1.data) )
    

        print('_____________________________________________________')

        

        
    print('Test passed')
    













