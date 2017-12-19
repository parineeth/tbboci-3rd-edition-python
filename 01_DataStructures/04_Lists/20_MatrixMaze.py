
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





def handle_error() :
    print('Test failed')
    sys.exit(1)


def print_matrix(m) :
    for  inner_list in m:
        for  cur_val in inner_list:
            print('{} '.format(cur_val) , end='')
        
        print('')




#m: matrix that has to be navigated
#cur_row: row of the current cell
#cur_col: column of the current cell
#Return value: the total number of paths possible is returned
def navigate_maze(m, cur_row, cur_col) :
    if (cur_row < 0 or cur_col < 0):
        return 0

    if (m[cur_row][cur_col] == -1):
        return 0 #We can't traverse this cell, so simply return

    if (cur_row == 0 and cur_col == 0) :
        #We have reached the destination
        return 1
    
    #Try continuing the path by going to the cell in previous row
    num_paths = navigate_maze(m, cur_row - 1, cur_col)

    #Try continuing the path by going to the cell in previous column
    num_paths += navigate_maze(m, cur_row, cur_col - 1)

    #Try continuing the path by going to the diagonally above cell
    num_paths += navigate_maze(m, cur_row - 1, cur_col - 1)

    return num_paths




def test_01() :

    m =  [ [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0] ]
    
    print('Input: ')
    print_matrix(m)

    num_paths = navigate_maze(m, len(m) - 1, len(m[0]) - 1)

    print('Number of paths = {}'.format(num_paths) )

    if (num_paths != 321):
        handle_error()



if (__name__ == '__main__'):
    test_01()
    print('Test passed')




