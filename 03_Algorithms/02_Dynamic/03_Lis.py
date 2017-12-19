
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




#a: list in which we need to find the longest increasing sequence
#   should have at least 1 element
#Return value: list having the longest increasing sequence is returned
def find_lis(a) :
    n = len(a)

    #seq_length stores length of LIS for each position of list a
    #Each element by itself forms a sequence of length 1
    seq_length = [1 for i in range(n)]

    #prev_ix stores the index of previous element in the LIS sequence
    prev_ix = [0] * n

    #Find the LIS for each position in list a
    for  i in range(1, n):
        for  j in range(i):
            if ( a[j] < a[i] and seq_length[i] < seq_length[j] + 1 ) :
                seq_length[i] = seq_length[j] + 1
                prev_ix[i] = j
            
    #The longest LIS amongst all positions of list a will be the LIS 
    #for the whole list 
    lis_length = 1
    lis_end = 0
    for  i in range(1, n):
        if (lis_length < seq_length[i]) :
            lis_length = seq_length[i]
            lis_end = i
        
    lis = [0] * lis_length

    #Use the prev_ix list to reconstruct the LIS for the whole list
    #lis_end has the index of the last element in the LIS for whole list
    j = lis_end
    for  i in range(lis_length - 1, -1,-1):
        lis[i] = a[j]
        j = prev_ix[j]
    
    return lis






def test01() :
    a = [6, 3, 2, 4, 5]

    print('Input : ', end='')
    print(a)

    lis = find_lis(a)

    print('LIS : ', end='')
    print(lis)

    print('___________________________________________')



def test02() :
    a = [2, 4, 3,  1, 7 , 7, 9] 

    print('Input : ', end='')
    print(a)

    lis = find_lis(a)

    print('LIS : ', end='')
    print(lis)

    print('___________________________________________')




if (__name__ == '__main__'):
    test01()
    test02()

    print('Test passed')




