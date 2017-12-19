
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random






MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_ELEMENT_VALUE = 100

MIN_INT = (-1 * 0x7FFFFFFF)

def handle_error() :
    print('Error occured ')
    sys.exit(1)





#a: list of numbers for which MCS should be found. size of a >= 1
#Return value:  1. Maximum continuous sum of the elements , 
#       2. the starting list index of the MCS 
#       3. the ending list index of the MCS 
def kadane_mcs(a) :
    mcs_start_pos = mcs_end_pos = 0
    cur_start_pos = 0 #store the start position of the current window

    max_local = max_global = MIN_INT

    for  i, cur_value in enumerate(a):
        max_local = max(cur_value, cur_value + max_local)
        if (max_local == cur_value):
            cur_start_pos = i #start a new window here

        #Find the global maximum
        if (max_local > max_global) :
            max_global = max_local
            mcs_start_pos = cur_start_pos
            mcs_end_pos = i

    return max_global, mcs_start_pos, mcs_end_pos



def find_brute_force_mcs(a) :
    mcs = MIN_INT

    for  start_elem in range(len(a)):
            cur_sum = 0
            for  i in range(start_elem, len(a)):
                cur_sum += a[i]
            
                if (mcs < cur_sum) :
                    mcs = cur_sum
            
    return mcs






def test() :
    
    #Pick a random number of elements
    num_elems = random.randint(1, MAX_NUM_ELEMS)

    #Generate random values into the list. 
    a = [random.randint(0, MAX_ELEMENT_VALUE) for  i in range(num_elems)]

    for  i in range(num_elems):
        #Some elements will be negative
        if (random.randint(0, 1) == 0):
            a[i] = -1 * a[i]
    

    print('Input : ', end='')
    print(a)


    #Find the maximum continuous sum
    algo_mcs, mcs_start_pos, mcs_end_pos = kadane_mcs(a)

    print('Max Continuous Sum = {}, MCS start position = {}, MCS end position = {} '.format(algo_mcs, 
            mcs_start_pos, mcs_end_pos) )

    #Find the maximum continuous sum using brute force
    brute_force_mcs = find_brute_force_mcs(a)

    #The two results should match
    if (algo_mcs != brute_force_mcs) :
        handle_error()
    

    print('______________________________________________')



if (__name__ == '__main__'):
    for  test_nr in range(MAX_NUM_TESTS):
        test()

    print('Test passed')




