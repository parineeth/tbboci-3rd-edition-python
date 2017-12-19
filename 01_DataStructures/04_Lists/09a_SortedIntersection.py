
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




#a, b: two input lists whose intersection has to be found
#Returns: list containing the result of intersection of a and b
def find_intersection(a,  b) :
    result = []

    #Sort the two lists
    a.sort()
    b.sort()

    i = j = result_pos = 0
    while (i < len(a) and j < len(b)) :
        #Check if the elements in a and b match
        if (a[i] == b[j]) :
            #Add only unique elements to the result
            if (i == 0 or a[i] != a[i - 1]) :
                result.append(a[i])
            
            i += 1
            j += 1

        elif (a[i] < b[j]):
            i += 1
        else :
            j += 1

    return result








#a, b: two input lists whose intersection has to be found
#Returns: list containing the result of intersection of a and b
def brute_force_intersection(a,  b):
    result = []

    for  val in a:
        #Search for val in list b
        if (not val in b):
            continue

        #We have found val in b. Now make sure that val is not 
        #already present in the result
        if (not val in result) :
            #val is present in a and b and val is not present in result. So add 
            #it to result
            result.append(val)
    
    return result



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

    #Find the intersection of a and b. The result will be in c
    c = find_intersection(a, b)

    print ('Intersection : ', end='')
    print(c)

    #Apply brute force to find the intersection. The result will be in d
    d = brute_force_intersection(a, b)

    #The two results should match
    if (c != d):
        handle_error()

    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()

    print('Test passed')




