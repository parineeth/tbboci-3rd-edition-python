
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_TESTS = 100
MAX_VALUE = 9
MAX_NUM_ELEMS = 9

def handle_error() :
    print('Test failed')
    sys.exit(1)



#a: input list 
#Returns: result[i] will contain product of all elements of list a except a[i]
def compute_product(a) :
    n = len(a)
    result = []

    #Compute the product of elements of list a in forward direction.
    #Store product of a[0] to a[i-1] in result[i]
    product = 1
    for  cur_value in a:
        result.append(product)
        product = cur_value * product 
    

    #Next compute the product of elements of list a in reverse direction
    #So we now compute product of a[n-1] to a[i+1] and multiply it with 
    #value in result[i]. In this way result[i] will contain product of 
    #a[0]...a[i-1]*a[i+1]....a[n-1]
    product = 1
    for  i in range(n - 1, -1,-1):
        result[i] = result[i] * product
        product = a[i] * product 
    
    return result



def verify_result(a, result) :
    for  i in range(len(a)):
        expected_result = 1
        for  j, cur_value in enumerate(a):
            if (i != j) :
                expected_result = expected_result * cur_value           
        

        if (expected_result != result[i]):
            handle_error()
    



def test() :
    length = random.randint(1, MAX_NUM_ELEMS)

    a = [random.randint(1, MAX_VALUE) for  i in range(length)]

    print('Input  : ', end='')
    print(a)

    result = compute_product(a)

    print('Output : ', end='')
    print(result)

    verify_result(a, result)

    print('_________________________________________')


if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed ')





