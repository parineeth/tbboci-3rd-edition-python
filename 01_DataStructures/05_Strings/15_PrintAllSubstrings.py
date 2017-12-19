
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys


#str1: string whose substrings should be printed
def print_all_sub_strings(str1) :
    #Generate all pairs (i,j) where i <= j
    for  i in range(len(str1)):
        for  j in range(i, len(str1)):
        
            #print the substring str1[i] to str1[j]
            print(str1[i:j+1])
        

if (__name__ == '__main__'):
    print_all_sub_strings('ABCDE')
    print('Test passed')

    


