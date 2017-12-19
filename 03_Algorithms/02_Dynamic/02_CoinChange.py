
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




MAX_INT_VALUE = (0x7FFFFFFF)

def handle_error() :
    print('Error occured ')
    sys.exit(1)






#denom: list having the coin denominations. Should have at least 1 element
#final_amount: amount for which change has to be obtained
#Return value: Minimum number of coins needed to represent final_amount
def find_min_coins(denom, final_amount) :
    #List for storing the minimum number of coins for an amount
    min_num_coins = [0] * (final_amount + 1)

    #List for storing the coin denomination chosen for an amount
    chosen_denom = [0] * (final_amount + 1)
    
    min_num_coins[0] = 0
    for  cur_amt in range(1, final_amount+1):
        min_num_coins[cur_amt] = MAX_INT_VALUE
        for  cur_denom in denom:
            if (cur_denom <= cur_amt) :
    
                smaller_amt = cur_amt - cur_denom

                if (1 + min_num_coins[smaller_amt] < 
                        min_num_coins[cur_amt]) :
                    min_num_coins[cur_amt] = (1 + 
                        min_num_coins[smaller_amt])
                    chosen_denom[cur_amt] = cur_denom
    

    result = min_num_coins[final_amount]
    print('Minimum number of coins = {}'.format(result) )

    #print the chosen denominations to get the amount
    cur_amt = final_amount
    while (cur_amt > 0) :
        print('{} '.format(chosen_denom[cur_amt]) , end='')
        cur_amt = cur_amt - chosen_denom[cur_amt]
    print(' = {}'.format(final_amount) )

    return result




def test01() :
    denom = [1, 2, 3, 4, 5]
    total_amount = 13

    print('Coin denominations : ', end='')
    print(denom)
    print('Total amount needed = {}'.format(total_amount) )

    min_coins = find_min_coins(denom, total_amount)

    if (min_coins != 3):
        handle_error()

    print('_____________________________________________')

    return 0



def test02() :
    denom = [1, 2, 3, 4]
    total_amount = 17

    print('Coin denominations : ', end='')
    print(denom)
    print('Total amount needed = {}'.format(total_amount) )

    min_coins = find_min_coins(denom, total_amount)

    if (min_coins != 5):
        handle_error()

    print('_____________________________________________')

    return 0


def test03() :
    denom = [1, 5, 10, 25, 50]
    total_amount = 30

    print('Coin denominations : ', end='')
    print(denom)
    print('Total amount needed = {}'.format(total_amount) )

    min_coins = find_min_coins(denom, total_amount)

    if (min_coins != 2):
        handle_error()

    print('_____________________________________________')

    return 0



def test04() :
    denom = [1, 3, 4, 5]
    total_amount = 7

    print('Coin denominations : ', end='')
    print(denom)
    print('Total amount needed = {}'.format(total_amount) )

    min_coins = find_min_coins(denom, total_amount)

    if (min_coins != 2):
        handle_error()

    print('_____________________________________________')

    return 0





if (__name__ == '__main__'):
    test01()
    test02()
    test03()
    test04()

    print('Test passed')






