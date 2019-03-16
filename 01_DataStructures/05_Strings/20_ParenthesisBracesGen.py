
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
def verify(buf) :
    s = queue.LifoQueue() #create a stack
    
    for c in buf :
        if (c == '{' or c == '[' or c == '(') :
            #If we get an opening brace, bracket or parenthesis, 
            #then push it on to the stack
            s.put(c)
        elif (c == '}' or c == ']' or c == ')'):
            #If we get a closing brace, bracket or parenthesis, 
            #then the character on top of stack should be the corresponding opening
            #character
            if (s.empty()):
                handle_error()

            top_char = peek(s)
            if (c == '{' and top_char != '}'):
                handle_error()
            elif (c == ']' and top_char != '['):
                handle_error()
            elif (c == ')' and top_char != '('):
                handle_error()

            #Since we have matched the opening and closing character,
            #remove the opening character from the stack
            s.get()
        else :
            #We found a character other than a brace, bracket or parenthesis
            handle_error()
        

    #At the end of processing the stack, the stack should be empty
    if (not s.empty()):
        handle_error()



def print_output(buf) :
    for c in buf: 
        print(c, end='')

    print('')
    verify(buf)

#Helper function for finding the nearest unmatched opening character
#buf: list containing braces, brackets and parenthesis
#pos: we will search for unmatched character from pos - 1 to 0
#Return value: index of the first unmatched character when traversing from
#   pos - 1 to 0 if it exists, -1 otherwise 
def find_unmatched(buf, pos) :
    back_pos = pos - 1
    n_braces = n_brackets = n_parenthesis = 0

    #When we get a closing character, decrement the count by 1,
    #when we get an opening character, increment the count by 1
    while (back_pos >= 0) :
        if (buf[back_pos] == '{') :
            n_braces += 1
        elif (buf[back_pos] == '['):
            n_brackets += 1
        elif (buf[back_pos] == '('):
            n_parenthesis += 1
        elif (buf[back_pos] == '}'):
            n_braces -= 1
        elif (buf[back_pos] == ']'):
            n_brackets -= 1
        elif (buf[back_pos] == ')'):
            n_parenthesis -= 1

        #If we encounter more opening characters than closing
        #characters as we traverse backwards, then we have found
        #the location of the mismatch
        if (n_braces > 0 or n_brackets > 0 or n_parenthesis > 0):
            return back_pos

        back_pos -= 1
    
    return -1

#Main function for printing the braces, brackets and parenthesis
#buf: list used to store braces, brackets and parenthesis
#pos: next free position in buf
#n_max: maximum number of opening characters (equal to max closing characters)
#n_open: number of opening characters currently in buf
#n_close: number of closing characters currently in buf
def print_nesting(buf, pos, n_max, n_open, n_close):
    #Condition for terminating the recursion
    if (n_close == n_max) :
        print_output(buf)
        return

    if (n_open < n_max) :
        #Add an opening brace and call print_nesting recursively
        buf[pos] = '{'
        print_nesting(buf, pos+1, n_max, n_open + 1, n_close)

        #Add an opening bracket and call print_nesting recursively
        buf[pos] = '['
        print_nesting(buf, pos+1, n_max, n_open + 1, n_close)

        #Add an opening parenthesis and call print_nesting recursively
        buf[pos] = '('
        print_nesting(buf, pos+1, n_max, n_open + 1, n_close) 

    unmatched_pos = find_unmatched(buf, pos)
    if (n_open > n_close and unmatched_pos >= 0) :
        #to balance the characters, add closing character corresponding
        #to the unmatched character and call print_nesting recursively
        unmatched_char = buf[unmatched_pos]
        if (unmatched_char == '{') :
            buf[pos] = '}'
            print_nesting(buf, pos+1, n_max, n_open, n_close + 1)
        elif (unmatched_char == '['):
            buf[pos] = ']'
            print_nesting(buf, pos+1, n_max, n_open, n_close + 1)
        elif (unmatched_char == '('):
            buf[pos] = ')'
            print_nesting(buf, pos+1, n_max, n_open, n_close + 1)
        


def test01() :
    for  i in range(1, 5):
        buf = ['a'] * (2*i) #one opening and one closing character. So multiply i by 2
        print_nesting(buf,  0, i, 0, 0) 
        print('______________________________________')

    

if (__name__ == '__main__'):
    test01()
    print('Test passed')






