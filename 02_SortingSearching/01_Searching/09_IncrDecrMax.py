
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random

MIN_INT = -999999

def handle_error() :
    print('Error occured')
    sys.exit(1)


#a: list where elements first increase and then decrease
#Return value: maximum element in the list
def find_max(a) :
    start = 0
    end = len(a) - 1
    max_element = MIN_INT

    while (start <= end) :
        #If only one element is left, then it is the max element
        if (start == end)   :
            max_element = a[start]
            break
        
        #If two elements are left, find the maximum of the two
        if (start + 1 == end) :
            max_element = a[start]
            if (a[start+1] > max_element):
                max_element = a[start+1]
            break
        
        #If there are more than two elements left, then inspect the 
        #middle element in between start and end
        mid = (start+end) // 2

        #If middle element is greater than previous element and also 
        #greater than the next element, then it is the maximum element
        if (a[mid - 1] < a[mid] and a[mid] > a[mid + 1]) :
            max_element = a[mid]
            break
        
        #We have not yet been able to find the max_element. So modify the 
        #range in which to search in the next iteration
        if (a[mid - 1] < a[mid] and a[mid] < a[mid + 1]) :
            start = mid + 1
        else :
            end = mid - 1
        
    return max_element




def test01() :
    a = [50, 40, 30, 20, 10]

    print(a)
    result = find_max(a)

    print('Maximum element = {}'.format(result) )

    if (result != 50):
        handle_error()

    print('_________________________________________')


def test02() :
    a = [30, 50, 40, 30, 20]

    print(a)
    result = find_max(a)

    print('Maximum element = {}'.format(result) )

    if (result != 50):
        handle_error()

    print('_________________________________________')


def test03() :
    a = [30, 40, 50, 20, 10]

    print(a)
    result = find_max(a)

    print('Maximum element = {}'.format(result) )

    if (result != 50):
        handle_error()

    print('_________________________________________')


def test04() :
    a = [10, 20, 30, 50, 10]

    print(a)
    result = find_max(a)

    print('Maximum element = {}'.format(result) )

    if (result != 50):
        handle_error()

    print('_________________________________________')



def test05() :
    a = [10, 20, 30, 40, 50]

    print(a)
    result = find_max(a)

    print('Maximum element = {}'.format(result) )

    if (result != 50):
        handle_error()

    print('_________________________________________')





if (__name__ == '__main__'):
    test01()
    test02()
    test03()
    test04()
    test05()

    print('Test passed')



