
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

try: 
    import queue
except ImportError:
    import Queue as queue



def handle_error() :
    print('Test failed')
    sys.exit(1)


#There is no peek functionality in python stack. So we are doing a get
#followed by an immediate put to mimic the peek
def peek(stack):
    result = stack.get()
    stack.put(result)
    return result


#histo_height: histo_height[i] has height of ith bar. Should not be empty
#Return value: returns the area of the largest rectangle in the histogram
def find_max_area(histo_height) :
    max_area = 0
    n = len(histo_height)
    height_stack = queue.LifoQueue() #stack stores the height of the bars
    index_stack = queue.LifoQueue() #stack stores the index of the bars

    for  i in range(n):

        if ( height_stack.empty() or 
        histo_height[i] > peek(height_stack) ) :
            #push height and index of current bar
            height_stack.put(histo_height[i])
            index_stack.put(i)

        elif (histo_height[i] < peek(height_stack)):

            while (not height_stack.empty() and 
            histo_height[i] < peek(height_stack)) :
                # keep popping from index and height stacks
                popped_index = index_stack.get()
                popped_height = height_stack.get()

                # calculate the area from popped bar to 
                #the current bar. 
                #Area = popped height * difference of index of 
                #current bar and popped bar
                area =  popped_height * (i - popped_index)

                if (area > max_area):
                    max_area = area
            
            #push the height of the current bar into the height stack 
            height_stack.put(histo_height[i])

            #push the LAST POPPED INDEX into the index stack, 
            #since we can form a rectangle from the LAST POPPED INDEX 
            #to the current bar (where the height of the rectangle is 
            #height of current bar)
            index_stack.put(popped_index)


    #Process the remaining elements in the stacks
    while (not height_stack.empty() ) :
        popped_index = index_stack.get()
        area = height_stack.get() * (n - popped_index)

        if (area > max_area):
            max_area = area
    
    return max_area






def test01() :
    histo_height = [3, 2, 5, 6, 1, 4, 4]

    max_area = find_max_area(histo_height)

    print('Histogram: ', end='')
    print(histo_height)
    print('Max area = {}'.format(max_area) )

    if (max_area != 10):
        handle_error()

    print('____________________________________')



def test02() :
    histo_height = [2, 4, 2, 1]

    max_area = find_max_area(histo_height)

    print('Histogram: ', end='')
    print(histo_height)
    print('Max area = {}'.format(max_area) )

    if (max_area != 6):
        handle_error()

    print('____________________________________')




if (__name__ == '__main__'):
    test01()

    test02()

    print('Test passed ')



