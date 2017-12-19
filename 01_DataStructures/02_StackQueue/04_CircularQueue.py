
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys


class CircularQueue(object): 
    def __init__(self) :
        self.head = -1 #index of first element in queue. -1 if queue is empty
        self.tail = -1 #index of last element in queue. -1 if queue is empty
        self.count = 0 #Number of elements currently present in the queue

        self.max_size = 0 #Max number of elements that can be stored in queue
        self.buf = [] #buffer for storing elements

    
    def add(self, new_element): 
        if (self.count == self.max_size) :
            #If the queue is full, then resize the queue
            if (self.max_size == 0):
                new_size = 1
            else:
                new_size = self.max_size * 2

            new_buf = [new_element] * new_size
            old_pos = self.head
            new_pos = 0

            #Copy from the old queue buf to the new buf
            while (new_pos < self.count) :
                new_buf[new_pos] = self.buf[old_pos]
                new_pos += 1
                old_pos = (old_pos + 1) % self.max_size
             

            self.buf = new_buf
            self.head = 0
            self.tail = self.count - 1
            self.max_size = new_size

        #Advance the tail and insert the element at the tail 
        self.tail = (self.tail + 1) % self.max_size
        self.buf[self.tail] = new_element

        if (self.count == 0):
            self.head = self.tail

        self.count += 1
    
        #Return the result code indicating success
        return 0
    

    def remove(self): 
        #Can't remove an item from an empty queue
        if (self.count <= 0):
            return None

        removed_element = self.buf[self.head]

        if (self.head == self.tail) :
            #There was only 1 item in the queue and that item has been 
            #removed. So reinitialize self.head and self.tail to -1
            self.head = -1
            self.tail = -1
        else :
            #Advance the head to the next location
            self.head = (self.head + 1) % self.max_size 
        
        self.count -= 1

        return removed_element
    

    def print_queue(self): 
        print('Queue: ', end='')
        pos = self.head
        for  i in range(self.count):
            print('{} '.format(self.buf[pos]) , end='')
            pos = (pos + 1) % self.max_size
        

        print('\n___________________________________________________\n')
    








MAX_NUM_QUEUE_ELEMS = 10

def handle_error() :
    print('Test failed')
    sys.exit(1)


def test() :

    q = CircularQueue()

    
    #Test for different number of elements in the circular queue
    for  num_elems in range(MAX_NUM_QUEUE_ELEMS+1):

        #Add elements to the queue
        for  i in range(num_elems):
            q.add(i)
            print('Inserting element {}'.format(i) )
            q.print_queue()
        

        #Remove all elements from the queue
        for  i in range(num_elems):
            result = q.remove()

            print('Removing element {} from queue'.format(result) )
            q.print_queue()

            if (result != i) :
                handle_error()
            
        

        #The queue is now empty. So trying to remove an element should return an error
        result = q.remove()
        if (result) :
            handle_error()
        
    

    



if (__name__ == '__main__'):
    test()
    print('Test passed ')




