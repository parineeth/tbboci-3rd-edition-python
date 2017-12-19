
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




WHITE = 0
GRAY = 1
BLACK = 2


def handle_error() :
    print(  'Test failed')
    sys.exit(1)


#Helper function that performs depth first search on the graph
#cur_node: the current node that we are searching
#adjacency_table: a list of lists. If there is an edge between node 0 and 
#    node 5, then adjacency_table[0] is a list which stores 5 in it.
#color: this list indicates color assigned to the node
#num_nodes: total number of nodes in the graph
#Return value: True if cycle is present in directed graph, False otherwise
def dfs(cur_node, adjacency_table, color, num_nodes) :
    does_cycle_exist = False
    neighbors = adjacency_table[cur_node]

    #Assign the gray color to the node indicating that we have started 
    #processing this node
    color[cur_node] = GRAY

    for  cur_neighbor in neighbors:
        #If we find a neighboring node with the gray color, then we 
        #have found a loop
        if (color[cur_neighbor] == GRAY) :
            return True
        
        #If the neighboring node has a white color, then perform 
        #DFS on it
        if (color[cur_neighbor] == WHITE) :
            does_cycle_exist = dfs(cur_neighbor, adjacency_table, 
                        color, num_nodes)
            if (does_cycle_exist):
                return True
    
    #Assign the node the black color to indicate that we have finished 
    #processing it
    color[cur_node] = BLACK
    return False    


#Main function that checks if cycle is present or not
#adjacency_table: a list of lists. If there is an edge between node 0 and 
#   node 5, then adjacency_table[0] is a list which stores 5 in it.
#num_nodes: total number of nodes in the graph
#Return value: True if cycle is present in directed graph, False otherwise
def is_cycle_present(adjacency_table, num_nodes) :
    does_cycle_exist = False

    #Assign the white color to all the nodes to indicate that we have not 
    #started processing the nodes
    color = [WHITE] * num_nodes
    
    #Go through all the nodes in the graph and perform DFS on the 
    #nodes whose color is white
    for  i, cur_color in enumerate(color):
        if (cur_color == WHITE) :
            does_cycle_exist = dfs(i, adjacency_table, 
                        color, num_nodes)
            if (does_cycle_exist) :
                break
            
    return does_cycle_exist



def test01() :
    #Construct a graph without a cycle
    #The edges in the graph are 0->1, 0->2, 0->3, 1->2, 1->3, 2->3, 4->1

    num_nodes = 5
    adjacency_table = [[1, 2, 3], [2, 3], [3], [], [1]]


    result = is_cycle_present(adjacency_table, num_nodes)

    if (result != False):
        handle_error()





def test02() :
    #Construct a graph with a cycle
    #The edges in the graph are 0->1, 0->2, 0->3, 1->2, 1->3, 2->3, 3->4 and 4->2
    #The cycle is 2->3, 3->4, 4->2
    
    num_nodes = 5

    adjacency_table = [[1, 2, 3], [2, 3], [3], [4], [2]]

    result = is_cycle_present(adjacency_table, num_nodes)

    if (result != True):
        handle_error()





if (__name__ == '__main__'):
    test01()

    test02()

    print(  'Test passed')



