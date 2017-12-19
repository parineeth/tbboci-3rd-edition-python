
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE     = 10
MAX_INT       = 1000000
MIN_INT       = -100000


def handle_error() :
    print('Test failed')
    sys.exit(1)







#a:input list 
#Returns: the maximum product of 3 elements in the list 
def find_max_product(a) :
    max_value = [MIN_INT] * 3
    min_value = [MAX_INT] * 2
    assert (len(a) >= 3)

    for  cur_val in a:
        #Check if cur_val is among the 3 largest values
        if (cur_val > max_value[0]) :
            max_value[2] = max_value[1]
            max_value[1] = max_value[0]
            max_value[0] = cur_val
        elif (cur_val > max_value[1]):
            max_value[2] = max_value[1]
            max_value[1] = cur_val
        elif (cur_val > max_value[2]):
            max_value[2] = cur_val
        
        #Check if cur_val is among the 2 smallest values
        if (cur_val < min_value[0]) :
            min_value[1] = min_value[0]
            min_value[0] = cur_val
        elif (cur_val < min_value[1]):
            min_value[1] = cur_val
        
    return max(max_value[0] * max_value[1] * max_value[2],
            min_value[0] * min_value[1] * max_value[0])



#a:input list 
#Returns: the maximum product of 3 elements in the list 

def brute_force_max_product(a) :
    max_product = MIN_INT

    for  i in range(len(a) - 2):
        for  j in range(i+1, len(a) - 1):
            for  k in range(j+1, len(a)):
                cur_product = a[i] * a[j] * a[k]

                if (cur_product > max_product):
                    max_product = cur_product
            

    return max_product





def test() :

    #Randomly decide the number of elements in the list
    length = random.randint(3, MAX_NUM_ELEMS)

    #Fill in random values into the list
    a = [random.randint(0, MAX_VALUE) for  i in range(length)]

    #Randomly make some of the elements negative in the list
    for  i in range(length):
        if (random.randint(0, 1) == 0) :
            a[i] = a[i] * -1


    print(a)

    #Find the result using the efficient technique
    result = find_max_product(a)

    print('Max product =  {}'.format(result) )


    #Find the result using brute force
    brute_force_result = brute_force_max_product(a)


    #The two results should match
    if (result != brute_force_result):
        handle_error()


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')




