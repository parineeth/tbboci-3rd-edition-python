
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




class AnagramHelper(object):
    
    def __init__(self, word, index):
        self.word = word
        self.index = index




def handle_error() :
    print('Test failed ')
    sys.exit(1)





#word_list: list of words that should be sorted so that the anagrams occur 
#  together
#num_words: Number of elements in the word_list
def anagram_sort(word_list) :
    num_words = len(word_list)
    helper = []

    for  i, cur_word in enumerate(word_list):
        #Sort the characters of the word 
        sorted_word = ''.join(sorted(cur_word))

        #Copy the original word into the helper
        #Store the original index (i) of the word in the helper
        obj = AnagramHelper(sorted_word, i)

        helper.append(obj) 

        
    #Sort all the words in the helper
    helper.sort(key = lambda x: x.word )

    #We need to move the words in word_list based on the indexes in 
    #the helper. We can't directly move the strings in the word_list.
    #First we will copy the strings into a scratchpad list
    #based on the indexes in the helper and then copy the scratchpad
    #list into the word_list.
    scratchpad = []
    for  i in range(num_words):
        index = helper[i].index
        scratchpad.append(word_list[index])
    
    #copy word by word from scratchpad to word_list since when we 
    #return from the function, the original word_list should be 
    #modified
    for  i, cur_word in enumerate(scratchpad):
        word_list[i] = cur_word
    






def test() :
    num_words = 6
    word_list =  ['rat', 'atm', 'hill', 'art', 'mat', 'tar']
    expected_result = ['atm', 'mat', 'rat', 'art', 'tar', 'hill'] 

    print('Before sorting: ', end='')
    print(word_list)    

    anagram_sort(word_list)

    print('After  sorting: ', end='')
    print(word_list)    

    if (word_list != expected_result) :
            handle_error()
        
    


if (__name__ == '__main__'):
    test()
    print('Test passed')



