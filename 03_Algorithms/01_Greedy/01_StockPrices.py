
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 10
MAX_NUM_ELEMENTS = 10
MAX_VALUE = 100


def handle_error() :
    print('Error occured')
    sys.exit(1)




#stock_price: list of stock price values
#Return value: maximum profit possible
def find_max_profit(stock_price) :
    n = len(stock_price)

    max_profit = 0
    if (n <= 1):
        return max_profit

    min_stock_price = stock_price[0]

    for  i in range(1, n):
        cur_profit = stock_price[i] - min_stock_price

        if (cur_profit > max_profit):
            max_profit = cur_profit

        if (stock_price[i] < min_stock_price):
            min_stock_price = stock_price[i]
    
    return max_profit






def find_brute_force_max_profit(stock_price) :
    n = len(stock_price)

    max_profit = 0
    if (n <= 1):
        return max_profit

    for  i in range(n - 1):
        for  j in range(i+1, n ):
            if (stock_price[j] > stock_price[i]) :
                cur_profit = stock_price[j] - stock_price[i]
                if (cur_profit > max_profit):
                    max_profit = cur_profit


    return max_profit




if (__name__ == '__main__'):
    for  test_nr in range(MAX_NUM_TESTS):
        #Randomly pick the number of elements
        num_elements = random.randint(1, MAX_NUM_ELEMENTS)

        #Add random share values to the list
        a = [random.randint(0, MAX_VALUE) for  i in range(num_elements)]

        print('Input : ', end='')
        print(a)

        #Find the best profit possible
        result = find_max_profit(a)

        print('Maximum profit = {}'.format(result) )

        #Find the best profit using the brute force approach
        brute_force_result = find_brute_force_max_profit(a)

        #Both results should match
        if (result != brute_force_result):
            handle_error()

        print('__________________________________________________')




    print('Test passed')








