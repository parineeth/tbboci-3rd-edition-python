
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

MAX_NUM_COLS_ON_SCREEN = 40

class PrintTreeHelper(object): 

    #Helper function for printing the binary tree:
    #cur_node: current node being processed in pre-oder traversal
    #cur_depth: depth of the current node. Depth of root is 0
    #max_depth: maximum depth of the tree observed so far
    #print_list: The nodes of the binary tree are stored in this list. print_list[0] will contain the root.
    #   print_list[1] will store the left child of root. print_list[2] will store right child of root and so on
    #   In case, we get a None node while traversing the tree, we will still store it:
    #pos: position of the current node in the print_list 
    #Returns: Maximum depth of the tree 
    @staticmethod
    def fill_print_list(cur_node, cur_depth, max_depth, print_list, pos): 

        #Store the node in the list (even if the node is None):
        print_list[pos] = cur_node

        if (not cur_node):
            return max_depth

        if (cur_depth > max_depth):
            max_depth = cur_depth

        left_max_depth = PrintTreeHelper.fill_print_list(cur_node.left, cur_depth + 1, max_depth, 
                            print_list, (2*pos) + 1)
        if (left_max_depth > max_depth):
            max_depth = left_max_depth
        
        right_max_depth = PrintTreeHelper.fill_print_list(cur_node.right, cur_depth + 1, max_depth, 
                            print_list, (2*pos) + 2)
        if (right_max_depth > max_depth):
            max_depth = right_max_depth
        
        return max_depth



    #Main function for printing the tree:
    @staticmethod
    def print_tree(root, max_num_nodes_in_tree):
        if (max_num_nodes_in_tree > 16):
            print('Oops, too many nodes in tree. Can\'t print the tree')
            return          

        max_print_list_size = 1 << (max_num_nodes_in_tree + 2)

        print_list = [None] * max_print_list_size

        #Store the nodes of the tree in print_list. print_list[0] will hold the root.
        #print_list[1] will hold root's left child. print_list[2] will hold root's right child
        #print_list[3] to print[6] will hold the nodes at depth 2 and so on. 
        #Even None nodes are stored in the list
        max_depth = -1
        max_depth = PrintTreeHelper.fill_print_list(root, 0, max_depth, print_list, 0)

        #Our print function is limited by the number of columns on the screen. We can print
        #properly on till a depth of 3
        if (max_depth > 3) :
            print('Oops can\'t print the tree at depth more than 4 ')
            return  
        

        # If MAX_NUM_COLS_ON_SCREEN is 40,
        #for depth 0, start_display_pos = 20, offset = 40: root is printed at column 20:
        #for depth 1, start_display_pos = 10, offset = 20: printing happens at column 10 and 30:
        #for depth 2, start_display_pos = 5,  offset = 10: printing happens at column 5, 15, 25 and 35:
        
        cur_depth = print_index = 0
        start_display_pos = MAX_NUM_COLS_ON_SCREEN // 2
        offset = MAX_NUM_COLS_ON_SCREEN

        while (cur_depth <= max_depth) :
            num_nodes_in_this_level = (1 << cur_depth)
            screen_pos = 0
            node_display_pos = start_display_pos

            for i in range (num_nodes_in_this_level) :

                cur_node = print_list[print_index]

                #We need to display current node at node_display_pos
                #So print spaces on the screen till screen_pos reaches node_display_pos
                while (screen_pos < node_display_pos) :
                    print(' ', end='')
                    screen_pos += 1
                

                if (cur_node) :
                    print(cur_node.data, end='')
                    screen_pos += 1
                

                node_display_pos += offset #Compute the position of the next node
                print_index += 1
            

            #We are going to nodes at next depth. So go to next line
            print('\n')

            cur_depth += 1
            start_display_pos = start_display_pos // 2
            offset = offset // 2
        

        print('\n')
    
    

