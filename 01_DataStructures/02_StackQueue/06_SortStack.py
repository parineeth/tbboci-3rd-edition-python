
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
MAX_VALUE = 20


def handle_error() :
    print('Test failed')
    sys.exit(1)



def peek(stack):
    return stack.queue[-1]



#Input elements are stored in original_stack. At the end of the operation, 
#original_stack will be empty and sorted stack will have elements in sorted 
#order
def stack_sort(original_stack, sorted_stack): 
    while (not original_stack.empty()) :
        e1 = original_stack.get()
        e2 = None
        if(not sorted_stack.empty()):
            e2 = peek(sorted_stack)
        
        #If sorted stack is empty OR e1 is <= top element of  
        #sorted stack, then push e1 onto the sorted stack 
        if (e2 is None or e1 <= e2) :
            sorted_stack.put(e1)
            continue
         
        
        #While e1 > top element of sorted stack, remove the top 
        #element of sorted stack and push it onto the original stack. 
        while (not sorted_stack.empty()) :
            e2 = peek(sorted_stack)
            if (e1 > e2) :
                e2 = sorted_stack.get()
                original_stack.put(e2)
            else :
                break
            

        sorted_stack.put(e1) #Push e1 onto the sorted stack 
    

 




def test_stack() :

    original_stack = queue.LifoQueue()
    sorted_stack = queue.LifoQueue()

    #Test for different sizes of the stack
    for num_elems in range(MAX_NUM_STACK_ELEMS + 1):
        #Generate a random list of numbers
        number_list = [random.randint(0, MAX_VALUE) for x in range(num_elems)]

        for j in range(num_elems):
            #push the value in number_list on to original stack
            original_stack.put(number_list[j])
        

        #Sort the stack. The sorted results will be in sorted_stack
        stack_sort(original_stack, sorted_stack)

        print('Sorted stack contents are : ')

        prev_data = -1
        for j in range(num_elems):
            #Pop an element from the sorted stack
            output = sorted_stack.get()
            print(output)

            #Verify if the data in stack is in ascending order
            if (prev_data > output) :
                handle_error()
            

            prev_data = output
        

        print('\n_________________________________________________')
    



    

if (__name__ == '__main__'):
    test_stack()
    print('Test passed')
    



