
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
    



#m: 2-D matrix that should be printed spirally
def print_spiral(m) :
    num_rows = len(m)
    num_cols = len(m[0])
    r1 = 0
    r2 = num_rows - 1
    c1 = 0
    c2 = num_cols - 1

    while (r1 <= r2 and c1 <= c2) :
        #Print row r1
        cur_row = r1
        for  cur_col in range(c1, c2+1):
            print('{} '.format(m[cur_row][cur_col]) , end='')
        
        r1 += 1 #Advance r1 to next row

        #Print column c2
        cur_col = c2
        for  cur_row in range(r1, r2+1):
            print('{} '.format(m[cur_row][cur_col]) , end='')
        
        c2 -= 1 #Advance c2 to previous column

        if (r1 != r2) :
            #Print row r2
            cur_row = r2
            for  cur_col in range(c2, c1-1,-1):
                print('{} '.format(m[cur_row][cur_col]) , end='')
            
            r2 -= 1 #Advance r2 to previous row

        if (c1 != c2) :
            #Print column c1
            cur_col = c1
            for  cur_row in range(r2, r1-1,-1):
                print('{} '.format(m[cur_row][cur_col]) , end='')
            
            c1 += 1 #Advance c1 to next column
        
    

if (__name__ == '__main__'):
    m =     [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25] ]
    
    print_spiral(m)

    print('')
    print('Test passed')




