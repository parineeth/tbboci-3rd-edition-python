
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



def handle_error() :
    print('Test failed')
    sys.exit(1)




def rand5() :
    result = random.randint(1, 5)
    return result



def rand7() :
    while(True) :
        result = (rand5() - 1) + (5 * (rand5() - 1))
        if (result <= 20):
            break

    result = 1 + (result % 7)
    return result



if (__name__ == '__main__'):
    for  i in range(100):
        result = rand7()
        print('Random value is {}'.format(result) )
        if (result < 1 or result > 7):
            handle_error()


    print('Test passed')




