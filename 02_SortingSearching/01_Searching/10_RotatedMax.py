
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_ELEMENTS = 10
MAX_NUM_TESTS = 10


def handle_error() :
    print('Error occured')
    sys.exit(1)




#a: non-empty list that has been sorted and rotated. 
#   There should NOT be any duplicates in the list
#Return value: maximum element in the list
def find_max(a) :
    start = 0
    end = len(a) - 1

    while (a[start] > a[end]) :
        mid = (start + end) // 2

        if (mid < len(a) - 1 and a[mid] > a[mid + 1]):
            return a[mid]

        if (a[mid] > a[end]) :
            start = mid #max is in the region (mid, end)
        else :
            end = mid - 1 #max is in the region (start, mid - 1)

    return a[end]



def generate_sorted_rotated_list(a) :
    n = len(a)

    #Generate the first random value
    a[0] = random.randint(0, 9)
    if (n == 1):
        return

    #Generate the remaining random values in increasing sorted order without duplication
    for  i in range(1, n):
         a[i] = a[i - 1] + random.randint(1, 10)
    

    #Randomly decide the number of rotations
    num_rotations = random.randint(0, n - 1)

    #Perform the rotations
    for  rotation_iter in range(num_rotations):
        temp = a[n-1]
        for  i in range(n - 1, 0,-1):
            a[i] = a[i - 1]
        
        a[0] = temp
    




def test01() :

    #randomly decide the number of elements
    n = random.randint(1, MAX_NUM_ELEMENTS)
    a = [0] * n

    #Generate the sorted rotated list
    generate_sorted_rotated_list(a)

    print('Input : ', end='')
    print(a)

    #Find the max using linear search
    expected_result = max(a)
        
    #Find the max using binary search
    actual_result = find_max(a)

    print('The maximum element is {}'.format(actual_result) )

    #Compare the results of linear and binary search
    if (expected_result != actual_result):
        handle_error()

    print('_______________________________________________')



def test2():
    a = [2, 2, 3, 3, 1, 1, 2, 2, 2]
    result = find_max(a)
    print('Max of {} is {}'.format(a, result))
    print('So this technique fails with duplicates')



if (__name__ == '__main__'):
    for  test_nr in range(MAX_NUM_TESTS):
        test01()

    print('Test passed ')





