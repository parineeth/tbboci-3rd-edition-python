
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE     = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)



#a: non-empty input list from which duplicates should be removed. 
#   this list will be modified in-place
def remove_duplicates(a) :
    #Sort the list
    a.sort()

    fill_pos = 1
    for  i in range(1, len(a)):
        if (a[i] != a[i - 1]) :
            a[fill_pos] = a[i]
            fill_pos += 1

    #remove the remaining items in the list from fill_pos onwards
    if (fill_pos < len(a)):     
        del a[fill_pos:]







def verify(a) :
    for  i in range(len(a)):
        for  j in range(i+1, len(a)):
            if (a[i] == a[j]) :
                #We found a duplicate
                handle_error()
            
        
    




def test() :

    #Randomly decide the number of elements
    length1 = random.randint(1, MAX_NUM_ELEMS)

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for  i in range(length1)]

    print ('Original list : ', end='')
    print(a)


    #Remove the duplicates 
    remove_duplicates(a)

    print ('After removing duplicates : ', end='')
    print(a)

    verify(a)


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')



