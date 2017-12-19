
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Test failed')
    sys.exit(1)




#str1: valid input character string
#Return value: length of longest palindrome
def find_longest_palindrome(str1)  :
    max_pal_len = 0
    for  pos in range(len(str1)):
        #Check for odd length palindromes by comparing the characters
        #to the left of pos with the characters to the right of pos
        left = pos - 1
        right = pos + 1
        cur_pal_len = 1
        while (left >= 0 and right <= len(str1) - 1):
            if (str1[left] != str1[right]):
                break
            cur_pal_len += 2
            left -= 1
            right += 1
        

        if (cur_pal_len > max_pal_len):
            max_pal_len = cur_pal_len


        #Check for even length palindromes. If str1[pos], matches
        #with str1[pos+1], then compare the characters to the left of
        #pos with the characters to the right of pos+1
        if (pos < len(str1) - 1 and str1[pos] == str1[pos + 1]):
            left = pos - 1
            right = pos + 2
            cur_pal_len = 2
            while (left >= 0 and right <= len(str1) - 1):
                if (str1[left] != str1[right]):
                    break
                cur_pal_len += 2
                left -= 1
                right += 1
            

            if (cur_pal_len > max_pal_len):
                max_pal_len = cur_pal_len
        
    
    return max_pal_len




def test01(str1, expected_result) :

    result = find_longest_palindrome(str1)

    print('Length of longest palindrome in {} = {}'.format(str1, result) )

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    test01('RACECAR', 7)
    test01('AABB', 2)
    test01('ABBA', 4)
    test01('ACBBDA', 2)
    test01('ABCDE', 1) #A single character in the string can be treated as a palindrome

    print('Test passed')


