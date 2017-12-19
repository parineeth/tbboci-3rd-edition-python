
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
    



    #x:  any node in the binary search tree 
    #Return value:  the node previous to node x
    @staticmethod
    def get_previous(x) :
        #Handle Case - 1
        if (x.left) :
            y = x.left
            while (y.right) :
                y = y.right
            
            return y
        

        #Handle Case - 2
        y = x.parent
        while (y and y.left == x) :
            x = y
            y = y.parent
        
        return y
    





    #root: the root node of the binary search tree
    #k: indicates the kth largest value. k >= 1
    #Return value: kth largest node in the binary search tree
    @staticmethod
    def find_kth_largest(root, k) :
        if (not root or k < 1):
            return None

        #Find the node with the maximum value
        n = root
        while (n.right):
            n = n.right

        #Find the k-1 previous nodes 
        for i in range(1, k) :
            n = TreeNode.get_previous(n)
            if (not n) :
                return None
        
        return n



    




MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)


if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]

    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):
    
        #construct the Binary Search Tree
        root1 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root1, num_elems)

        for k in range(1, num_elems + 1) :
            #Find the kth largest. k can take values from 1 to num_elems
            cur_node = TreeNode.find_kth_largest(root1, k)

            print('K =  {}, Kth Largest = {}'.format(k, cur_node.data) )

            #Verify the result returned
            if (cur_node.data != num_elems - k ):
                handle_error()
    

        #If we pass k value that is > than num_elems, we should get NULL
        cur_node = TreeNode.find_kth_largest(root1, num_elems + 1)
        if (cur_node):
            handle_error()

        print('_________________________________________________________')



    print('Test passed')














