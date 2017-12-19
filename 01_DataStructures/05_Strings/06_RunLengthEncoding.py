
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



def handle_error() :
    print('Test failed')
    sys.exit(1)


#Performs run length encoding on a string
#str1: input string (example: 'aaabb')
#Returns: output string (example: 'a3b2')
def run_length_encode(str1) :
    if (not str1):
        return str1

    pos1 = 0
    result = []
    while (pos1 < len(str1)) :
        c = str1[pos1]

        #Count the number of consecutive occurrences of character c
        count = 0
        while (pos1 < len(str1) and c == str1[pos1]) :
            count += 1
            pos1 +=  1
        
        #Store character c and the count in the result
        result.append(str(c))
        result.append(str(count))
    
    #convert list to string
    return ''.join(result)



def test(str1, expected_result) :
    result = run_length_encode(str1)
    
    print(str1 + ' => ' + result)
    
    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    test('', '')
    test('a', 'a1')
    test('abcde', 'a1b1c1d1e1')
    test('aaabcccbba', 'a3b1c3b2a1')
    print('Test passed')



