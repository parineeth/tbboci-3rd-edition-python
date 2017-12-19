
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys


MAX_POS = 1000000
NUM_CHARS = 256


class StreamParam(object):
    
    def __init__(self):
        #If we have seen the character 2 or more times in the stream,
        #then is_repeated[character] = True
        self.is_repeated = [False] * NUM_CHARS 
    
        #For every character, we maintain the position of its first
        #occurrence. If the character has not yet occured in stream, 
        #we store -1 
        self.first_pos = [-1] * NUM_CHARS
 
        #the first unique character in the stream
        self.first_unique = '#'

        #the current position in the stream
        self.cur_pos    = 0 








def handle_error() :
    print('Test failed')
    sys.exit(1)




#p: contains the parameters for processing the stream 
#cur_char: indicates the current character in the stream
#Returns: first unique character in the stream if it exists, '#' otherwise
def first_unique_in_stream(p, cur_char) :
    if (p.first_pos[ord(cur_char)] == -1) :
        #We are seeing the character for the first time in the stream. 
        #So update its first position
        p.first_pos[ord(cur_char)] = p.cur_pos

        #If there are no unique characters in the stream, then make 
        #this the first unique character
        if (p.first_unique == '#') :
            p.first_unique = cur_char
        

        p.cur_pos += 1
        return p.first_unique
    

    #We have already seen this character before
    p.is_repeated[ord(cur_char)] = 1

    #If the current character is the first unique character in the stream, 
    #then we need to replace it with next unique character
    if (p.first_unique == cur_char) :

        #Find the first character that occurs only once in stream
        smallest_pos = MAX_POS
        p.first_unique = '#'
        for  i in range(NUM_CHARS):
            if (p.is_repeated[i] == 0 and p.first_pos[i] != -1
               and p.first_pos[i] < smallest_pos) :
                smallest_pos = p.first_pos[i]
                p.first_unique = chr(i)
            

    p.cur_pos += 1
    return p.first_unique



def test(str1, expected_result) :
    p = StreamParam()

    print(str1, end='')

    print(' => ', end='')

    i = 0
    for  c in str1:
        result = first_unique_in_stream(p, c)

        print(result, end='')

        if (result != expected_result[i]):
            handle_error()
    
        i += 1
    

    print('')




if (__name__ == '__main__'):
    test('a', 'a')
    test('aaabcdeb', 'a##bbbbc')
    print('Test passed')



