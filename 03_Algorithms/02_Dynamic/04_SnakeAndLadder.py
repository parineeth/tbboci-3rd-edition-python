
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



MAX_POSITIONS_ON_BOARD  = 100


def handle_error() :
    print('Error occured ')
    sys.exit(1)


#is_snake: if there is a snake at position 20, is_snake[20] is set to True
#ladder:  if there is a ladder from position 30 to 44, then ladder[44] = 30.
#   if there is no ladder at location 90 then ladder[90] = -1
#Return value:  1. least number of throws to reach the position on the board
#       2. predecessor list
def find_least_throws(is_snake, ladder) :

    #for a particular position pos on the board, least_throws[pos] will store
    #the least number of dice throws required to reach the position
    least_throws = [0] * (MAX_POSITIONS_ON_BOARD + 1)

    #predecessor list has the previous board position from where we came to 
    #current position with least number of dice throws. If predecessor[100]   
    # = 95, then we reached 100 from 95.
    predecessor = [0] * (MAX_POSITIONS_ON_BOARD + 1) 

    #All positions from 1 to 6 can be reached from a single dice throw
    for  pos in range(1, 7):
        least_throws[pos] = 1
        predecessor[pos] = 0
    
    for  pos in range(7, MAX_POSITIONS_ON_BOARD+1):
        min_throws = MAX_POSITIONS_ON_BOARD

        #Find how many dice throws are needed to reach pos from any of 
        #the 6 previous cells
        for  i in range(1, 7):
            prev_pos = pos - i

            if (is_snake[prev_pos]):
                continue

            #Pick the minimum throws needed from the 6 previous cells
            if (least_throws[prev_pos] + 1 < min_throws) :
                min_throws = least_throws[prev_pos] + 1
                predecessor[pos] = prev_pos
            

        #Suppose we are at pos = 14 and ladder[14] = 4, then there is a ladder
        #from 4 to 14. So number of dice throws needed to reach 14 = number of 
        #dice throws needed to reach position 4
        ladder_start_pos = ladder[pos]
        if (ladder_start_pos != -1) :
            if (least_throws[ladder_start_pos] < min_throws) :
                min_throws = least_throws[ladder_start_pos]
                predecessor[pos] = ladder_start_pos
            
        least_throws[pos] = min_throws

    return least_throws[MAX_POSITIONS_ON_BOARD], predecessor




def test() :
    is_snake = [False] * (MAX_POSITIONS_ON_BOARD + 1)
    ladder = [-1] * (MAX_POSITIONS_ON_BOARD + 1)
    

    #if there is a snake at position 20 on board, the is_snake[20] is set to True
    is_snake[17] = True
    is_snake[54] = True
    is_snake[62] = True
    is_snake[64] = True
    is_snake[87] = True
    is_snake[93] = True
    is_snake[95] = True
    is_snake[99] = True

    #if there is a ladder from position 30 to 44, then ladder[44] = 30.
    #if there no ladder at location 90 then ladder[90] = -1
    ladder[14] = 4
    ladder[31] = 9
    ladder[38] = 20
    ladder[84] = 28
    ladder[59] = 40
    ladder[67] = 51
    ladder[81] = 63
    ladder[91] = 71

    min_throws, predecessor = find_least_throws(is_snake, ladder)

    print('Least number of throws = {}'.format(min_throws) )

    if (min_throws != 7):
        handle_error()

    print('The positions on the board corresponding to dice throws in reverse order are: ')

    i = MAX_POSITIONS_ON_BOARD
    print(i)
    while (i > 0): 
        print(predecessor[i])
        i = predecessor[i]
     


if (__name__ == '__main__'):
    test()
    print('Test passed')




