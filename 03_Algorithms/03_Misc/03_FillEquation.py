
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Test failed ')
    sys.exit(1)


#Helper function that evaluates the numbers and operators
#a: list of numbers. Should have at least one element
#operators: list of operators (+, -) to be applied on numbers
def evaluate(a, operators) :
    result = a[0]
    for  i in range(1, len(a)):
        if (operators[i-1] == '+'):
            result += a[i]
        else:
            result -= a[i]
    
    return result


#a: list of numbers. Should have at least one element
#rhs: right hand side of the equation
#operators: list for storing the operators to be applied on the numbers
#num_operators: number of operators that have been filled in so far
#Return value: True if we can get the rhs by placing operators between numbers
def fill_operators(a, rhs, operators, num_operators) :
    if (num_operators == len(a) - 1) :
        #We have filled in all the operators. So evaluate the result and
        #terminate the recursion
        result = evaluate(a, operators)
        if (result == rhs) :
            return True
        else:
            return False
    
    #Fill in + as the next operator and try out
    operators[num_operators] = '+'
    is_possible = fill_operators(a, rhs, operators, num_operators + 1)
    if (is_possible):
        return True

    #Fill in - as the next operator and try out
    operators[num_operators] = '-'
    is_possible = fill_operators(a, rhs, operators, num_operators + 1)

    return is_possible




def test() :
    n = 3
    a = [10, 20, 30]
    operators = ['+'] * n
    rhs = -40

    is_possible = fill_operators(a, rhs, operators, 0)

    #We should be able to get -40 since 10 - 20 - 30 = -40 
    if (not is_possible):
        handle_error()

    print('{} '.format(a[0]) , end='')
    for  i in range(1, n):
        print('{} '.format(operators[i-1]) , end='')
        print('{} '.format(a[i]) , end='')
    
    print(' = {}'.format(rhs) )




if (__name__ == '__main__'):
    test()
    print('Test passed')



