
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



#a: input list 
#Returns: the minimum value and maximum value in list are returned
def find_min_max(a) :
    max_value = MIN_INT
    min_value = MAX_INT

    i = 0
    if (len(a) % 2 == 1) :
        #If there are odd number of elements, then initialize 
        #max_value and min_value with a[0]
        max_value = min_value = a[0]
        i = 1
    
    while ( i < len(a) ) :
        if (a[i] > a[i+1]) :
            if (a[i] > max_value) :
                max_value = a[i]
            if (a[i+1] < min_value):
                min_value = a[i+1]
        else :
            if (a[i] < min_value):
                min_value = a[i]
            if (a[i+1] > max_value):
                max_value = a[i+1]
        
        i += 2

    return min_value, max_value






def test() :

    #Randomly decide the number of elements in the list
    length = random.randint(1, MAX_NUM_ELEMS)

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]

    print(a)

    #Find the result using an efficient technique
    result_min, result_max = find_min_max(a)


    print('Min = {}, Max = {}'.format(result_min, result_max) )


    #Find the result using sorting
    a.sort()
    expected_min = a[0]
    expected_max = a[length-1]


    #The two results should match
    if (result_min != expected_min or result_max != expected_max ) :
        handle_error()
    


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')



