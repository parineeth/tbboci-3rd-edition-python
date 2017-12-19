
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





#Helper function for printing the words corresponding to the telephone number
#digits: list of digits from 0-9
#key_pad: contains the characters corresponding to each digit
#buf: contains the word formed corresponding to the telephone digits
#pos: current position in buf and digits
def keypad_string_gen(digits, keypad, buf, pos) :
    if (pos == len(digits)) :
        #We have processed all the digits. So print the 
        #word and terminate the recursion
        print(buf)
        return
    
    cur_digit = digits[pos]
    key_string = keypad[cur_digit]

    #key_string is the string corresponding to the current digit
    #So if current digit is 2, key_string will be 'ABC'.
    #Cycle through all the characters in the key_string.
    for c in key_string :
        buf[pos] = c
        keypad_string_gen(digits, keypad, buf, pos+1)
    



#Main function for printing the words corresponding to the telephone number
#digits: list of digits from 0-9 in the telephone number
def telephone_digits_to_string(digits) :
    num_digits = len(digits)
    #Create a temporary buffer for storing the words corresponding to 
    #the digits
    buf = ['A'] * num_digits 

    #digit 2 corresponds to ABC, 3 corresponds to DEF and so on
    keypad = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 
        'PQRS', 'TUV', 'WXYZ']
    
    keypad_string_gen(digits, keypad, buf, 0)



if (__name__ == '__main__'):
    digits = [4, 2, 1, 1, 8, 9, 2, 5, 0, 8]
    telephone_digits_to_string(digits)
    print('Test passed')



