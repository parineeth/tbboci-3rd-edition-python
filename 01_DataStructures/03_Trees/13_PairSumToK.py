
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
    


    # n: root of the binary search tree
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
    





    #x: any node in the binary search tree
    #Return value:  the node next to node x
    @staticmethod
    def get_next(x) :

        #Handle Case - 1
        if (x.right) :
            y = x.right
            while (y.left) :
                y = y.left
            
            return y
        

        #Handle Case - 2
        y = x.parent
        while (y and y.right == x) :
            x = y
            y = y.parent
        

        return y
    



    #root: root of the binary search tree
    #k: sum of two nodes should equal k
    #Return value: list with the 2 tree nodes which sum up to k if they 
    #       exist, None otherwise
    @staticmethod
    def find_pair_sum_to_k(root, k) :
        if (not root):
            return None

        #Store the leftmost node in n1
        n1 = root
        while (n1.left):
            n1 = n1.left

        #Store the right most node in n2
        n2 = root
        while (n2.right):
            n2 = n2.right

        #Process the tree by picking one node from left and one node from right
        while (n1 != n2) :
            current_sum = n1.data + n2.data

            #check if the left node and right node sum to k
            if (current_sum == k) :
                return  [n1, n2]
        
            if (current_sum < k) :
                #Pick the next higher value node from the left
                n1 = TreeNode.get_next(n1)
            else :
                #Pick the next smaller value from the right
                n2 = TreeNode.get_previous(n2)
        
        return None




    





MAX_NUM_NODES_IN_TREE = 10


def handle_error() :
    print('Test failed')
    sys.exit(1)



#Returns the two value that sum to K in the number_list.
#If there are no pair of values that sum to K, return value will be None
def find_list_sum_to_k(number_list, num_elems, K) :
    for i  in range(num_elems - 1) :
        for j in range(num_elems - 1, i, -1) :
            if (number_list[i] + number_list[j] == K) :
                result = [number_list[i], number_list[j]]
                return result
            
    return None


def check_condition(condition) :
    if (not condition):
        handle_error()


if (__name__ == '__main__'):

    #number_list contains numbers in ascending order from 0 to MAX_NUM_NODES_IN_TREE
    number_list = [i for i in range(MAX_NUM_NODES_IN_TREE)]


    #Test for different number of nodes in the tree
    for num_elems in range(1, MAX_NUM_NODES_IN_TREE + 1):

        #construct the Binary Search Tree using the number_list
        root1 = TreeNode.construct_bst(None, number_list, 0, num_elems - 1)

        print('Printing tree:')
        PrintTreeHelper.print_tree(root1, num_elems)

        #Test for different values of K
        for K in range ((2 * num_elems) + 1) :

            #find the pair of nodes that sum to K in the tree
            node_result = TreeNode.find_pair_sum_to_k(root1, K)

            if (not node_result) :
                n1 = None
                n2 = None
            else :
                n1 = node_result[0]
                n2 = node_result[1]
        

            #find the two numbers that add upto K in the number list
            expected_result = find_list_sum_to_k(number_list, num_elems, K)
        
            if (not expected_result) :
                num1 = -1
                num2 = -1
            else :
                num1 = expected_result[0]
                num2 = expected_result[1]
        

            #The result from the tree and the list should match
            if (not n1 or num1 == -1) :
                check_condition(not n1)
                check_condition(not n2)
                check_condition(num1 == -1)
                check_condition(num2 == -1)
            else :

                check_condition(n1.data == num1)
                check_condition(n2.data == num2)

                print('{} + {} = {}'.format(n1.data, n2.data, K) )
        


        print('__________________________________________')

    

        
    print('Test passed')
    













