
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 100
MAX_NUM_ELEMS = 10
MAX_VALUE     = 100
MAX_INT       = 1000000

def handle_error() :
    print('Test failed ')
    sys.exit(1)







#Helper function for finding the kth smallest element in a list
#This function, picks a pivot and arranges all numbers smaller than pivot to
#the left of the pivot and all numbers greater than pivot to the right of pivot
#a: list on which the partition operation should be performed
#left: index of the starting element of the partition in the list
#right: index of the ending element of the partition in the list
#Return value: index of the pivot element of the partition
def partition(a, left, right):
    num_elements = right - left + 1
    rand_pos = left + (random.randint(0, num_elements - 1))

    #pick a random element and swap it with the last element
    a[rand_pos], a[right] = a[right], a[rand_pos]

    #The last element is treated as the pivot
    pivot = a[right]

    i = left
    for  j in range(left, right - 1+1):
        if (a[j] <= pivot) :
            #If i is not equal to j, then a[i] has a value
            #greater than pivot and a[j] has a value less than
            #pivot. So swap a[i] and a[j]
            if (i != j) :
                a[i], a[j] = a[j], a[i]
            
            i += 1

    #Swap a[i] and the pivot that is at a[right]
    a[i], a[right] = a[right], a[i]

    return i #the pivot is now at i. So return i



#Finds the kth smallest element in a list
#a: list in which the kth smallest element should be found
#k: value of k (can range from 0 to number of elements in list - 1)
#Returns: the kth smallest element in the list
def find_kth_smallest(a, k) :
    left = 0
    right = len(a) - 1

    while (k >= left and k <= right) :
        pivot_pos = partition(a, left, right)
    
        if (pivot_pos == k):
            return a[pivot_pos]
        elif (pivot_pos < k):
            left = pivot_pos + 1
        else :
            right = pivot_pos - 1
        
    return MAX_INT #incorrect k value was specified






def test() :

    #Randomly decide the number of elements in the list
    length = random.randint(1, MAX_NUM_ELEMS)
    k = random.randint(0, length - 1)

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]

    print(a)

    #Find the result using an efficient technique
    result = find_kth_smallest(a, k)

    print('K = {}, Kth smallest is {}'.format(k, result) )

    #Find the expected result using sorting
    a.sort()
    expected_result = a[k]

    #The two results should match
    if (result != expected_result ) :
        handle_error()
    


    print('________________________________________________')



if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')



