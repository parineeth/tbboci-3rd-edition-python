
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


class QueueUsingStacks(object):
    def __init__(self):
        #Create the internal stacks
        self.s1 = queue.LifoQueue()
        self.s2 = queue.LifoQueue()

    def add(self, new_element): 
        #Add elements only to stack s1
        self.s1.put(new_element)
    
    def remove(self): 
        if(self.s2.empty()) :
            #We remove elements only from stack s2. So
            #if s2 is empty, then pop all the elements from s1 and  
            #push them into s2.
            while(not self.s1.empty()) :
                e = self.s1.get()
                self.s2.put(e)
            
        #If s2 is not empty, then remove the element from top of s2.
        #This element corresponds to the head of the queue
        e = None
        if(not self.s2.empty()):
            e = self.s2.get()

        return e
    
    def empty(self): 
        #Queue is empty only if both stacks are empty
        if (self.s1.empty() and self.s2.empty()):
            return True
        return False
    
    






MAX_NUM_QUEUE_ELEMS = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)


def test() :
    q = QueueUsingStacks()


    #Test for different number of elements in the queue
    for  num_elems in range(MAX_NUM_QUEUE_ELEMS+1):

        #Add all the elements to the queue
        for  j in range(num_elems):
            q.add(j)
        

        print('Queue size = {}, Elements are : '.format(num_elems) , end='')

        #Remove one element at a time from the queue and print it
        for  j in range(num_elems):
            output = q.remove()

            expected_val = j
            if (output != expected_val) :
                handle_error()
            
            print('{} '.format(output) , end='')
        

        output = q.remove()
        if (output):
            handle_error()


        print('')
        print('__________________________________________') 
        
    

if (__name__ == '__main__'):
    test()
    print('Test passed ')














