
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys






def handle_error() :
    print(  'Test failed')
    sys.exit(1)


#Helper function that performs depth first search on the graph
#cur_node: the current node that we are searching
#adjacency_table: a list of lists. If there is an edge between node 0 
#   and node 5, then adjacency_table[0] is a list which will store 5 in it.
#is_visited: this list indicates if a node has already been visited or not
#num_nodes: total number of nodes in the graph
def dfs(cur_node, adjacency_table, is_visited, num_nodes): 
    neighbors = adjacency_table[cur_node]

    is_visited[cur_node] = True

    #Go through all the neighbors of the current node
    for  cur_neighbor in neighbors:
        #If the current neighbor has not been visited, then recursively 
        #call dfs on it
        if (not is_visited[cur_neighbor]):
            dfs(cur_neighbor, adjacency_table, is_visited, num_nodes)
    



#Main function to find the number of connected components in an undirected graph
#adjacency_table: a list of lists. If there is an edge between node 0 and 
#   node 5, then adjacency_table[0] is a list which will store 5 in it. 
#num_nodes: total number of nodes in the graph
#Return value: number of connected components in the graph
def connected_components(adjacency_table, num_nodes) :
    is_visited = [False] * num_nodes

    #Traverse through all the nodes in the graph and perform Depth First 
    #Search. Each time we perform DFS on a node that has not been visited 
    #so far, increment the number of connected components
    count = 0
    for  i, visited in enumerate(is_visited):
        if (not visited) :
            dfs(i, adjacency_table, is_visited, num_nodes)
            count += 1
        
    return count



def test01() :
    num_nodes = 4


    #Create an undirected graph where there is only one connected component
    #The edges in the graph are 0-1, 0-2, 0-3, 1-2, 1-3 and 2-3
    adjacency_table = [ [1, 2, 3], [2, 3], [3], []]

    result = connected_components(adjacency_table, num_nodes)

    if (result != 1):
        handle_error()






def test02() :
    num_nodes = 8


    #Create an undirected graph where there are 3 connected component
    #The edges in the graph are 0-1, 0-2, 0-3, 
    #4-5, 5-6 
    #7-7
    
    adjacency_table = [ [1, 2, 3], [], [], [], [5], [6], [], [7]]

    result = connected_components(adjacency_table, num_nodes)

    if (result != 3):
        handle_error()




def test03() :
    num_nodes = 8

    adjacency_table = [[] for x in range(num_nodes)]
    
    result = connected_components(adjacency_table, num_nodes)

    if (result != 8):
        handle_error()





if (__name__ == '__main__'):
    test01()

    test02()

    test03()

    print(  'Test passed')




