
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random

class CacheNode(object): 


    def __init__(self, key, value): 
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    



class LruCache(object): 

    def __init__ (self, max_size):
        self.max_size = max_size #Max number of nodes that cache can hold
        self.count = 0 #current number of nodes in the cache
        self.ht = {} #dictionary
        self.head = None #Head of the doubly linked list
        self.tail = None #Tail of the doubly linked list


    #self - LRU cache
    #key - key for the node that should be fetched from the cache
    def lru_get(self, key): 
        #Get the node from the key using the dictionary
        cur_node = self.ht.get(key)

        if (not cur_node):
            return None

        #If the node being fetched is at the head of the linked list, 
        #then simply return
        if (self.head == cur_node):
            return cur_node

        #The node being fetched is not at the front. So detach it from 
        #the linked list and add it to the beginning. 
        #If the node was removed from the tail, then update the tail
        if (self.tail == cur_node):
            self.tail = cur_node.prev

        cur_node.prev.next = cur_node.next
        if (cur_node.next):
            cur_node.next.prev = cur_node.prev

        cur_node.prev = None
        cur_node.next = self.head
        self.head.prev = cur_node
        self.head = cur_node

        return cur_node
    


    #self - the LRU cache
    #new_item - new node to be added to the LRU cache
    def lru_add(self, new_item): 
        if (self.count == self.max_size) :
            #The cache is full. So remove the last node from 
            #linked list 
            temp = self.tail

            self.tail = self.tail.prev

            if (not self.tail):
                self.head = None
            else:
                self.tail.next = None

            self.count -= 1

            #Remove the last node from the dictionary
            del self.ht[temp.key]


        #Add the new node to the front of the linked list
        new_item.prev = None
        new_item.next = self.head

        if (self.head):
            self.head.prev = new_item

        self.head = new_item

        if (not self.tail):
            self.tail = new_item

        self.count += 1

        #Add the new node to the dictionary
        self.ht[new_item.key] = new_item













MAX_NUM_TESTS = 50
MAX_CACHE_SIZE = 20


def handle_error() :
    print('Test Failed')
    sys.exit(1)



def lru_verify(cache) :

    #If there are no items in the cache, then head and tail should be None
    if (cache.count == 0) :
        if (cache.head or cache.tail):
            handle_error()
        return 0
    

    #head.prev should be None
    if (cache.head.prev):
        handle_error()

    #tail.next should be None
    if (cache.tail.next):
        handle_error()

    #If there is only 1 item in the cache, then head and tail should be identical
    if (cache.count == 1) :
        if (cache.head != cache.tail):
            handle_error()

        return 0
    

    #Count the number of nodes in cache from the head and verify if it matches cache.count
    cur_node = cache.head
    count = 0
    while (cur_node) :
        count += 1
        cur_node = cur_node.next
    

    if (count != cache.count):
        handle_error()


    #Count the number of nodes in cache from the tail and verify if it matches cache.count
    cur_node = cache.tail
    count = 0
    while (cur_node) :
        count += 1
        cur_node = cur_node.prev
    

    if (count != cache.count):
        handle_error()

    return 0




def test01(max_size) :
    
    cache = LruCache(max_size)
    key = 0
    value = 100

    for  i in range(MAX_NUM_TESTS):

        #Perform either the add or the get operation based on random number
        rand_num = random.randint(0, 1)

        if (rand_num == 0) :
            #Perform the add operation
            new_node = CacheNode(key, value)
            key += 1
            value += 1
            cache.lru_add(new_node)
        else :
            #Perform the get operation
            search_key = random.randint(0, key + 2)
            cur_node = cache.lru_get(search_key)

            if (cur_node) :
                #Since we just accessed the cur_node in the cache, the head of cache
                #should refer to it
                if (cache.head != cur_node):
                    handle_error()
            else :
                #We didn't find the key in the cache. Verify that the key doesn't
                #exist in the cache
                cur_node = cache.head
                while (cur_node) :
                    if (cur_node.key == search_key):
                        handle_error()
                    cur_node = cur_node.next
                
            

        


        lru_verify(cache)
    



if (__name__ == '__main__'):
    for  max_size in range(1, MAX_CACHE_SIZE + 1):
        test01(max_size)

    print('Test passed ')




