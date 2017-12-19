
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Error occured ')
    sys.exit(1)


#a: input list whose equilibrium point has to be found. 
#Return value: index of the equilibrium point if it exists, -1 otherwise
def find_equilibrium_point(a) :
    #Compute the sum of all elements and store in right_sum
    right_sum = 0
    for  cur_value in a:
        right_sum += cur_value
    
    #Go on computing sum of all elements from the left to right and 
    #compare with right sum 
    left_sum = 0
    for  i, cur_value in enumerate(a):
        #Subtract cur_value from right_sum to find out sum of 
        #the elements to the right of i
        right_sum -= cur_value

        if (left_sum == right_sum) :
            return i #We have found the equilibrium point
        
        left_sum += cur_value

    return -1





if (__name__ == '__main__'):

    a = [-50, 100, 80, 30, -60, 10, 70]

    print('Input : ', end='')
    print(a)

    result = find_equilibrium_point(a)

    print('Equilibrium point index = {}'.format(result) )

    if (result != 2):
        handle_error()

    print('Test passed')



