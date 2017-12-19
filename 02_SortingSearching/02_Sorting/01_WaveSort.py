
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 100

def handle_error() :
    print('Test failed')
    sys.exit(1)




#a: non-empty list that has to be sorted so that the values in it 
#   alternatively increase and decrease. The elements should be unique
def wave_sort(a) :
    #Sort the elements in ascending order
    a.sort()

    #Swap the neighboring elements
    for  i in range(1, len(a) - 1, 2):
        a[i], a[i+1] = a[i+1], a[i]
    


#Generate a list without duplicates
def generate_list(length) :
    a = []
    for  i in range(length):
        while (True) :
            #Generate a random number
            temp = random.randint(0, MAX_VALUE)

            if (temp in a):
                continue
            else:
                break
        

        a.append(temp)
    
    return a




def test() :

    #Randomly pick the number of elements
    length = random.randint(1, MAX_NUM_ELEMS)

    #Generate numbers in the list without any duplicates
    a = generate_list(length)

    print ('Input : ', end='')
    print(a)

    #Perform the wave sort
    wave_sort(a)

    print ('Output: ', end='')
    print(a)


    is_prev_increasing = False
    if (length > 1 and a[0] < a[1]) :
        is_prev_increasing = True
    
        
    #Verify if the elements are alternately increasing and decreasing
    for  i in range(1, length - 1):
        is_cur_increasing = False
        if (a[i] < a[i+1]):
            is_cur_increasing = True

        if (is_prev_increasing == is_cur_increasing):
            handle_error()

        is_prev_increasing = is_cur_increasing
    



    print('_________________________________________________')



if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')







