
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)



#a: input list from which all occurrences of an element should be removed
#x: element to be removed
def remove_element(a, x) :
    fill_pos = 0
    for  cur_value in a:
        if (cur_value != x) :
            a[fill_pos] = cur_value
            fill_pos += 1
    
    #delete all the elements from fill_pos onwards  
    if (fill_pos < len(a)) :
        del a[fill_pos:]







def test() :

    #Randomly decide the number of elements
    length1 = random.randint(1, MAX_NUM_ELEMS)

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for i in range(length1)]

    #Pick an element in list to be deleted
    rand_pos = random.randint(0, length1 - 1)
    x = a[rand_pos]

    print('Element to remove: {}'.format(x) )

    print ('Original list : ', end='')
    print(a)


    #Remove the element x 
    remove_element(a, x)

    print ('After removing : ', end='')
    print(a)

    if (x in a):
        handle_error()


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')



