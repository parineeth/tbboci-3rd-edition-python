
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys







def handle_error() :
    print('Test failed')
    sys.exit(1)




#a: list of unique numbers. A number can have a value between 1 to n
#n: maximum value that can be stored in the list. list has n-1 elements
#Return value: missing element in the list
def find_missing(a, n) :
    #Since 1 element is missing, there are only n-1 elements in the list
    total_sum = 0
    for  i in range(n - 1):
        total_sum += a[i]
    
    expected_sum = n * (n+1) // 2

    missing_num = expected_sum - total_sum
    return missing_num



def test() :
    a = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    length = 9 #Number of elements in the list

    print('Input : ', end='')
    print(a)

    result = find_missing(a, length+1)

    print('Missing element = {}'.format(result) )

    expected_result = 5
    if (result != expected_result):
        handle_error()




if (__name__ == '__main__'):
    test()
    print('Test passed ')



