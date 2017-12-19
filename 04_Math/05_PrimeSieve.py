
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





def handle_error() :
    print('Test failed')
    sys.exit(1)



#n: Upto what number the primes should be generated
def generate_primes(n) :
    #is_multiple will be initialized with False since we have not yet 
    #identified the multiples
    is_multiple = [False] * (n+1)

    #We don't consider 0 and 1 as prime. Start from 2
    for  i in range(2, n+1):
        if (is_multiple[i]) :
            continue #i is a multiple, so it can't be prime
    
        print('{} is prime '.format(i) )

        #Mark all multiples of i (2i, 3i, 4i, etc) starting from 2i 
        for  j in range(2*i, n+1, i):
            is_multiple[j] = True
         
    




if (__name__ == '__main__'):
    generate_primes(100)

    print('Test passed ')







