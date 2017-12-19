
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Error occured ')
    sys.exit(1)






#arrival: list containing the arrival time of the trains
#departure: list containing the departure time of the trains
#Return value: minimum number of train platforms needed 
def find_min_platforms(arrival, departure) :
    n = len(arrival)
    if (n == 0):
        return 0

    #Sort the arrival and departure time independently in non-decreasing order
    arrival.sort()
    departure.sort()

    cur_num_platforms = min_num_platforms = 1
    i = 1 #i is used for traversing arrival
    j = 0 #j is used for traversing departure

    while (i < n and j < n) :
        if (arrival[i] < departure[j]) :
            #A new train is coming in before a train departs. So  
            #we need an extra platform
            cur_num_platforms += 1
            if (cur_num_platforms > min_num_platforms):
                min_num_platforms = cur_num_platforms
            i += 1
        elif (arrival[i] == departure[j]):
            #A train arrives at the same time as a departing train. 
            #So we don't need an extra platform
            i += 1
            j += 1
        else :
            #A train departs before the new train arrives. 
            #So a platform is freed up
            cur_num_platforms -= 1
            j += 1
        
    return min_num_platforms





def test01() :
    arrival = [800, 900, 945, 1300, 1500, 1530, 1545] 
    departure = [1030, 915, 1100, 1400, 1545, 1830, 1715]

    print('Arrival: ', end='')
    print(arrival)

    print('Departure: ', end='')
    print(departure)

    result = find_min_platforms(arrival, departure)

    print('Minimum number of platforms = {}'.format(result) )

    expected_result = 2

    if (result != expected_result):
        handle_error()

    print('__________________________________')





if (__name__ == '__main__'):
    test01()
    print('Test passed')



