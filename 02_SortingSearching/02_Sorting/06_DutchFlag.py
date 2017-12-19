
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_ELEMENTS = 10
MAX_VALUE = 10
MAX_NUM_TESTS = 10

def handle_error() :
    print('Error occured ')
    sys.exit(1)



#a: input list that has to be sorted. 
#pivot_value: after sorting, all elements smaller than pivot will lie to the 
#left of the pivot and all values that are greater than pivot will lie to the 
#right of the pivot. If there are many pivot values, then they will occur  
#together in the middle 
def dutch_sort(a, pivot_value) :
    cur_pos = 0
    left_pos = 0
    right_pos = len(a) - 1
    while (cur_pos <= right_pos) :
        if (a[cur_pos] < pivot_value) :
            #swap a[left_pos], a[cur_pos]
            a[left_pos], a[cur_pos] =  a[cur_pos], a[left_pos]
        
            left_pos += 1
            cur_pos += 1

        elif (a[cur_pos] > pivot_value) :
            #swap a[cur_pos], a[right_pos]
            a[cur_pos], a[right_pos] = a[right_pos], a[cur_pos]

            #Advance the right fill location. Since we have newly 
            #brought in an element from right_pos to cur_pos, we 
            #have to process the new element. So don't advance cur_pos
            right_pos -= 1 

        else :
            cur_pos += 1
        
    





def test(a, pivot_value) :
    print('Pivot value = {}'.format(pivot_value) )

    print('Before : ', end='')
    print(a)

    #Perform the sort
    dutch_sort(a, pivot_value)

    #Verify the result of dutch sort 
    i = 0
    length = len(a)
    #All elements less than pivot should occur first
    while (i < length and a[i] < pivot_value ):
        i += 1

    #If there are one or more pivot values, they should come next
    while (i < length and a[i] == pivot_value):
        i += 1

    #All elements greater than the pivot value should occur at the end
    while ( i < length and a[i] > pivot_value):
        i += 1

    if (i != length):
        handle_error()

    print('After  : ', end='')
    print(a) 

    print('_______________________________________________')
 





if (__name__ == '__main__'):
    a = [0] * MAX_NUM_ELEMENTS


    #Run several number of tests
    for  loop in range(MAX_NUM_TESTS):
        #Pick the number of elements in the list randomly
        length = random.randint(1, MAX_NUM_ELEMENTS)

        #Randomly generate the elements in the list
        a = [random.randint(1, MAX_VALUE) for  i in range(length)]
    

        #Pick a random pivot
        i = random.randint(0, length - 1)
        pivot_value = a[i]

        test(a, pivot_value)


    print('Test passed')



