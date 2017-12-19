
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
    print(  'Test failed')
    sys.exit(1)


#There is no peek functionality in python stack. So we are doing a get
#followed by an immediate put to mimic the peek
def peek(stack):
    result = stack.get()
    stack.put(result)
    return result


#Helper function that picks the operator from the top of operator stack
#and applies them on the two values at the top of the num_stack. The result
#will then be pushed back onto the num_stack
def compute(num_stack, operator_stack) :
    c = operator_stack.get()

    #Since stack is LIFO we will first pop value2 and then pop value1 
    value2 = num_stack.get()
    value1 = num_stack.get()

    if (c == '+') :
        num_stack.put(value1 + value2)
    elif (c == '-'):
        num_stack.put(value1 - value2)
    elif (c == '*'):
        num_stack.put(value1 * value2)
    elif (c == '/'):
        num_stack.put(value1 // value2)



#Helper function to check priority of operators
#stack_operator: operator that is at the top of the operator stack
#exp_operator: operator that is currently being examined in the expression
#Return value: True if operator in the stack is higher priority than operator
#being examined in the expression
def is_higher_precedence(stack_operator, exp_operator) :
    if ((stack_operator == '*' or stack_operator == '/') and 
        (exp_operator == '+' or exp_operator == '-')) :
        return True

    return False

#Main function for evaluating the expression
#expression: string containing the expression to be evaluated
#Return value: the integer result value obtained by evaluating the expression
def evaluate_expression(expr) :
    num_stack = queue.LifoQueue()
    operator_stack = queue.LifoQueue()

    i = 0
    while (i < len(expr)) :
        #Skip the white space characters
        if (expr[i] == ' ' or expr[i] == '\t' or expr[i] == '\n') :
            i += 1
            continue
         
        #If we encounter an integer, then parse out the digits in it    
        if (expr[i] >= '0' and expr[i] <= '9') :
            start_pos = i
            while (i < len(expr) and expr[i] >= '0' and expr[i] <= '9') :
                i += 1
            
            cur_value = int(expr[start_pos:i])
            num_stack.put(cur_value)

        elif (expr[i] == '(') :
            operator_stack.put(expr[i])
            i += 1

        elif (expr[i] == ')'):
            #Till we encounter '(', process the two stacks
            while (peek(operator_stack) != '(') :
                compute(num_stack, operator_stack)
            operator_stack.get() #pop out '(' 
            i += 1
        
        elif (expr[i] == '+' or expr[i] == '-' or
            expr[i] == '*' or expr[i] == '/'): 
            #As long as the operator in the stack is of higher 
            #priority than the operator in the expression, keep processing 
            #the two stacks 
            while (not operator_stack.empty() and 
                is_higher_precedence(peek(operator_stack), expr[i])): 
                compute(num_stack, operator_stack)
            
            operator_stack.put(expr[i])
            i += 1
    
    #If there are still operators in the operator stack, then process them
    while ( not operator_stack.empty()):
        compute(num_stack, operator_stack)

    #The result will be present at the top of the num_stack
    return num_stack.get()



def test(expression, expected_result) :
    result = evaluate_expression(expression)

    print('{} = {}'.format(expression, result) )

    if (result != expected_result):
        handle_error()



if (__name__ == '__main__'):
    test('20 * 40', 800)

    test('10 + 10 * 40', 410)

    test('(200 - (100 + 50)) * 30 / 10', 150) 

    print('Test passed ')



