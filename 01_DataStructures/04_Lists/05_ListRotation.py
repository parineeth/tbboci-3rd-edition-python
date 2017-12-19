
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




#Helper function which reverses a list in region (low, high)
#a: list which needs to be reversed
#low: lower index of region to be reversed
#high: higher index of region to be reversed
def reverse_list(a, low, high) :
    while (low < high) :
        a[low], a[high] = a[high], a[low]
        low += 1
        high -= 1
    


#Main function to rotate a 1 dimensional list
#a: list which should be rotated. 
#num_rotations: how many times to rotate the list. Should be >= 0
def rotate_list(a, num_rotations) :
    length = len(a)
    if (length == 0):
        return

    #Suppose a list has a length of 5, every time we rotate by 
    #5 locations, we end up with the same list. So obtain num_rotations 
    #value from 0 to length - 1
    num_rotations = num_rotations % length

    if (num_rotations == 0):
        return

    #Reverse the entire list
    a.reverse()

    #Reverse the list in the region (0, num_rotations - 1)
    reverse_list(a, 0, num_rotations - 1)

    #Reverse the list in the region (num_rotations, length - 1)
    reverse_list(a, num_rotations, length - 1)



def handle_error() :
    print('Error occured ')
    sys.exit(1)




    


def perform_test(input_list, num_rotations, expected_result) :
    print('Num Rotations = {}'.format(num_rotations))

    print('Before Rotating: ', end='')
    print(input_list)

    rotate_list(input_list, num_rotations)
    if (input_list == expected_result):
        pass
    else:
        handle_error()

    print('After  Rotating: ', end='')
    print(input_list) 

    print('________________________________________')   



def test1() :
    input_list  = [10]
    expected_result  = [10]
    num_rotations = 1

    perform_test(input_list, num_rotations, expected_result)



def test2() :
    input_list  = [10, 20, 30, 40, 50]
    expected_result  = [50, 10, 20, 30, 40]
    num_rotations = 1

    perform_test(input_list, num_rotations, expected_result)



def test3() :
    input_list  = [10, 20, 30, 40, 50]
    expected_result  = [40, 50, 10, 20, 30]
    num_rotations = 2

    perform_test(input_list, num_rotations, expected_result)    



def test4() :
    input_list  = [10, 20, 30, 40, 50]
    expected_result  = [20, 30, 40, 50, 10]
    num_rotations = 4

    perform_test(input_list, num_rotations, expected_result)    


def test5() :
    input_list  = [10, 20, 30, 40, 50]
    expected_result  = [10, 20, 30, 40, 50]
    num_rotations = 5

    perform_test(input_list, num_rotations, expected_result)        



if (__name__ == '__main__'):
    test1()
    test2()
    test3()
    test4()
    test5()

    print('Test passed')



