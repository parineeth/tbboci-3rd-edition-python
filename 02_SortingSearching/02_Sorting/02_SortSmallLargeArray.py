
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_TESTS = 10
MAX_NUM_ELEMS  = 10
MAX_VALUE = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)




#a: list of size m+n which has m elements at beginning 
#b: list of size n with n elements
#m: number of elements in list a
#n: number of elements in list b
def merge_lists(a, b, m, n) :
    i = m - 1
    j = n - 1
    fill_pos = m + n - 1 #Start filling from the rear of list a

    while (i >= 0 and j >= 0) :
        if (a[i] > b[j]) :
            a[fill_pos] = a[i]
            fill_pos -= 1
            i -= 1
        else :
            a[fill_pos] = b[j]
            fill_pos -= 1
            j -= 1
        
    #Fill up the remaining elements of list a if any
    while (i >= 0):
        a[fill_pos] = a[i]
        fill_pos -= 1
        i -= 1

    #Fill up the remaining elements of list b if any
    while (j >= 0):
        a[fill_pos] = b[j]
        fill_pos -= 1
        j -= 1





def verify_result(a, num_elems) :
    prev = 0
    for  i, cur_value in enumerate(a):
        if (i > 0 and prev > cur_value):
            handle_error()

        prev = cur_value



#Sort in ascending order using simple bubble sort
def sort_list(a, n) :
    for  i in range(n - 1):
        for  j in range(i + 1, n):
            if (a[i] > a[j]) :
                a[i], a[j] = a[j], a[i]
            
        
    



def test01() :

    #Generate two random values m and n
    n = random.randint(1, MAX_NUM_ELEMS)
    m = random.randint(1, MAX_NUM_ELEMS)

    #Let a have size of (m+n) and b have a size of n
    a = [0] * (m+n)

    #Generate m random values in a
    for  i in range(m):
        a[i] = random.randint(0, MAX_VALUE)
    

    #Generate n random values in b
    b = [random.randint(0, MAX_VALUE) for  i in range(n)]
    

    #Sort the two lists. We are using a special sort function for list a  
    #since size of a is m+n, but we have only m elements in a
    sort_list(a, m)
    b.sort()

    print('Input1 : ', end='')
    print(a[0:m])
    print('Input2 : ', end='')
    print(b)

    #Merge the lists
    merge_lists(a, b, m, n)

    print('Output : ', end='')
    print(a)
    
    verify_result(a, m+n)

    print('____________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test01()

    print('Test passed')






