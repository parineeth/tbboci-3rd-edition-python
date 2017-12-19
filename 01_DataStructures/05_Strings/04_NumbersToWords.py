
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




#Helper function to print number from 1 to 999
#number: number from 1 to 999
def print_3_digits(number) :
    #basic_lookup[0] is empty. We want basic_lookup[1] to map to 'One'
    #and so on. 
    basic_lookup = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 
            'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
            'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 
            'Seventeen', 'Eighteen', 'Nineteen']

    #tens_lookup[0] and tens_lookup[1] are empty.
    #We want tens_lookup[2] to map to 'Twenty' and so on. 
    tens_lookup = ['', '','Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety']

    #Suppose number is 987, then hundreds_digit is 9
    hundreds_digit = number // 100
    if (hundreds_digit > 0) :
        print(basic_lookup[hundreds_digit] + ' Hundred ', end='')
    

    #Suppose number is 987, then remainder will be 87
    remainder = number % 100
    if (remainder > 0) :
        if (remainder <= 19) :
            print(basic_lookup[remainder] + ' ', end='')
        else :
            tens_digit = remainder // 10
            unit_digit = remainder % 10
            print(tens_lookup[tens_digit] + ' ', end='')
            print(basic_lookup[unit_digit] + ' ', end='')
        
    




#Main function to print the number in words
#number: any number from 0 to 999999999
def print_num_in_words(number) :
    #If number is 0, handle it here and return
    if (number == 0) :
        print('Zero ')
        return
    
    #Suppose number is 123456789, then millions = 123, remainder = 456789
    millions = number // 1000000
    remainder = number - (millions * 1000000)

    #Suppose remainder = 456789, then thousands = 456, remainder = 789
    thousands = remainder // 1000
    remainder = remainder - (thousands * 1000)

    if (millions > 0) :
        print_3_digits(millions)
        print('Million ', end='')
    
    if (thousands > 0) :
        print_3_digits(thousands)
        print('Thousand ', end='')
    
    if (remainder > 0) :
        print_3_digits(remainder)
     
    print('')



def test(x) :
    print('{} in words = '.format(x) , end='')
    print_num_in_words(x)




if (__name__ == '__main__'):
    test(0)
    test(8)
    test(15)
    test(75)
    test(100)
    test(512)
    test(987)
    test(1001)
    test(450012)
    test(816280)
    test(1000001)
    test(10011284)
    test(90145012)
    test(987654321)

    print('Test passed')



