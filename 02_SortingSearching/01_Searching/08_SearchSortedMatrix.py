
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



def handle_error() :
    print('Error occured')
    sys.exit(1)



#m: matrix to be searched
#x: element to search
#Return value:  True if element is present, False otherwise
def search_matrix(m, x):
    num_rows = len(m)
    num_cols = len(m[0])

    i = 0
    j = num_cols - 1
    is_found = False
    while (i < num_rows and j >= 0) :
        if (m[i][j] == x) :
            is_found = True
            break
        elif (m[i][j] < x):
            i += 1 #go to the row below
        else :
            j -= 1 #go to the previous column
        
    return is_found
 

def print_matrix(m) :
    for  inner_list in m:
        for  val in inner_list:
            print('{} '.format(val) , end='')
        
        print('')
    


def print_result(result, x) :
    if (result):
        print('Found {}'.format(x) )
    else :
        print('Could NOT Find {}'.format(x) )


def test(m, x, expected_result) :

    result = search_matrix(m, x)

    print_result(result, x)

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    m =  [[10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50] ]
          

    print_matrix(m)

    test(m, 40, True)
    test(m, 10, True)
    test(m, 50, True)
    test(m, 25, True)
    test(m, 37, True)
    test(m, 28, False)

    print('Test passed')






