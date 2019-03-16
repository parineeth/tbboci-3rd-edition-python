
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
    print('Test failed')
    sys.exit(1)


def peek(stack):
    return stack.queue[-1]


#Verify if the braces, brackets and parenthesis are properly nested 
#str1: input string containing braces, brackets and parenthesis
#Return value: True if the nesting is proper, False otherwise
def validate_nesting(str1) :
    s = queue.LifoQueue() #create a stack
    
    for c in str1 :
        if (c == '{' or c == '[' or c == '(') :
            #If we get an opening brace, bracket or parenthesis  
            #in string, then push it on to the stack
            s.put(c)
        elif (c == '}' or c == ']' or c == ')'):
            #If we get a closing brace, bracket or parenthesis  
            #in string, then the character on top of stack should be 
            #the corresponding opening character
            if (s.empty()):
                return False

            top_char = peek(s)
            if (c == '{' and top_char != '}'):
                return False
            elif (c == ']' and top_char != '['):
                return False
            elif (c == ')' and top_char != '('):
                return False

            #Since we have matched the opening and closing character,
            #remove the opening character from the stack
            s.get()
        else :
            #We found a character other than a brace, bracket 
            #or parenthesis
            return False
        

    #At the end of processing, the stack should be empty
    if (not s.empty()):
        return False

    return True



def test(str1, expected_result) :
    result = validate_nesting(str1)

    if (result):
        print(str1 + ' => is balanced ')
    else :
        print(str1 + ' => is NOT balanced ')

    if (result != expected_result):
        handle_error()


if (__name__ == '__main__'):
    test('[{()}]', True)
    test('[{]', False)
    print('Test passed')






