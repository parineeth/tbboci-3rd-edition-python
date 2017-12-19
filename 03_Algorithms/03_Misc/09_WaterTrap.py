
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Error occured')
    sys.exit(1)




#histogram: histogram[i] contains the height of the bar at location i
#   histogram should consist of at least one bar
#Return value: amount of water that can be trapped by the histogram 
def water_trap(histogram) :
    n = len(histogram) #number of bars in the histogram
    left_max = [0] * n
    right_max = [0] * n

    #The left max of bar i is the height of the tallest bar in the 
    #region (0, i). Note that region (0, i) includes 0 and i
    left_max[0] = histogram[0]
    for  i in range(1, n):
        left_max[i] = max(left_max[i-1], histogram[i])
    

    #The right max of bar i is the height of the tallest bar in the 
    #region (i, n-1). Note that region (i, n-1) includes i and n-1
    total_water = 0
    right_max[n-1] = histogram[n-1]
    for  i in range(n - 2, -1,-1):
        #Compute the right max and simultaneously calculate the 
        #amount of water that can be trapped
        right_max[i] = max(right_max[i+1], histogram[i])
    
        smaller_max = min(left_max[i], right_max[i])

        #calculate the amount of water that can be stored
        #on top of the histogram bar i
        total_water += smaller_max - histogram[i]
    
    return total_water



def test() :
    histogram =  [3, 1, 4, 0, 2, 5, 0, 3, 2]
    total_water = water_trap(histogram)

    print('Total water trapped = {}'.format(total_water) )

    if (total_water != 11):
        handle_error()




if (__name__ == '__main__'):
    test()
    print('Test passed ')





