
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
MAX_INT       = 1000000
MIN_INT       = -100000

def handle_error() :
    print('Test failed')
    sys.exit(1)








#a:input list 
#Return value: the two smallest values will be returned 
def find_two_smallest(a) :
    length = len(a)

    min_value = [MAX_INT, MAX_INT]

    for  cur_val in a:
        if (cur_val < min_value[0]) :
            min_value[1] = min_value[0]
            min_value[0] = cur_val 
        elif (cur_val  < min_value[1]) :
            min_value[1] = cur_val 
        
    
    return min_value[0], min_value[1]




#a:input list 
#Return value: the two smallest values will be returned here 
def sorting_two_smallest(a) :

    a.sort()

    return a[0], a[1]








def test() :

    #Randomly decide the number of elements in the list
    length = random.randint(2, MAX_NUM_ELEMS)

    result = [0, 0]
    expected_result = [0, 0]

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]

    print(a)

    #Find the result using an efficient technique
    result[0], result[1] = find_two_smallest(a)

    print('Two Smallest are = {}, {}'.format(result[0], result[1]) )


    #Find the result using sorting
    expected_result[0], expected_result[1] = sorting_two_smallest(a)


    #The two results should match
    if ( (result[0] == expected_result[0] and result[1] == expected_result[1]) 
        or (result[1] == expected_result[0] and result[0] == expected_result[1]) ): 
        #The results match. Do nothing
        pass
    else :
        handle_error()
    


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()


    print('Test passed')



