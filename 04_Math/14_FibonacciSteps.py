
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





MAX_N_STEPS = 20


def handle_error() :
    print('Test failed')
    sys.exit(1)



#n: number of steps. n >= 1
#Returns: the number of ways to climb the steps
def climb_steps(n) :
    #Directly return the value for the first two numbers in the series
    if (n <= 2):
        return n

    x = 1
    y = 2
    for i in range(3, n+1):
        temp = x + y
        x = y
        y = temp
     
    return y


#n: number of steps. n >= 1
#Returns: the number of ways to climb the steps using recursion
def climb_steps_r(n) :
    if (n <= 2):
        return n

    return climb_steps_r(n-1) + climb_steps_r(n-2)




if (__name__ == '__main__'):
    for i in range(1, MAX_N_STEPS+1):
        #Find the number of ways to climb steps non-recursively
        a = climb_steps(i)

        #Find the number of ways to climb steps recursively
        b = climb_steps_r(i)

        if (a != b):
            handle_error()

        print('Number of steps = {}, Number of ways to climb = {}'.format(i, a) )



    print('Test passed')




