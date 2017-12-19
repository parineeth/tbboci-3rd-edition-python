
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
from PrintTreeHelper import PrintTreeHelper


class TreeNode(object):

    def __init__(self, val = 0) :
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
    



    #cur_node: current node of the binary tree 
    #above_sum: sum of the nodes from root to the parent of current node
    #k: the threshold path value for retaining the nodes
    #Return value: length of the longest path from root to leaf in which current 
    #       node is present
    @staticmethod
    def k_heavy_path(cur_node, above_sum, k):
        if (not cur_node):
            return above_sum

        above_sum += cur_node.data

        #Find longest path in left sub-tree that contains current node
        max_left_path = TreeNode.k_heavy_path(cur_node.left, above_sum, k)

        #If longest left sub-tree path is below threshold, prune left sub-tree
        if (max_left_path < k):
            cur_node.left = None

        #Find longest path in right sub-tree that contains current node
        max_right_path = TreeNode.k_heavy_path(cur_node.right, above_sum, k)

        #If longest right sub-tree path is below threshold, prune right sub-tree
        if (max_right_path < k):
            cur_node.right = None

        #longest_path is the maximum of max_left_path and max_right_path
        longest_path = max(max_left_path, max_right_path)

        return longest_path



    




MAX_NUM_NODES_IN_TREE = 10
MAX_NODE_VALUE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)





#Verify if all paths from the root to any leaf has a path sum >= K
def verify_path(cur_node, top_sum, K) :
    if (not cur_node):
        return top_sum

    top_sum += cur_node.data

    max_left_path = verify_path(cur_node.left, top_sum, K)
    max_right_path = verify_path(cur_node.right, top_sum, K)

    #Only paths whose path sum is >= K should be present in the tree
    if (max_left_path < K and max_right_path < K):
        handle_error()

    return max (max_left_path, max_right_path)




def test() :
    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]
    

    #Test for different number of elements in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1) :

        #Construct the tree from the list
        root = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Original tree:')
        PrintTreeHelper.print_tree(root, num_elems)

        K = 20

        #if k_heavy_path returns a value less than K, then there is no path from
        #the root to any leaf whose path sum is >= K. So the root itself will get removed.
        #In this case set the root to NULL
        if (TreeNode.k_heavy_path(root, 0, K) < K):
            root = None

        print('After retaining only K-Heavy paths, K = {}'.format(K) )
        PrintTreeHelper.print_tree(root, num_elems)

        verify_path(root, 0, K)


        print('___________________________________________________')

    

    


if (__name__ == '__main__'):
    test()
    print('Test passed \n')
    













