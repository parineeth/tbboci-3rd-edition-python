
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Test failed')
    sys.exit(1)



#Helper function which reverses a list between indexes low and high
#list1: list which needs to be reversed
#low: lower index of region to be reversed
#high: higher index of region to be reversed
def reverse_list(list1, low, high) :
    while (low < high) :
        list1[low], list1[high] = list1[high], list1[low]
        low += 1
        high -= 1
    



#Main function to reverse the words in a string
#str1: the string in which the words have to be reversed
#Returns: string in which the words have been reversed
def reverse_words(str1) :
    #convert input string to a list 
    result = list(str1)

    #if length is < 2 then convert the result list to string and return 
    if (len(str1) < 2):
        return ''.join(result)

    #Reverse the entire list
    result = result[::-1]

    #Reverse the individual words 
    pos = 0
    while (pos < len(result)) :
        if (result[pos].isalpha()) :
            low = pos
            while (pos < len(result) and result[pos].isalpha()) :
                pos += 1
            
            high = pos - 1
            reverse_list(result, low, high)
        else :
            pos += 1
            
    
    #convert list to string
    return ''.join(result)



def test(str1, expected_result) :
    print(str1, end='')

    result = reverse_words(str1)

    print(' =>  ' + result)

    if (result != expected_result):
        handle_error()





if (__name__ == '__main__'):
    test('', '')
    test('a', 'a')
    test('Hello how are you', 'you are how Hello')

    print('Test passed')



