
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

#Queue in python 2.7 has been renamed to queue. So handling this so that code
#is portable on all versions of python
try: 
    import queue
except ImportError:
    import Queue as queue


class StackUsingQueues(object):
    def __init__(self):
        #Create the internal queues
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def empty(self): 
        #Stack is empty if q1 is empty
        if (self.q1.empty()):
            return True
        return False
    
    def push(self, new_element): 
        #Add elements only to queue q1
        self.q1.put(new_element)
    
    def pop(self): 
        if (self.q1.empty()):
            return None

        #Remove all elements from q1 and add it to q2 except the last item
        while (self.q1.qsize() > 1): 
            e = self.q1.get()
            self.q2.put(e)
        
        #Remove the last element in q1. It will contain the top of stack
        e = self.q1.get()

        #Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return e #Return the top of the stack
    



MAX_NUM_ELEMS = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)


def test() :
    s = StackUsingQueues()


    #Test for different number of elements in the stack
    for  num_elems in range(MAX_NUM_ELEMS+1):

        #Add all the elements to the stack
        for  j in range(num_elems):
            s.push(j)
        

        print('Stack size = {}, Elements are : '.format(num_elems) )

        #Remove one element at a time from the stack and print it
        for  j in range(num_elems):
            output = s.pop()

            expected_val = num_elems - 1 - j
            if (output != expected_val) :
                handle_error()
            
            print(output)
        

        output = s.pop()
        if (output):
            handle_error()


        print('')
        print('__________________________________________') 
        
    


if (__name__ == '__main__'):
    test()
    print('Test passed ')














