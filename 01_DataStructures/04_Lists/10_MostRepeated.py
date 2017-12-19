
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



MIN_INT = -100000

def handle_error() :
    print('Test failed')
    sys.exit(1)




#a: list consisting of numbers. A number can have a value between 0 to k-1
#k: k should be <= num elements in list
def find_most_repeated(a,  k) :
    #For each number found in the list, go to the index corresponding to 
    #the number and add k to the value at the index. 
    for  i, cur_value in enumerate(a):
        #By the time we come to location i, we might have already added k  
        #to the value at this location one or more times. 
        #So take a[i] % k to get the original value
        index = cur_value % k
        a[index] += k
    
    most_repeated = -1
    max_value = MIN_INT
    for  i, cur_value in enumerate(a):
        if (cur_value > max_value) :
            #Note that index i will give the most repeated number
            most_repeated = i
            max_value = cur_value
        
        #Get back the original value in the list
        a[i] = cur_value % k
    

    return most_repeated



def test() :
    a = [2, 4, 0, 5, 2, 1, 9, 6, 8, 9, 2, 7]
    n = 12 #Number of elements in the list
    k = 10 #The value of all numbers in the list are less than k and k <= n 

    result = find_most_repeated(a, k)

    print('Input  : ', end='')
    print(a)

    print('Most repeated element = {}'.format(result) )

    print('Output : ', end='')
    print(a)

    expected_result = 2
    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    test()
    print('Test passed ')



