
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys






def handle_error() :
    print(  'Error occured')
    sys.exit(1)



#tickets: list which stores the information about the tickets bought. 
#   ticket[i][0] stores the starting city of the ith ticket
#   ticket[i][1] stores the destination city of the ith ticket
#   There should be no loop in the trip
#   There should be at least 1 ticket 
#Return value: list containing the names of cities in the order of travel 
def reconstruct_trip(tickets) :
    num_tickets = len(tickets)
    next_hop = {}
    destinations = set()

    #Store the starting city (key) and destination city (value) in next_hop 
    #dictionary. Store the destination cities in destinations set
    for  start, dest in tickets:
        next_hop[start] = dest
        destinations.add(dest)
    
    #Search the starting city of each ticket in the destinations 
    #Only the first city of the entire trip will NOT be in destinations 
    start_index = -1
    i = 0
    for  start, dest in tickets:
        if (start not in destinations) :
            #We didn't find the city in the destinations.
            #So this must be the first city of the entire trip
            start_index = i
            break
        i += 1
    
    if (start_index == -1):
        return None

    result = []

    #add the first city of entire trip into the result
    result.append(tickets[start_index][0]) 

    #Search for the first city of the entire trip in the next_hop dictionary
    next_city = next_hop.get(tickets[start_index][0])

    while (next_city) :
        #Store the destination city in the result
        result.append(next_city) 

        #make the destination city as the next starting city 
        #and search for it in the next_hop dictionary
        next_city = next_hop.get(next_city) 
    
    return result
 


def verify(result) :
    expected = ['LA', 'SF', 'TOKYO', 'BEIJING', 'DELHI', 'ROME']

    for  result_city, expected_city in zip(result, expected) :
        if (result_city != expected_city):
            handle_error()
    


def test() :
    tickets = [['TOKYO', 'BEIJING'], ['LA', 'SF'], ['DELHI', 'ROME'], ['SF', 'TOKYO'], ['BEIJING', 'DELHI']]
    num_tickets = 5

    for  i in range(num_tickets):
        print(  tickets[i][0] + ' -> ' + tickets[i][1] )
    

    print(  'The order of visiting: ', end='')
    result = reconstruct_trip(tickets)

    for city in  result :
        print(city + ' ', end='')
    
    print('')

    verify(result)


if (__name__ == '__main__'):
    test()
    print(  'Test passed ')



