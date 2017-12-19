
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





def handle_error() :
    print('Test failed')
    sys.exit(1)


#Helper function that performs binary search on a list of unknown length
#a: list which should be searched
#x: element which we are trying to find
#low: start position of region in list for searching
#high: end position of region in list for searching 
def binary_search(a, x, low, high) :
    mid = 0
    while (low <= high) :
        try: 
            mid = (low + high) // 2

            #if mid is greater than actual list length, then 
            #an exception is raised
            value = a[mid]

            if (value == x):
                return mid
            elif (value > x):
                high = mid - 1
            else :
                low = mid + 1
        except IndexError as e: 
            #mid has crossed the boundary of the list. So reduce 
            #the search region to (low, mid - 1)
            high = mid - 1
        
    return -1



#Main function for performing search on list whose length is not known
#a: input list
#x: item to be searched
#Returns: if x is found, the index of x is returned, otherwise -1 is returned
def search(a, x) :
    #Perform exponential search to first find the upper bound. Start with
    #high = 0 and then increase high to 1, 2, 4, 8, 16 and so on
    low = high = 0
    while (True) :
        try: 
            value = a[high]

            if (value == x) :
                return high #We found the element x
            elif (value > x):
                break   #Found range (low, high) where element exists
                    
            low = high + 1

            if (high == 0):
                high = 1
            else:
                high = high * 2
        
        except IndexError as e:  
            #We have crossed the boundary of the list. So we have found
            #the upper bound for high. 
            break
        
    #Perform binary search in range(low, high). Note that high may still be 
    #outside the list bounds
    return binary_search(a, x, low, high)



def test(length, x, expected_result) :

    a = [i for  i in range(length)]

    result = search(a, x)

    if (length > 0):
        print('Location of {} in list [0 to {}] is {}'.format(x, length - 1, result) )
    else:
        print('Location of {} in empty list is {}'.format(x, result) )

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    test(20, 0, 0)
    test(20, 15, 15) 
    test(20, 19, 19)

    test(20, 100, -1)
    test(20, -1, -1)

    test(0, 0, -1)

    print('Test passed')



