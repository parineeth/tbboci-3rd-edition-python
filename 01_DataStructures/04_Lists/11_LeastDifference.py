
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE     = 100
MAX_INT       = 1000000

def handle_error() :
    print('Test failed')
    sys.exit(1)







#a:input list 
#Returns: the least absolute difference between any two elements in the list 
def find_least_difference(a) :
    assert (len(a) > 1)

    #Sort the list in non-decreasing order
    a.sort()

    least_difference = a[1] - a[0]
    for  i in range(1, len(a) - 1):
        if (a[i+1] - a[i] < least_difference):
            least_difference = a[i+1] - a[i]
    
    return least_difference



#a:input list 
#length: number of elements in list a
#Returns: the least absolute difference between any two elements in the list 
def brute_force_least_difference(a) :
    least_difference = MAX_INT

    for  i in range(len(a) - 1):
        for  j in range(i+1, len(a)):
            if (abs(a[i] - a[j]) < least_difference):
                least_difference = abs(a[i] - a[j])
        
    return least_difference




def test() :

    #Randomly decide the number of elements in the list
    length = random.randint(2, MAX_NUM_ELEMS)

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]
    
    print(a)

    #Find the least difference using brute force
    brute_force_result = brute_force_least_difference(a)


    #Find the least difference using the efficient technique
    result = find_least_difference(a)

    print('Least difference = {}'.format(result) )


    #The two results should match
    if (result != brute_force_result):
        handle_error()


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')



