
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Error occured ')
    sys.exit(1)






#house_value: value that the thief can steal from each house
#Return value: maximum loot value that the thief can steal from all the houses
def find_max_loot(house_value) :
    n = len(house_value)

    if (n == 0):
        return 0

    if (n == 1):
        return house_value[0]

    if (n == 2):
        return max(house_value[0], house_value[1])

    #val1 has the max loot till the previous house,
    #val2 has the max loot till the second previous house
    val1 = max(house_value[0], house_value[1])
    val2 = house_value[0]

    cur_val = 0
    for  i in range(2, n):
        #cur_val stores the maximum loot till the current house (ith house)
        cur_val = max(val2 + house_value[i], val1)

        #val2 now takes the value of val1 and val1 takes the current value
        val2 = val1
        val1 = cur_val
    
    return cur_val







def test01() :
    house_value = [6, 1, 2, 7]

    print('House values : ', end='')
    print(house_value)

    max_loot = find_max_loot(house_value)

    print('Max loot = {}'.format(max_loot) )

    if (max_loot != 13):
        handle_error()

    print('__________________________________')




def test02() :
    house_value = [6]

    print('House values : ', end='')
    print(house_value)

    max_loot = find_max_loot(house_value)

    print('Max loot = {}'.format(max_loot) )

    if (max_loot != 6):
        handle_error()

    print('__________________________________')



def test03() :
    house_value = [6, 4]

    print('House values : ', end='')
    print(house_value)

    max_loot = find_max_loot(house_value)

    print('Max loot = {}'.format(max_loot) )

    if (max_loot != 6):
        handle_error()

    print('__________________________________')



def test04() :
    house_value = [6, 8]

    print('House values : ', end='')
    print(house_value)

    max_loot = find_max_loot(house_value)

    print('Max loot =  {}'.format(max_loot) )

    if (max_loot != 8):
        handle_error()

    print('__________________________________')



def test05() :
    house_value = [1, 6, 2, 8, 3]

    print('House values : ', end='')
    print(house_value)

    max_loot = find_max_loot(house_value)

    print('Max loot = {}'.format(max_loot) )

    if (max_loot != 14):
        handle_error()

    print('__________________________________')




if (__name__ == '__main__'):
    test01()
    test02()
    test03()
    test04()
    test05()

    print('Test passed ')




