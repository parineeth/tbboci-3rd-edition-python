
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




#Keep the number of coin flips >= 1000 so that we have sufficient number of flips
MAX_COIN_FLIPS  = 1000


def handle_error() :
    print('Test failed')
    sys.exit(1)


#Return value: returns 0 with a probability of 0.7 and 1 with a probability of 0.3
def toss_unfair_coin():
    rand_num = random.randint(0, 9)

    if (rand_num <= 6) :
        #If we get a number from 0 to 6, return 0.
        #So likelihood of getting 0 is 0.7 
        return 0
    else :
        #If we get a number from 7 to 9, return 1
        #So likelihood of getting 1 is 0.3
        return 1
    
    


#Returns 0 with a probability of 0.5 and 1 with a probability of 0.5
def toss_fair_coin() :
    while (True) :
        x = toss_unfair_coin()
        y = toss_unfair_coin()

        if (x == 0 and y == 1):
            return 0 
        elif (x == 1 and y == 0):
            return 1
    





def test():

    num_heads = num_tails = 0
    for  i in range(MAX_COIN_FLIPS):
        outcome = toss_fair_coin()

        if (outcome == 0) :
            num_heads += 1
        elif (outcome == 1):
            num_tails += 1
        else :
            handle_error()


    print('Number of heads = {} Number of tails = {}'.format(num_heads, num_tails) )

    diff = abs(num_heads - num_tails) / 2

    #The difference between number of heads and number of tails should not be more than
    #5% of the total number of coin flips
    if (diff > (5 * MAX_COIN_FLIPS / 100)) :
        handle_error()


if (__name__ == '__main__'):
    test()
    print('Test passed')




