
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




def rand7() :
    result = random.randint(1, 7)
    return result



def rand5() :
    while(True) :
        result = rand7()
        if (result <= 5):
            break

    return result



if (__name__ == '__main__'):
    for  i in range(100):
        result = rand5()
        print('Random value is {}'.format(result) )
        if (result < 1 or result > 5):
            handle_error()


    print('Test passed')






