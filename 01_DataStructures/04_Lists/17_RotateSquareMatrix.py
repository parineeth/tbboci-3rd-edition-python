
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
    



#m: 2-D square matrix to be rotated by 90 degrees in clockwise direction
def rotate_square_matrix90(m) :
    n = len(m) #Get the number of rows in the square matrix

    #max_i and max_j have the boundaries of the first quadrant
    max_i = (n // 2) - 1
    max_j = ((n+1) // 2) - 1

    for  i in range(max_i + 1):
        for  j in range(max_j + 1):

            #Perform  a four way swap
            temp = m[i][j]

            m[i][j] = m[n - j - 1][i]

            m[n - j - 1][i] = m[n - i - 1][n - j - 1]

            m[n - i - 1][n - j - 1] = m[j][n - i - 1]

            m[j][n - i - 1] = temp
        


    
if (__name__ == '__main__'):
    m =     [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25] ]
    rotate_square_matrix90(m)
    print_matrix(m)
    print('Test passed')




