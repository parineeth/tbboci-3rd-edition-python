
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




MAX_NUM_TESTS = 100

def handle_error() :
    print('Error occured ')
    sys.exit(1)


def print_matrix(m) :
    for  inner_list in m:
        for  cur_val in inner_list:
            print('{} '.format(cur_val) , end='')
        
        print('')



#Helper function that indicates if we can enter the cell or not
def can_enter_cell(matrix, is_visited, cur_row, cur_col) :
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    #If we are outside the bounds of the matrix or
    #if the cell is already visited or if the value in cell is 0
    #then we shouldn't enter the cell
    if (cur_row < 0 or cur_row >= n_rows 
        or cur_col < 0 or cur_col >= n_cols
        or is_visited[cur_row][cur_col] 
        or matrix[cur_row][cur_col] == 0) :
        return False
    

    return True



#Helper function to count the number of islands of 1's
#matrix: 2-D matrix consisting of 0's and 1's
#is_visited: if cell (i, j) has been visited, is_visited[i][j] is set to True
#cur_row: row of the current cell being processed
#cur_col: column of the current cell being processed
def expand_search(matrix, is_visited, cur_row, cur_col) :
    n_rows = len(matrix) 
    n_cols = len(matrix[0])

    is_visited[cur_row][cur_col] = True

    #For the current cell, find out if we can continue the island of 1's
    #with its neighbors. Each cell has 8 neighbors. The rows
    #of neighbors will vary from cur_row - 1 to cur_row + 1
    #The columns of the neighbors will vary from cur_col - 1
    #to cur_col + 1
    for  i in range(-1, 2):
        for  j in range(-1, 2):
            is_safe_cell = can_enter_cell(matrix, is_visited, cur_row+i, 
                                cur_col+j)

            if (is_safe_cell) :
                expand_search(matrix, is_visited, cur_row+i, cur_col+j)
            


#Main function to find the number of islands of 1's
#matrix: 2-D matrix consisting of 0's and 1's. Should not be empty
def find_islands(matrix) :
    n_rows = len(matrix) 
    n_cols = len(matrix[0])
    is_visited = [ [False for x in range(n_cols)] for x in range(n_rows)]

    #Search all the cells in matrix that are not yet visited
    count = 0
    for  i in range(n_rows):
        for  j in range(n_cols):
            if (matrix[i][j] == 1 and not is_visited[i][j]) :
                #We have found an island. Now expand the island 
                #in all directions
                expand_search(matrix, is_visited, i, j)
                count += 1
            
    return count



def test01() :
    matrix =  [
            [1, 1, 1, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0]
        ]

    expected_result = 4

    print_matrix(matrix)

    result = find_islands(matrix)

    print('Number of islands = {}'.format(result) )

    if (result != expected_result):
        handle_error()

    print('______________________________________')




def test02() :
    matrix =  [
            [1, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0]
        ]
            
    expected_result = 1

    print_matrix(matrix)

    result = find_islands(matrix)

    print('Number of islands = {}'.format(result) )

    if (result != expected_result):
        handle_error()

    print('______________________________________')




if (__name__ == '__main__'):
    test01()
    test02()

    print('Test passed')




