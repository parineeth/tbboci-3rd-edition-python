
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys

import random



MAX_NUM_TESTS  = 10
MAX_NUM_DIGITS = 4


def handle_error() :
    print('Error occured ')
    sys.exit(1)


def print_num(a) :
    for  digit in a:
        print(digit, end='')
    



def get_random_num() :
    num_digits = random.randint(1, MAX_NUM_DIGITS)
    result = []     
    for  i in range(num_digits):
        if (i == 0) :
            #Most significant digit should not be 0
            result.append(random.randint(1, 9))
        else:
            result.append(random.randint(0, 9))
    
    return result




def convert_list_to_num(a) :
    num = 0
    for  cur_value in a:
        num = (num * 10) + cur_value

    return num


def print_result(num1, num2,  result, is_negative) :
    print_num(num1)

    print(' - ', end='')

    print_num(num2)

    print (' = ', end='')

    if (is_negative):
        print(' -', end='')

    print_num(result)

    print('')


#Helper function which returns True if num1 is smaller than num2
def is_smaller(num1, num2) :
    if (len(num1) > len(num2)):
        return False

    if (len(num1) < len(num2)):
        return True

    for  digit1, digit2 in zip(num1, num2):
        if (digit1 > digit2):
            return False

        if (digit1 < digit2):
            return True
    

    return False    


#num1 and num2: lists which store the digits of the two numbers. 
#   The two lists store numeric value of the digits and not ascii values
#Returns: 1. result list which contains num1 - num2 
#     2. boolean value which indicates if result is negative
def large_subtract(num1, num2) :
    is_negative = False

    #Store larger number in num1
    #So if num1 is smaller than num2, then swap num1 and num2
    if (is_smaller(num1, num2) ) :
        #Swap num1 and num2
        num1, num2 = num2, num1

        #If num1 was smaller than num2, then result will be negative
        is_negative = True
     

    #initialize result list 
    result = [0] * len(num1)     

    #Perform the subtraction for all the digits in num2
    pos1 = len(num1) - 1
    pos2 = len(num2) - 1
    borrow = 0
    while (pos2 >= 0) :
        difference = num1[pos1] - num2[pos2] - borrow
        if (difference < 0) :
            difference += 10
            borrow = 1
        else :
            borrow = 0
        
        result[pos1] = difference 
        pos1 -= 1
        pos2 -= 1 
    

    #Process any digits leftover in num1
    while (pos1 >= 0) :
        difference = num1[pos1] - borrow
        if (difference < 0) :
            difference += 10
            borrow = 1
        else :
            borrow = 0
        
        result[pos1] = difference 
        pos1 -= 1
    

    return result, is_negative  



if (__name__ == '__main__'):

    for  test_nr in range(MAX_NUM_TESTS):

        #Generate a random set of digits in the list num1
        num1 = get_random_num()

        #Generate a random set of digits in the list num2
        num2 = get_random_num()

        #Perform the subtraction
        result, is_negative = large_subtract(num1, num2)

        print_result(num1, num2, result, is_negative)

        val1 = convert_list_to_num(num1)
        val2 = convert_list_to_num(num2)
    
        val3 = convert_list_to_num(result)
        if (is_negative):
            val3 = val3 * -1

        #Verify the result
        if (val3 != (val1 - val2)):
            handle_error()



    print('Test passed')








