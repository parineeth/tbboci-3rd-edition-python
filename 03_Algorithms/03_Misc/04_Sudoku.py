
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




NUM_ROWS = 9
NUM_COLS = 9

def handle_error() :
    print('Error occured ')
    sys.exit(1)



def verify_grid(grid) :
    num_rows = len(grid)
    num_cols = len(grid[0])

    #The sum of the numbers in a row should be 
    #1 + 2 + 3 + 4+ 5 + 6 + 7 + 8 + 9 = 45
    for  row_nr in range(num_rows):
        total_sum = 0
        for  col_nr in range(num_cols):
            total_sum += grid[row_nr][col_nr]

        if (total_sum != 45):
            handle_error()
    


    #The sum of the numbers in a column should be 
    #1 + 2 + 3 + 4+ 5 + 6 + 7 + 8 + 9 = 45
    for  col_nr in range(num_cols):
        total_sum = 0
        for  row_nr in range(num_rows):
            total_sum += grid[row_nr][col_nr]

        if (total_sum != 45):
            handle_error()
    

    #We should also check if the sum in every 3*3 box is 45



def print_grid(grid, verify) :
    for  inner_list in grid:
        for  cur_val in inner_list:
            print('{} '.format(cur_val) , end='')
        
        print('')
    
    print('\n\n')

    if (verify):
        verify_grid(grid)





#Helper function which checks if it is possible to place a number in a cell
#grid: the 2-D sudoku matrix
#row_nr: row number of the cell we are checking
#col_nr: column number of the cell we are checking
#num: the number which we want to place in the cell
#Returns: True if we can place num in the cell, False otherwise
def can_fill_cell(grid, row_nr, col_nr, num) :
    #Ensure that the number is not present in any row of requested column
    for  i in range(NUM_ROWS):
        if (grid[i][col_nr] == num):
            return False

    #Ensure that the number is not present in any column of requested row
    for  j in range(NUM_COLS):
        if (grid[row_nr][j] == num):
            return False

    #Ensure that the number is not present in the 3*3 box it belongs to
    region_start_row = (row_nr // 3) * 3
    region_start_col = (col_nr // 3) * 3

    for  i in range(region_start_row, region_start_row + 3):
        for  j in range(region_start_col, region_start_col + 3):
            if (grid[i][j] == num):
                return False

    return True


#Main function for solving the sudoku puzzle
#grid: the 2-D sudoku matrix
#row_nr: row number of the current cell being processed
#col_nr: column number of the current cell being processed
def solve_sudoku(grid, row_nr, col_nr) :
    if (row_nr >= NUM_ROWS) :
        #We have found a solution. print the grid and
        #terminate the recursion
        print_grid(grid, True)
        return
    
    #Pre-compute the row and column of the next cell
    next_row = row_nr
    next_col = col_nr + 1
    if (next_col >= NUM_COLS) :
        next_col = 0
        next_row = row_nr + 1
    
    if (grid[row_nr][col_nr] == -1) :
        #The puzzle writer has not assigned a number to this cell.
        #So try assigning numbers 1-9 to the cell
        for  num in range(1, 10):
            if (can_fill_cell(grid, row_nr, col_nr, num)) :
                grid[row_nr][col_nr] = num
                solve_sudoku(grid, next_row, next_col)
            
        #Once we are done trying all numbers from 1-9, assign the cell
        #back to -1 to indicate puzzle writer has not assigned a number 
        #to the cell
        grid[row_nr][col_nr] = -1

    else :
        #The puzzle writer has already assigned a value to the cell. 
        #So proceed to the next cell
        solve_sudoku(grid, next_row, next_col)
    


if (__name__ == '__main__'):
    #Initialize all cells with -1
    grid = [[-1 for x in range(NUM_COLS)] for x in range(NUM_ROWS)] 



    #Fill in the cells specified by the puzzle writer
    grid[0][0] = 5
    grid[0][1] = 3
    grid[0][4] = 7

    grid[1][0] = 6
    grid[1][3] = 1
    grid[1][4] = 9
    grid[1][5] = 5

    grid[2][1] = 9
    grid[2][2] = 8
    grid[2][7] = 6

    grid[3][0] = 8
    grid[3][4] = 6
    grid[3][8] = 3

    grid[4][0] = 4
    grid[4][3] = 8
    grid[4][5] = 3
    grid[4][8] = 1

    grid[5][0] = 7
    grid[5][4] = 2
    grid[5][8] = 6

    grid[6][1] = 6
    grid[6][6] = 2
    grid[6][7] = 8

    grid[7][3] = 4
    grid[7][4] = 1
    grid[7][5] = 9
    grid[7][8] = 5

    grid[8][4] = 8
    grid[8][7] = 7
    grid[8][8] = 9

    print('Input: ')
    print_grid(grid, False) #passing False so that we don't verify the grid

    print('Output: ')
    solve_sudoku(grid, 0, 0)

    print('Test passed')



