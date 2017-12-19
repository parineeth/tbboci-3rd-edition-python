
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



MAX_STRING_LENGTH = 100

def handle_error() :
    print('Test failed')
    sys.exit(1)

#Helper function for printing the result
def print_result(buf, buf_pos, remainder) :
    result = ''.join(buf[0:buf_pos])
    result = result + remainder
    print(result)


#str1, str2: two valid input strings that have to be interleaved
#buf: list that contains the result of interleaving the two strings
#pos1: current position in string str1
#pos2: current position in string str2
#buf_pos: current position in the buf list
def string_interleave(str1, str2, buf, pos1, pos2, buf_pos):
    #If we have finished processing both strings, print buf and
    #terminate the recursion
    if (pos1 == len(str1) and pos2 == len(str2)) :
        print_result(buf, buf_pos, '')
        return
    
    #If we have finished processing str2, concatenate remaining str1 to buf,
    #print buf and terminate the recursion
    if (pos2 == len(str2)) :
        print_result(buf, buf_pos, str1[pos1:])
        return
    
    #If we have finished processing str1, concatenate remaining str2 to buf,
    #print buf and terminate the recursion
    if (pos1 == len(str1)) :
        print_result(buf, buf_pos, str2[pos2:])
        return
    
    #Include the next character of str1 into buf
    buf[buf_pos] = str1[pos1]
    string_interleave(str1, str2, buf, pos1 + 1, pos2, buf_pos + 1)

    #Include the next character of str2 into buf
    buf[buf_pos] = str2[pos2]
    string_interleave(str1, str2, buf, pos1, pos2 + 1, buf_pos + 1)     




if (__name__ == '__main__'):
    buf = [' '] * MAX_STRING_LENGTH
    string_interleave('abcde', '123', buf, 0, 0, 0)

    print('Test passed')






