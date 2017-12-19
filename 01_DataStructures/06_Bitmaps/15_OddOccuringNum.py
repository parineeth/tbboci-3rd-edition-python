
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys







def handle_error() :
    print('Test failed')
    sys.exit(1)




#a: list consisting of numbers, where one element occurs odd number of times 
#   while remaining elements occur even number of times 
#Return value: element that occurs odd number of times
def find_odd_occurrence(a) :
    #XOR all the elements
    result = 0
    for  cur_value in a :
        result = result ^ cur_value
    
    return result



def test() :
    a = [1, 8, 4, 8, 2, 1, 4]

    print('Input : ', end='')
    print(a)

    result = find_odd_occurrence(a)

    print('Element that occurs odd number of times = {}'.format(result) )

    expected_result = 2
    if (result != expected_result):
        handle_error()




if (__name__ == '__main__'):
    test()
    print('Test passed ')




