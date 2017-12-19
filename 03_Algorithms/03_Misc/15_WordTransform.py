
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
    print(  'Test failed ')
    sys.exit(1)


#begin_word: starting word in the word transformation
#end_word: ending word in the word transformation
#dictionary: contains the permitted words that can be used in the transformation
#Result:  the list that contains the sequence of words if word transformation 
#   is possible, None if word transformation is not possible
def transform_word(begin_word, end_word, dictionary):
    q = queue.Queue()

    visited = set() #Contains the words that have already been visited

    #If we can transform word a to word b, then we store b -> a mapping in
    # the reverse_path. b is the key and a is the value. 
    reverse_path = {}

    q.put(begin_word)
    visited.add(begin_word)
    while (not q.empty()) :
        #Get the word at the beginning of the queue
        cur_word = q.get()

        #If the current word matches the ending word, we have found
        #the word transformation. Store the sequence of transformation 
        #in the result list
        if (cur_word == end_word):
            result = []
            result.insert(0, cur_word) #Add to beginning of list

            #Find the previous word from where we reached the current 
            #word and add the previous word to the result list
            cur_word = reverse_path.get(cur_word)
            while (cur_word) :
                result.insert(0, cur_word) #Add to beginning of list
                cur_word = reverse_path.get(cur_word)
            
            return result
        
        #Look at all possible words that can be generated from the 
        #current word by changing a single character
        for  i in range(len(cur_word)):
            char_list = list(cur_word) 
        
            #Generate new word by changing the character at position i
            for c in range(ord('a'), ord('z') + 1) :
                char_list[i] = chr(c)
                new_word = ''.join(char_list)

                #If the new word is present in dictionary and has
                #not been visited so far, then add it to the queue
                if (new_word in dictionary and 
                 new_word not in visited ): 
                    q.put(new_word)
                    visited.add(new_word)
                    reverse_path[new_word] = cur_word

    return None #transformation is not possible



def test() :
    dictionary = {}
    begin_word = 'bell'
    end_word = 'walk'

    dictionary['tall'] = 1
    dictionary['bell'] = 1
    dictionary['walk'] = 1
    dictionary['ball'] = 1
    dictionary['talk'] = 1

    result = transform_word(begin_word, end_word, dictionary)

    if (not result):
        handle_error()

    #Print out the word transformation
    print(result)




if (__name__ == '__main__'):
    test()
    print(  'Test passed ')



