
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



def handle_error() :
    print('Test failed')
    sys.exit(1)



#strings: sorted list of strings in which some of the strings can be empty ('')
#x: string to be searched
#Returns: index of x in the list strings if found, -1 otherwise
def search(strings, x) :
    low = 0
    high = len(strings) - 1

    while (low <= high) :
        #If we hit an empty string at position high, then keep decreasing
        #high till we get a non-empty string
        while (low <= high and strings[high] == '') :
            high -= 1
        
        #If we have only empty strings between low and high, then return
        #not found
        if (low > high):
            return -1

        mid = (low + high) // 2

        #If we get an empty element at mid, then keep incrementing mid.
        #We are guaranteed to find a non-empty string since strings[high]
        #is non-empty
        while (strings[mid] == ''):
            mid += 1

        #Compare the mid element with the element being searched
        if (strings[mid] == x) :
            return mid
        elif (strings[mid] < x) :
            low = mid + 1
        else :
            high = mid - 1
        
    return -1





def test(strings,  x, expected_result) :
    result = search(strings, x)

    print('Input: [', end='')
    for  cur_string in strings:
        print('\'' + cur_string + '\'' + ', ' , end='')
    
    print(']')

    print('Searching {}, Postion = {}'.format(x, result) )

    if (result != expected_result) :
        handle_error()
    
    print('______________________________________________')
 



if (__name__ == '__main__'):
    strings = ['', 'apple', '', '', 'ball', 'cat', '', 'dog', '', '', '', 'egg', '']

    test(strings, 'apple', 1) 
    test(strings, 'ball', 4)
    test(strings, 'cat', 5)
    test(strings, 'dog', 7)
    test(strings, 'egg', 11)
    test(strings, 'air', -1)
    test(strings, 'film', -1)

    print('Test passed')



