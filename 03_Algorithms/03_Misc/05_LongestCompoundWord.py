
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys






def handle_error() :
    print(  'Error occured ')
    sys.exit(1)





#str1: string that we need to check if it can be broken
#dictionary: permitted words are stored in the dictionary 
#Return value: True if we can break str1 into words in the dictionary
def word_break(str1, dictionary) :
    length = len(str1)

    if (length == 0):
        return False

    #if we can break the string from 0 to pos, then is_break_possible[pos] 
    #will be True
    is_break_possible = [False] * length

    #if the substring from position i to position j of the original string
    #is a word in dictionary, then word_start[j] will be i
    word_start = [-1] * length

    for  i in range(length):
        #Check if the substring from 0 to i is in the dictionary
        temp_str = str1[0:i+1]
        if (not is_break_possible[i] and temp_str in dictionary) :
            is_break_possible[i] = True
            word_start[i] = 0
        

        #If we can break the substring upto i into dictionary words, 
        #then check if all substrings starting from i+1 can be broken 
        #into dictionary words 
        if (is_break_possible[i]) :
            for  j in range(i + 1, length):
                temp_str = str1[i+1:j+1]
                if (not is_break_possible[j] 
                and temp_str in dictionary) :
                    #We can form a word from i+1 to j
                    is_break_possible[j] = True
                    word_start[j] = i+1
                

    #If is_break_possible[length-1] is True, then entire string can be
    #broken into dictionary words. If the word_start[length-1] is 0, then  
    #it means the entire input word is present in the dictionary. But we
    #want a compound word that has 2 or more dictionary words in it.
    #So modify the result condition to check word_start[length-1] != 0
    if (is_break_possible[length-1] and word_start[length-1] != 0): 
        return True

    return False



#words: the input list of words
#Return value:  the longest compound word if it exists, None otherwise
def find_longest_compound_word(words) :
    dictionary = {}

    #Create the dictionary from the input list of words
    for cur_word in words :
        dictionary[cur_word] = 1
    
    #Sort the words so that the longest word appears first
    words.sort(key = lambda x: -1 * len(x))

    #Starting from the longest word, check if the word can be broken into 
    #two or more words present in the dictionary. If yes, then we have 
    #found the longest compound word
    for cur_word in words :
        if (word_break(cur_word, dictionary)):
            return cur_word
    
    #There is no compound word in the input
    return None



def test01() :
    words = ['hello', 'lumber', 'hellolumberjack', 'hellojack', 'jack']

    print(words)

    longest = find_longest_compound_word(words)

    if (longest):
        print(  'Longest compound word = ' + longest)

    if (longest != 'hellolumberjack') :
        handle_error()
    
    print(  '________________________________________')



def test02() :
    words = ['hello', 'jack', 'lumber']

    print(words)

    longest = find_longest_compound_word(words)

    if (longest):
        print(  'Longest compound word = ' + longest)
    else:
        print(  'No compound word possible ')

    if (longest) :
        handle_error()
    


    print(  '________________________________________')



if (__name__ == '__main__'):
    test01()
    test02()

    print(  'Test passed ')



