
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





#str1: valid input string whose permutations have to be formed
#buf: list for storing the current permutation
#pos: current position in the buf list 
#visited: indicates if character in input string has already been visited
def generate_permutations(str1, buf, pos, visited): 
    #Recursion termination condition
    if (pos == len(str1)) :
        print(buf)
        return 
    
    for  i in range(len(str1)):
        if (visited[i] == False) :
            buf[pos] = str1[i]
            visited[i] = True
            generate_permutations(str1, buf, pos+1, visited)
            visited[i] = False
        
    



def test(str1) :
    buf = ['a'] * len(str1)
    visited = [False] * len(str1)

    print('Input: ', end='')
    print(str1)

    generate_permutations(str1, buf, 0, visited)

    print('______________________________')



if (__name__ == '__main__'):
    test('')
    test('A')
    test('ABCDE')

    print('Test passed')





