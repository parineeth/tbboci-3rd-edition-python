
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




def handle_error() :
    print('Test failed')
    sys.exit(1)



#a: input list of unsorted numbers
#k: number of random values to pick
#Return value: the k random values will be stored in result
def pick_random_values(a, k) :
    #We will need to rearrange the elements in list a. Since the user
    #may expect list a to remain unchanged, we are allocating memory 
    #for another list b and copying elements of a into b
    b = a[:]

    result = [] 

    j = 0
    last_index = len(a) - 1 
    while (j < k) :
        #Pick a random position from 0 to last_index
        rand_index = random.randint(0, last_index)

        #Store b[rand_index] in the result
        result.append(b[rand_index])

        #Let's say original value at b[rand_index] is x.
        #b[rand_index] is now overwritten with b[last_index].  
        #So we cannot choose x again in the next iterations
        b[rand_index] = b[last_index]

        last_index -= 1
        j += 1
    
    return result







if (__name__ == '__main__'):
    a = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    k = 5   #number of random values to be chosen


    print('Input : ', end='')
    print(a)

    result = pick_random_values(a, k)

    print('The random values are: ', end='')
    print(result)   

    print('Test passed')






