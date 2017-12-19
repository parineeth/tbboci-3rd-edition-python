
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 100
MAX_NUM_STATIONS = 10
MAX_DISTANCE = 100

def handle_error() :
    print('Error occured ')
    sys.exit(1)



#gas: the amount of gas available at each gas station. The total gas in all 
#   stations should be sufficient to complete the circular trip 
#distance: distance[i] has the distance between gas station i and i+1
#mileage: how much distance can the car travel for 1 unit of gas consumed
#Return value: station from where to start so that we don't run out of fuel and
#   complete the circular trip around all stations
def find_starting_gas_station(gas, distance, mileage) :
    num_stations = len(gas)
    assert(num_stations)

    #Station from where to start the journey so that we don't run out of fuel
    starting_station = 0 

    least_gas = 0 #Tracks the least amount of gas in fuel tank
    gas_in_tank = 0 #Tracks how much fuel is currently present in fuel tank
    for  i, (gas_in_station, cur_distance) in enumerate(zip(gas, distance)):
        gas_required = cur_distance // mileage
    
        #At station i, we fill up gas_in_station and then as we drive,  
        #we consume gas_required to reach the destination station = 
        #(i+1) % num_stations 
        gas_in_tank += gas_in_station - gas_required 
        if (gas_in_tank < least_gas) :
            least_gas = gas_in_tank
            #The starting station is the station where we have
            #the least amount of gas in the tank just before we fill up
            starting_station = (i+1) % num_stations
        
    return starting_station


#Verifies if we start at starting_station, we can complete the journey without running out of fuel
def verify(starting_station, gas, distance, mileage) :
    num_stations = len(gas)

    #Check if starting_station is out of range
    if (starting_station < 0 or starting_station >= num_stations):
        handle_error()

    cur_station = starting_station
    gas_in_tank = 0
    for  i in range(1, num_stations):
        gas_required = distance[cur_station] // mileage
        gas_in_tank += gas[cur_station] - gas_required

        #gas in the fuel tank should always be >= 0
        if (gas_in_tank < 0) :
            handle_error()
        
        cur_station = (cur_station + 1) % num_stations
    




def test() :

    #Randomly pick the number of gas stations
    num_stations = random.randint(1, MAX_NUM_STATIONS)

    gas = [0] * num_stations
    distance = [random.randint(1, 10) for  i in range(num_stations)] 

    total_distance = sum(distance)

    #We are fixing the mileage to 1 mile/gallon since we will
    #not have to deal with fractional values
    mileage = 1

    #Compute the gas needed to complete the journey around all stations
    total_gas = total_distance // mileage

    #Randomly distribute the total_gas among the gas stations
    remaining_gas = total_gas
    per_station_quota = remaining_gas // num_stations
    for  i in range(num_stations):
        if (remaining_gas > 0):
            gas[i] = random.randint(0, per_station_quota - 1)
        else :
            gas[i] = 0 
        remaining_gas -= gas[i]
     

    #If there is any gas left over, then distribute the 
    #remaining gas equally among the gas stations
    i = 0
    per_station_quota = remaining_gas // num_stations
    while (remaining_gas > 0 and i < num_stations - 1) :
        gas[i] += per_station_quota
        remaining_gas -= per_station_quota
        i += 1
    
    #If there is still any gas left over, give it to the last gas station
    gas[num_stations - 1] += remaining_gas 

    print('Gas      : ', end='')
    print(gas)


    print('Distance : ', end='')
    print(distance)

    #Find the gas station from where to start the journey
    #IMPORTANT: ensure that while calling this function that the sum of gas in all
    #the stations should be sufficient to complete the journey
    starting_station = find_starting_gas_station(gas, distance, mileage)

    print('Starting station = {}'.format(starting_station) )

    verify(starting_station, gas, distance, mileage)

    print('____________________________________________________')





if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')



