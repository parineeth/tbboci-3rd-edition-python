
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Test failed')
    sys.exit(1)



#x: input integer
#Return value: parity bit, 1 if there are odd number of 1's, 0 otherwise
def compute_parity(x):
    #for each bit set to 1 in x, toggle the parity bit
    parity = 0
    while (x):
        parity = parity ^ 1
        x = x & (x - 1)

    return parity


def test(x, expected_result):

    result = compute_parity(x)

    print('Parity bit for 0x + hex(x) = {}'.format(result) )

    if (result != expected_result):
        handle_error()


if (__name__ == '__main__'):
    test(0xB, 1)
    test(0xA, 0)

    print('Test passed')
  
