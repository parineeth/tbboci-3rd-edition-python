
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




#m: 2-D matrix to be processed having at least 1 row and 1 column
def process_matrix(m) :
    is_1_in_first_row = 0
    is_1_in_first_col = 0

    num_rows = len(m)
    num_cols = len(m[0])

    #Check if any cell in the first row is set to 1
    for  i in range(num_rows):
        if (m[i][0] == 1) :
            is_1_in_first_row = True
            break
        
    #Check if any cell in first column is set to 1
    for  j in range(num_cols):
        if (m[0][j] == 1) :
            is_1_in_first_col = True
            break
        
    #Scan the matrix. If m[i][0] is equal to 1 then, set m[i][0] to 1
    #and set m[0][j] to 1
    for  i in range(1, num_rows):
        for  j in range(1, num_cols):
            if (m[i][j] == 1) :
                m[i][0] = 1
                m[0][j] = 1
            
    #Mark the cells as 1 as indicated by m[i][0] and m[0][j]
    for  i in range(1, num_rows):
        for  j in range(1, num_cols):
            if (m[i][0] == 1 or m[0][j] == 1):
                m[i][j] = 1

    #If there was a 1 initially in first column, set 1 in all the 
    #cells of first column
    if (is_1_in_first_col):
        for  i in range(num_rows):
            m[i][0] = 1

    #If there was a 1 initially in first row, set 1 in all the 
    #cells of the first row
    if (is_1_in_first_row):
        for  j in range(num_cols):
            m[0][j] = 1



def test_01() :
    m = [ [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0] ]
        

    expected_result = [ 
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0],
            [1, 0, 1, 1, 0] ]
        

    print('Input: ')
    print_matrix(m)

    process_matrix(m)

    print('Output: ')
    print_matrix(m)

    if (m == expected_result):
        pass
    else:
        handle_error()



if (__name__ == '__main__'):
    test_01()
    print('Test passed')




