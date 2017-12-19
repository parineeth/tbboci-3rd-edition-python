
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random

try: 
    import queue
except ImportError:
    import Queue as queue


MAX_NUM_STACK_ELEMS = 10
MAX_VALUE = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)
    

#There is no peek functionality in python stack. So we are doing a get
#followed by an immediate put to mimic the peek
def peek(stack):
    result = stack.get()
    stack.put(result)
    return result


#main_stack: main stack
#min_stack: the additional stack for getting the minimum element
#data_to_add: data to be added to the stack
def add_element(main_stack, min_stack, data_to_add) :
    #Push the node being inserted onto the main stack
    main_stack.put(data_to_add)

    #If the min stack is empty or the data being inserted is <=
    #to the top of the min_stack, then add the data to the min_stack 
    if (min_stack.empty()) :
         min_stack.put(data_to_add)
    else :
        peek_result = peek(min_stack)
        if (data_to_add <= peek_result):
            min_stack.put(data_to_add)
    

#main_stack: main stack
#min_stack: the additional stack for getting the minimum element
#Return value: data at the top of the main stack
def remove_element(main_stack, min_stack) :
    if (main_stack.empty()):
        raise NameError('Stack is empty')

    #Remove the topmost element from the main stack
    popped_element = main_stack.get()

    #Peek at the minimum value, which is stored at the top of the min_stack
    min_val = peek(min_stack)

    #If value popped from the main stack matches the value at the top
    # of min_stack, then remove the topmost element from the min_stack  
    if (popped_element == min_val) :
        min_stack.get()

    return popped_element


#Finds the smallest number in a list upto max_index. We can't use the min 
#function which gives the minimum in the entire list
def find_smallest(number_list, max_index) :
    smallest = 0xFFFFFFF

    for i in range(max_index + 1) :
        if (smallest > number_list[i]) :
            smallest = number_list[i]
        
    return smallest



def test_stack() :

    #Create the main stacks and min_stack in python
    main_stack = queue.LifoQueue()
    min_stack = queue.LifoQueue()

    #Test for different sizes of the stacks
    for num_elems in range(MAX_NUM_STACK_ELEMS + 1) :
        #Generate random values and store in number_list
        number_list = [random.randint(0, MAX_VALUE) for x in range(num_elems)]
        
        for j in range(num_elems) :
            #Add the value to the main_stack and min_stack
            add_element(main_stack, min_stack,  number_list[j])

            #Peek the minimum value from the min_stack
            min_val= peek(min_stack)

            #Verify if the minimum value given by min_stack is correct
            smallest_element = find_smallest(number_list, j)
            if (min_val != smallest_element) :
                handle_error()
            
        

        for j in range(num_elems) :
            #Peek the minimum value from the min_stack
            min_val = peek(min_stack)

            #Verify if the minimum value given by min_stack is correct
            smallest_element = find_smallest(number_list, num_elems - 1 - j)
            if (min_val  != smallest_element) :
                handle_error()
            

            #Remove an element from the stack
            remove_element(main_stack, min_stack)
        

        #Verify that both min_stack and main_stack are empty
        if (not min_stack.empty() or not main_stack.empty()):
            handle_error()

    



if (__name__ == '__main__'):
    test_stack()
    print('Test passed')




