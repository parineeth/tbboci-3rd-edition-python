
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys







#Helper function which checks if it is possible to place queen in cur_row 
#at position col_for_row[cur_row]
#cur_row: Row in which the current queen should be placed
#col_for_row: col_for_row[i] gives the column in which queen is placed in the 
# ith row
#Return value: True if queen can be placed at col_for_row[cur_row], False 
# otherwise
def check_placement(cur_row, col_for_row) :
    #Check if the queens placed in the rows before the current row conflict 
    #with the queen placed in current row
    for  i in range(cur_row):
        #Check if two queens are present in the same column
        if (col_for_row[i] == col_for_row[cur_row]):
            return False

        #Check if two queens are in the same diagonal
        col_diff = abs(col_for_row[cur_row] - col_for_row[i])
        row_diff = cur_row - i
        if (row_diff == col_diff):
            return False        
         
    return True


#Main function for arranging the queens
#cur_row: current row in which the queen should be placed
#N: the number of cells in one row of the chess board
#col_for_row: col_for_row[i] is used for storing the column of the ith row queen 
def arrange_queens(cur_row, N, col_for_row) :
    if (cur_row == N) :
        #We have found a successful arrangement. So print it
        for  i in range(N):
            print('Row = {}, Col =  {}'.format(i, col_for_row[i]) )
        
        print('__________________________')

        return #Terminate the recursion
    
    #Try out different columns in the current row
    for  i in range(N):
        col_for_row[cur_row] = i
        if (check_placement(cur_row, col_for_row)) :
            #The placements of queens looks good so far. Go to the next row
            arrange_queens(cur_row + 1, N, col_for_row)
        
     




if (__name__ == '__main__'):
    N = 4 #Number of cells in one row of the chess board
    col_for_row = [0] * N


    print('N = {}'.format(N) )

    arrange_queens(0, N, col_for_row)

    print('Test passed')



