
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Error occured ')
    sys.exit(1)


def set_bit( n,  pos)  :
    n = n | (1 << pos)
    return n


def reset_bit( n,  pos) :
    n = n & ~(1 << pos)
    return n



def toggle_bit( n,  pos)  :
    n = n ^ (1 << pos)
    return n




if (__name__ == '__main__'):
    if (set_bit(0xf0, 3) != 0xf8):
        handle_error()

    if (reset_bit(0xf8, 3) != 0xf0):
        handle_error()

    if (toggle_bit(0xf0, 7) != 0x70):
        handle_error()

    print('Test passed')





