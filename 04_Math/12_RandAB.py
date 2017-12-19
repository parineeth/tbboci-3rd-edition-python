
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_TRIALS  = 50


def handle_error() :
    print('Test failed')
    sys.exit(1)


#Return value: returns 0 with a probability of 0.5 and 1 with a probability of 0.5
def binary_rand() :
    rand_num = random.randint(0, 1)
    return rand_num 


#Returns number x where a <= x <= b and x is uniformly distributed
def get_random_num(a, b) :
    num_outcomes = b - a + 1

    while (True) :
        rand_num = 0
        i = 0
        while ( (1 << i) < num_outcomes) :
            #Append the random binary digit to the end
            rand_num = (rand_num << 1) | binary_rand()
            i += 1

        if (rand_num < num_outcomes):
            break
        #If rand_num >= num_outcomes, we try again
     
    return rand_num + a




def test(a, b) :

    print('Generating random numbers from {} to {}'.format(a, b) )

    for  i in range(MAX_NUM_TRIALS):
        outcome = get_random_num(a, b)

        print(outcome)

        if (outcome < a or outcome > b) :
            handle_error()
    

    print('____________________________________')



if (__name__ == '__main__'):
    test(0, 0)
    test(0, 1)
    test(1, 10)
    test(100, 500)  

    print('Test passed')





