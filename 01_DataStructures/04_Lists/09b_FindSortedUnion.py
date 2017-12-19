
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random




MAX_NUM_TESTS = 10
MAX_NUM_ELEMS = 10
MAX_VALUE = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)




#a, b: two input lists whose union has to be found
#Returns: list containing the result of union of a and b
def find_union(a, b) :
    if (len(a) + len(b) == 0):
        return []

    result = []

    #sort a and b 
    a.sort()
    b.sort()
    
    #Process as long as there are elements in both a and b. 
    #Pick the smaller element among a[i] and b[j] and if it
    #doesn't match with last element in result, add it to result
    i = j = 0
    while (i < len(a) and j < len(b)) :
        if (a[i] <= b[j]) :
            if (len(result) == 0 or a[i] != result[-1]):
                result.append(a[i])
            
            if (a[i] == b[j]):
                j += 1 #advance b

            i += 1

        else :
            if (len(result) == 0 or b[j] != result[-1]):
                result.append(b[j])
            j += 1
        
    #Process the remainder elements in a
    while (i < len(a)) : 
        if (len(result) == 0 or a[i] != result[-1]):
            result.append(a[i])
        i += 1

    #Process the remainder elements in b
    while (j < len(b)):
        if (len(result) == 0 or b[j] != result[-1]):
            result.append(b[j])
        j += 1

    return result



#Adds all the unique items of list a into the result list
#a: input list
#result: the result will have the unique elements of list a appended to the result
#   result will store only unique elements
def brute_force_unique(a, result):
    for  val in a:
        if (not val in result):
            result.append(val)
    


def test() :

    #Randomly decide the number of elements in the two lists
    length1 = random.randint(1, MAX_NUM_ELEMS)
    length2 = random.randint(1, MAX_NUM_ELEMS)

    #Fill the lists with random values
    a = [random.randint(0, MAX_VALUE) for  i in range(length1)]
    b = [random.randint(0, MAX_VALUE) for  i in range(length2)]
    

    print ('A : ', end='')
    print(a)

    print ('B : ', end='')
    print(b)

    #Find the union of a and b. The result will be in c
    c = find_union(a,  b)

    print ('Union : ', end='')
    print(c)


    #Find the union using brute force. The result will be in d
    d = []  
    brute_force_unique(a, d)
    brute_force_unique(b, d)

    #c and d should match. Since c is sorted, but d is not, we need to sort d
    d.sort() 

    #The efficient result should match with the brute force result
    if (c != d):
        handle_error()
    


    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()
    
    print('Test passed')




