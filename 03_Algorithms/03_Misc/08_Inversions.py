
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 100
MAX_NUM_ELEMS = 10
MAX_VALUE     = 10



def handle_error() :
    print('Error occured ')
    sys.exit(1)




#Helper function that merges two sorted regions
#a: list where a[left] to a[mid] is sorted and a[mid+1] to a[right] is sorted
#   We now need to merge these two regions
#temp: temporary list used for sorting
#Return value: Number of inversions  
def merge(a, temp, left, mid, right) :
    num_inversions = 0

    i = left
    j = mid + 1
    k = left #k is used for storing the merged values into temp
    while (i <= mid and j <= right) :
        if (a[i] <= a[j]) :
            temp[k] = a[i]
            k += 1
            i += 1
        else :
            temp[k] = a[j]
            k += 1
            j += 1
            num_inversions += mid + 1 - i
        
    #Handle any pending entries in first region
    while (i <= mid) :
        temp[k] = a[i]
        k += 1
        i += 1

    #Handle any pending entries in second region
    while (j <= right):
        temp[k] = a[j]
        k += 1
        j += 1

    #Restore the values from temp into a
    for  i in range(left, right+1):
        a[i] = temp[i] 

    return num_inversions


#Helper function that performs merge sort
#a: list that should be sorted
#temp: temporary list used for sorting
#left: first index of the region in the list to be sorted
#right: last index of the region in the list to be sorted
#Return value: Number of inversions  
def merge_sort(a, temp, left, right) :
    if (left >= right):
        return 0

    mid = (left + right) // 2
 
    num_inversions = merge_sort(a, temp, left, mid)

    num_inversions += merge_sort(a, temp, mid + 1, right)

    num_inversions += merge(a, temp, left, mid, right)

    return num_inversions



#a: list of numbers. should have at least one number
#Return value: number of inversions
def find_inversions(a) :
    num_elements = len(a)

    temp = [0] * num_elements

    num_inversions =  merge_sort(a, temp, 0, num_elements - 1)

    return num_inversions




def brute_force_inversions(a) :
    num_inversions = 0

    for  i in range(1, len(a)):
        for  j in range(i):
            if (a[j] > a[i]):
                num_inversions += 1
        
    

    return num_inversions 
 


def test() :

    #Randomly decide the number of elements in the list
    num_elems = random.randint(1, MAX_NUM_ELEMS)

    #Randomly fill in the list
    a = [random.randint(0, MAX_VALUE) for  i in range(num_elems) ]  
    print(a)

    #Find the result using the brute force technique
    expected_result = brute_force_inversions(a)

    #Find the result using an efficient technique
    result = find_inversions(a)

    print('Number of Inversions = {}'.format(result) )


    #The two results should match
    if (result != expected_result) :
        handle_error()
    


    print('________________________________________________')





if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()


    print('Test passed')






