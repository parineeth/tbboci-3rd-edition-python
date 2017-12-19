
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





MAX_INT = 1000000

def handle_error() :
    print('Test failed ')
    sys.exit(1)



#n: total number of nodes in the binary search tree
#Return value: Number of unique binary search trees that can be constructed 
#with n nodes
def find_num_unique_bst(n) :
    if (n <= 2):
        return n

    num_bst = [0] * (n+1)

    num_bst[0] = 1  #We are making this 1 to simplify the calculation
    num_bst[1] = 1
    num_bst[2] = 2

    for  i in range(3, n+1):
        #the left sub-tree size can vary from 0 to i-1 
        #(one node has to be reserved for root)
        for  left_sub_tree_size in range(i):
            #Subtract the left subtree size and the root node to 
            #get right subtree size
            right_sub_tree_size = i - 1 - left_sub_tree_size

            num_bst[i] += (num_bst[left_sub_tree_size] * 
                        num_bst[right_sub_tree_size])
        
    return num_bst[n]






def test(n, expected_result) :
    result = find_num_unique_bst(n)

    print('Number of unique BST with {} nodes = {}'.format(n, result) )

    if (result != expected_result):
        handle_error()

    print('')  




if (__name__ == '__main__'):
    #catalan numbers
    test(1, 1)
    test(2, 2)
    test(3, 5)
    test(4, 14)
    test(5, 42)
    test(6, 132)
    test(7, 429)

    print('Test passed')



