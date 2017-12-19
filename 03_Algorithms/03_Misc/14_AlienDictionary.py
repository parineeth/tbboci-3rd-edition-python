
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






MAX_NUM_CHARACTERS = 256


#Helper function for performing topological sorting
#cur_char: current character that we are processing
#adjacency_table: a list of lists. if there is an edge from 'a' to 'b' then 
#adjacency_table['a'] contains list which will store b
#is_visited: indicates if a character has already been visited or not
#s: stack for storing the result of the topological sort
def topological_sort_helper(cur_char, adjacency_table, is_visited, s):
    if (is_visited[ord(cur_char)]):
        return

    #make is_visited to True here so that we don't run into loops
    is_visited[ord(cur_char)] = True

    #Process all the characters that are neighbors of the current  
    #character (ie  adjacent to current character) in the graph
    neighbor_list = adjacency_table[ord(cur_char)]

    for neighbor_char in neighbor_list:
        if (not is_visited[ord(neighbor_char)]):
            topological_sort_helper(neighbor_char, adjacency_table,
                        is_visited, s)

    #Push the current character onto the stack only after all the 
    #characters reachable from it have been recursively added to the stack
    s.put(cur_char)


#Function that performs topological sorting
#adjacency_table:a list of lists. if there is an edge from 'a' to 'b' then 
#adjacency_table['a'] contains list which will store b
def topological_sort(adjacency_table) :
    is_visited = [False] * MAX_NUM_CHARACTERS
    s = queue.LifoQueue()

    #Process all the characters
    for  i, neighbor_list in enumerate(adjacency_table):
        if (len(neighbor_list) ):
            topological_sort_helper(chr(i), adjacency_table, 
                        is_visited, s)
    
    #Pop out the contents of the stack to get the result of topological 
    #sort. This is the order of characters in the alien language
    while (not s.empty()) :
        cur_char = s.get()
        print(cur_char)
    




#Main function to find the order of characters in an alien language
#words: the words present in the dictionary
def get_alphabet_order(words) :
    #adjacency_table is a list of lists
    #For each character in the language we maintain a list
    adjacency_table = [[] for x in range(MAX_NUM_CHARACTERS)]

    num_words = len(words)

    #Go through the consecutive pairs of words in dictionary
    for  i in range(0, num_words - 1):
        word1 = words[i]
        word2 = words[i+1]
    
        for c1, c2 in zip(word1, word2):
            #Find first mismatching characters between the two words
            if (c1 != c2) :
                #In the graph, we have an edge from c1
                #to c2. Fetch the list for c1
                #and store c2 in it, since 
                #c2 is adjacent to c1
                neighbor_list = adjacency_table[ord(c1)]
                neighbor_list.append(c2)
                break
            

    #Perform the topological sort
    topological_sort(adjacency_table)



def test01() :
    words = ['aaa', 'abc', 'acb', 'dad'] #Words in the alien dictionary

    print(  'Dictionary: ', end='')
    print(words)

    print('Order of characters:')

    get_alphabet_order(words)

    print(  '_____________________________')




def test02() :
    words = ['aba', 'abb', 'abd', 'ac', 'ad', 'pq'] #Words in the alien dictionary

    print(  'Dictionary: ', end='')
    print(words)

    print('Order of characters: ')

    get_alphabet_order(words)

    print('_____________________________')




if (__name__ == '__main__'):
    test01()
    test02()

    print(  'Test passed')



