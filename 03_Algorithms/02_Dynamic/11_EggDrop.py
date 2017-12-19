
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




MAX_NUM_TESTS = 100
MAX_INT = 9999999

def handle_error() :
    print('Error occured ')
    sys.exit(1)


#num_eggs: total number of identical eggs available. should be >= 1 
#num_floors: total number of floors available. should be >= 1
#Return value: minimum number of throws with which we can find egg strength
def find_min_egg_drops(num_eggs, num_floors) :
    min_throws = [[0 for y in range(num_floors + 1)] for x in 
                            range(num_eggs + 1)]

    #If there is only 1 floor, we need only 1 throw
    for  cur_egg in range(1, num_eggs+1):
        min_throws[cur_egg][1] = 1

    #If there is only 1 egg and k floors, we need k throws
    for  cur_floor in range(1, num_floors+1):
        min_throws[1][cur_floor] = cur_floor

    for  cur_egg in range(2, num_eggs+1):
        for  cur_floor in range(2, num_floors+1):
            min_throws[cur_egg][cur_floor] = MAX_INT

            for  floor_iter in range(1, cur_floor+1):
                #Find the number of throws needed from floor_iter
                num_throws = max(
                    1 + min_throws[cur_egg - 1][floor_iter - 1],
                    1 + min_throws[cur_egg][cur_floor -floor_iter])

                if (min_throws[cur_egg][cur_floor] > num_throws):
                    min_throws[cur_egg][cur_floor] = num_throws

    return min_throws[num_eggs][num_floors]



def test(num_eggs, num_floors, expected_result) :

    result = find_min_egg_drops(num_eggs, num_floors)

    print('Num eggs = {} num floors = {}, minimum throws = {} '.format(num_eggs, num_floors, result) )

    if (result != expected_result):
        handle_error() 



if (__name__ == '__main__'):
    test(2, 100, 14)
    test(2, 36, 8)

    print('Test passed')



