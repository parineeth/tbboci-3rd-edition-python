
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random






MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_ELEMENT_VALUE = 100
MAX_NUM_ROWS = 5
MAX_NUM_COLS = 5


MIN_INT = (-1 * 0x7FFFFFFF)

def handle_error() :
    print('Error occured ')
    sys.exit(1)



#a: list of numbers for which MCS should be found. size of a >= 1
#Return value:  1. Maximum continuous sum of the elements , 
#       2. the starting list index of the MCS 
#       3. the ending list index of the MCS 
def kadane_mcs(a) :
    mcs_start_pos = mcs_end_pos = 0
    cur_start_pos = 0 #store the start position of the current window

    max_local = max_global = MIN_INT

    for  i, cur_value in enumerate(a):
        max_local = max(cur_value, cur_value + max_local)
        if (max_local == cur_value):
            cur_start_pos = i #start a new window here

        #Find the global maximum
        if (max_local > max_global) :
            max_global = max_local
            mcs_start_pos = cur_start_pos
            mcs_end_pos = i

    return max_global, mcs_start_pos, mcs_end_pos


#matrix: non-empty input matrix for which we have to find the maximum sum
#Return value: the sum of elements in the max sum sub-matrix in the input matrix
def find_max_sum_matrix(matrix) :
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    max_sum = MIN_INT
    for  left_col in range(n_cols):
        #We have chosen a left column. Initialize the temporary list to 0
        #the temporary list will store the result of column additions
        a = [0 for i in range(n_rows)]

        #Iterate through the right side columns which are >= left column
        for  right_col in range(left_col, n_cols):
        
            #Add the elements in the current right column to list a
            for  i in range(n_rows):
                a[i] += matrix[i][right_col]

            #Find the maximum continuous sum of the 1-D list using 
            #Kadane's algo. The start and end indices returned by Kadane's 
            #algo will correspond to the start row and end row of the 
            #2-D matrix
            cur_sum, start, end = kadane_mcs(a)

            if (cur_sum > max_sum) :
                max_sum = cur_sum
            
                #The maximum sum sub-matrix is bounded between 
                #col1 = left_col, col2 = right_col, row1 = start 
                #row2 = end
        
    return max_sum




def find_brute_force_mcs(matrix) :
    mcs = MIN_INT
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    #Fix the start_row, end_row, start_col and end_col of the sub-matrix
    for  start_row in range(n_rows):
        for  end_row in range(start_row, n_rows):
            for  start_col in range(n_cols):
                for  end_col in range(start_col, n_cols):

                    #Find the sum in the current sub-matrix
                    cur_sum = 0
                    for  i in range(start_row, end_row+1):
                        for  j in range(start_col, end_col+1):
                            cur_sum += matrix[i][j]
                        
                    

                    if (cur_sum > mcs):
                        mcs = cur_sum
                
            
        
    

    return mcs



def print_matrix(m) :
    for  inner_list in m:
        for  cur_val in inner_list:
            print('{} '.format(cur_val) , end='')
        
        print('')



def test() :

    #Pick a random number of rows
    n_rows = random.randint(1, MAX_NUM_ROWS)

    #Pick a random number of rows
    n_cols = random.randint(1, MAX_NUM_COLS)

    #Generate random values into the matrix 
    matrix = [[random.randint(0, MAX_ELEMENT_VALUE) for y in range(n_cols)] for x in range(n_rows)]

    for  i in range(n_rows):
        for  j in range(n_cols):
            #Some elements will be negative
            if (random.randint(0, 1) == 0):
                matrix[i][j] = -1 * matrix[i][j]
        
    

    print('Input : ')
    print_matrix(matrix)

    #Find the maximum continuous sum
    algo_mcs = find_max_sum_matrix(matrix)

    print('Max Continuous Sum =  {}'.format(algo_mcs) )

    #Find the maximum continuous sum using brute force
    brute_force_mcs = find_brute_force_mcs(matrix)

    #The two results should match
    if (algo_mcs != brute_force_mcs) :
        handle_error()
    

    print('______________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')



