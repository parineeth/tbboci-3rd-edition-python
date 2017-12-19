
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random





MAX_NUM_TESTS = 100
MAX_NUM_ELEMS = 10
MAX_VALUE = 1

def handle_error() :
    print('Test failed')
    sys.exit(1)





#a: input list in which the zeroes should be moved to one end
def move_zeroes(a) :
    left = 0
    right = len(a) - 1

    while (left < right) :
        #Locate the first zero from the left
        while (left < len(a) and a[left] != 0):
            left += 1

        #Locate first non-zero from the right
        while (right >= 0 and a[right] == 0):
            right -= 1

        if (left < right) :
            #Swap a[left] and a[right]
            a[left], a[right] = a[right], a[left]
        
    





def verify(a)  :
    found_zero = False
    for  i in range(len(a)):
        if (a[i] == 0) :
            found_zero = True
        
        else :
            #We have found a non-zero. Since all zeroes are at the end,
            #we should not have found a zero till now
            if (found_zero):
                handle_error()
        
    




def test() :


    #Randomly decide the number of elements
    length = random.randint(1, MAX_NUM_ELEMS)

    #Fill the list with random values
    a = [random.randint(0, MAX_VALUE) for  i in range(length)] 
    

    print ('Original list : ', end='')
    print(a)


    #Move zeroes to the right 
    move_zeroes(a)

    print ('After moving 0 : ', end='')
    print(a)

    verify(a)


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()


    print('Test passed')



