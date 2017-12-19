
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random


    




MAX_NUM_TESTS = 10 
MAX_NUM_ELEMS = 10 
MAX_VALUE     = 1 
MIN_INT       = -100

def handle_error() :
    print('Test failed')
    sys.exit(1)




#a:input list 
#Returns: 1. the length of the longest sub-list with equal 0's and 1's
#       2. start index of longest sub-list
#       3. end index of longest sub-list 
def find_sub_list(a) :
    num_elements = len(a)

    #first_ix_for_sum will store the first seen index for a particular 
    #normalized running sum. Initialize the sum table. MIN_INT should be < -1
    #normalized running sum = num_elements + running_sum
    first_ix_for_sum = [MIN_INT] * (2 * num_elements + 1)

    #Before we start processing, we say that at index -1, running sum is 0
    #The normalized running sum =  num_elements + running_sum = num_elements
    #+ 0 = num_elements. So first_ix_for_sum[num_elements] is set to -1
    first_ix_for_sum[num_elements] = -1
    max_length = 0
    running_sum = 0
    start_index = end_index = -1
    for  i, cur_element in enumerate(a):
        #If we get a 1, increment the running sum. If we get a 0
        #then decrement the running sum
        if (cur_element == 1):
            running_sum += 1
        else:
            running_sum -= 1

        #If there are 10 elements, then running sum can vary from -10
        #to +10. Normalize the running sum into an index from 0 to 20
        normalized_sum = num_elements + running_sum
        if (first_ix_for_sum[normalized_sum] == MIN_INT) :
            #We are observing the normalized running sum
            #for the first time. Store the index in first_ix_for_sum
            first_ix_for_sum[normalized_sum] = i
        else :
            #We have already observed the normalized running sum
            #before. Suppose we have a normalized running sum of 3
            #at index 10 and we again observe normalized running sum
            #of 3 at index 18, then there are equal 0's and 1's 
            #from index 11 to index 18
            first_index = first_ix_for_sum[normalized_sum]
            if (i - first_index > max_length) :
                max_length = i - first_index
                start_index = first_index + 1
                end_index = i 
            
    return max_length, start_index, end_index



#a:input list 
#Returns: length of longest sub-list with equal 0's and 1's   
def brute_force_sub_list(a) :
    max_length = 0
    num_elements = len(a)

    for  i in range(num_elements - 1):
        #If we get a 1 we add 1 to running sum, if we get a 0, 
        #we subtract -1
        running_sum = (2 * a[i]) - 1

        for  j in range(i+1, num_elements):
            running_sum += (2 * a[j]) - 1
            if (running_sum == 0) :
                length = j - i + 1
                if (length > max_length) :
                    max_length = length
            
    return max_length




def test() :
    
    #Randomly decide the number of elements in the list
    length = random.randint(2, MAX_NUM_ELEMS)

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for x in range(length)] 

    print(a)

    #Find the length of longest sub-list with equal 0's and 1's 
    #using the efficient technique
    result, start_index, end_index = find_sub_list(a)

    print('Length of longest sub list with equal 0s and 1s  = {} '.format(result)) 
    print('\t(start index = {} , end index = {} )'.format(start_index, end_index))

    #Find the length of longest sub-list with equal 0's and 1's 
    #using brute force
    brute_force_result = brute_force_sub_list(a)

    #The two results should match
    if (result != brute_force_result):
        handle_error()


    print('________________________________________________')



if (__name__ == '__main__') :
    for i in range (MAX_NUM_TESTS):
        test()

    print('Test passed')





