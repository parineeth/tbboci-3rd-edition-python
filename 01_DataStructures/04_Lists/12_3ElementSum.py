
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_TESTS = 50
MAX_NUM_ELEMS = 10
MAX_VALUE = 10




def handle_error() :
    print('Error occured')
    sys.exit(1)







#a: input list 
#S: the addition of any 3 elements in list should be equal to S
#Returns: Number of 3 elements subsets where sum of 3 elements is equal to S
def find_3_element_sum(a, S) :
    #Sort the list in non-decreasing order
    a.sort()

    count = 0
    for  i in range(len(a) - 2):
        #Choose a[i]. Start picking the other two elements from 
        #opposite ends. So start choosing from i+1 on one side and
        #length - 1 on the other side
        low = i + 1
        high = len(a) - 1
        while (low < high) :
            total = a[i] + a[low] + a[high]
            if (total == S) :
                count += 1
                print('{} + {} + {} = {} '.format(a[i], a[low], 
                            a[high], total) )
                
                low += 1
                high -= 1
            elif (total > S):
                high -= 1 #We need to pick a smaller element
            else :
                low += 1 #We need to pick a larger element
            
    return count




def test() :
    length = random.randint(1, MAX_NUM_ELEMS) #randomly choose size of list
    a = []
    S = 0

    for  i in range(length):
        #Randomly choose the value of elements in the list
        a.append(random.randint(0, MAX_VALUE))

        #Alternate elements will be negative
        if (i % 2 == 0) :
            a[i] = -1 * a[i]
    

    print('Input : ', end='')
    print(a)

    result = find_3_element_sum(a, S)

    print('________________________________________________')



if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()


    print('Test passed') 


