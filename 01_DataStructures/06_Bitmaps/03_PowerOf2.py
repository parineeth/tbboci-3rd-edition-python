
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Error occured ')
    sys.exit(1)



def is_power_of_two( x) :
    return (x != 0) and ((x & (x-1)) == 0)




if (__name__ == '__main__'):
    #0 is not a power of 2
    if (is_power_of_two(0)) :
        handle_error()

    #10 is not a power of 2
    if (is_power_of_two(10)) :
        handle_error()

    #15 is not a power of 2
    if (is_power_of_two(15)) :
        handle_error()


    #1 is power of 2
    if (not is_power_of_two(1)) :
        handle_error()

    #2 is power of 2
    if (not is_power_of_two(2)) :
        handle_error()

    #4 is a power of 2
    if (not is_power_of_two(4)) :
        handle_error()

    #0x80000000 is a power of 2
    if (not is_power_of_two(0x80000000)) :
        handle_error()


    print('Test passed')



