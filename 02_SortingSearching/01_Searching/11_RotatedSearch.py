
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_ELEMENTS = 10
MAX_NUM_TESTS = 100
MAX_VALUE = 9

def handle_error() :
    print('Error occured')
    sys.exit(1)





#a: non-empty list that has been sorted and rotated
# There should NOT be any duplicates in the list
#x: element to be searched in the list
#Return value: location of the element in list if found, -1 if not found
def find_element(a, x) :
    start = 0
    end = len(a) - 1

    while (start <= end) :
        mid = (start+end) // 2

        if (x == a[mid]) :
            return mid
        
        #Check which portion of the list has elements in sorted order
        if (a[start] <= a[mid]) :
            #The lower portion (start, mid) is still sorted even after
            #rotations. So use this portion for taking decisions
            if (a[start] <= x and x < a[mid]) :
                end = mid - 1   #search in region (start, mid-1)
            else:
                start = mid + 1 #search in region (mid+1, end)
        else :
            #The upper portion (mid, end) is sorted even after
            #rotations. So use this portion for taking decisions
            if (a[mid] < x and x <= a[end]) :
                start = mid + 1 #search in region (mid+1, end)
            else:
                end = mid - 1 #search in region (start, mid-1)

    return -1
 





def generate_unique_sorted_rotated_list(a, n) :
    #Generate the first random value
    a[0] = random.randint(0, 9)
    if (n == 1):
        return

    #Generate the remaining random values in increasing sorted order without duplication
    for  i in range(1, n):
        a[i] = a[i - 1] + 1 + random.randint(0, 9)

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
    generate_unique_sorted_rotated_list(a, n)

    print('Input : ', end='')
    print(a)

    for  index, x in enumerate(a):
        #Search the element using binary search
        actual_result = find_element(a, x)

        print('Location of {} is {}'.format(x, actual_result) )

        #Verify the result
        if (actual_result != index):
            handle_error()
    

    print('_________________________________________')



#Testing when the list contains duplicates
MAX_VALUE = 3
def test02() :

    #randomly decide the number of elements
    n = random.randint(1, MAX_NUM_ELEMENTS)

    a = [random.randint(1, MAX_VALUE) for x in range(n) ]

    a.sort() 

    #Randomly decide the number of rotations
    num_rotations = random.randint(0, n - 1)

    #Perform the rotations
    for  rotation_iter in range(num_rotations):
        temp = a[n-1]
        for  i in range(n - 1, 0,-1):
            a[i] = a[i - 1]
        
        a[0] = temp
    
    

    print('Input : ', end='')
    print(a)

    for  index, x in enumerate(a):
        #Search the element using binary search
        actual_result = find_element(a, x)

        print('Location of {} is {}'.format(x, actual_result) )

        #Verify the result
        if (a[actual_result] != x):
            handle_error()
    

    print('_________________________________________')




if (__name__ == '__main__'):
    for  test_nr in range(MAX_NUM_TESTS):
        test01()

    print('Test passed ')





