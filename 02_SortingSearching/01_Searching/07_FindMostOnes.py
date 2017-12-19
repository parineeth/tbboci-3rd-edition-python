
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




def handle_error() :
    print('Test failed')
    sys.exit(1)



def find_first(a, x) :
    start = 0
    end = len(a) - 1

    while (start <= end) :
        mid = (start + end) // 2

        if (a[mid] == x) :
            if (mid == 0 or a[mid - 1] != x):
                return mid
            else:
                end = mid - 1

        elif (a[mid] > x) :
            end = mid - 1
        else :
            start = mid + 1
        
    return -1



#a: list where each row is sorted and has only 0's and 1's
#Return value: row number that has most ones, if no row has 1's then return -1
def find_row_with_most_ones(a) :
    ncols = len(a[0])

    max_row = -1
    max_num_ones = 0

    for  i, inner_list in enumerate(a):
        #Find the position of the first 1 in the row
        first_one_index = find_first(inner_list, 1)

        #Compute number of 1's in row based on position of the first 1
        if (first_one_index == -1):
            cur_num_ones = 0 #there are no 1's in the row
        else:
            cur_num_ones = ncols - first_one_index

        if (cur_num_ones > max_num_ones) :
            max_num_ones = cur_num_ones
            max_row = i
        
    return max_row



def print_matrix(m) :
    for  inner_list in m:
        for  cur_val in inner_list:
            print('{} '.format(cur_val) , end='')
        
        print('')
    

def test01() :
    a = [[1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1] ]
     
    print_matrix(a)

    result = find_row_with_most_ones(a)
    print('\nRow with most ones = {}'.format(result) )

    if (result != 0):
        handle_error()

    print('___________________________________________________')


def test02() :
    a = [[0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 1, 1] ]
     
    print_matrix(a)

    result = find_row_with_most_ones(a)
    print('\nRow with most ones = {}'.format(result) )

    if (result != 3):
        handle_error()

    print('___________________________________________________')



if (__name__ == '__main__'):
    test01()
    test02()
    print('Test passed')



