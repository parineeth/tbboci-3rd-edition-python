
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys





class Point(object): 

    def __init__(self): 
        self.x = 0
        self.y = 0
    
 



def handle_error() :
    print('Test failed')
    sys.exit(1)




#left1: upper left corner of rectangle 1
#right1: lower right corner of rectangle 1
#left2: upper left corner of rectangle 2
#right2: lower right corner of rectangle 2
#Return value: True if rectangles overlap, False otherwise
def do_rectangles_overlap(left1, right1, left2, right2) :
    #one rectangle lies completely to the right or left of the other
    if (right1.x < left2.x or right2.x < left1.x):
        return False

    #one rectangle lies completely above or below the other
    if (left1.y < right2.y or left2.y < right1.y):
        return False

    #the rectangles overlap
    return True



def test(left1, right1, left2, right2, expected_result) :
    result = do_rectangles_overlap(left1, right1, left2, right2)

    if (result != expected_result):
        handle_error()




if (__name__ == '__main__'):
    left1 = Point()
    right1 = Point()
    left2 = Point()
    right2 = Point()

    left1.x = 0
    left1.y = 20
    right1.x = 20
    right1.y = 0

    left2.x = 10
    left2.y = 30
    right2.x = 30
    right2.y = 10

    test(left1, right1, left2, right2, True)


    left1.x = 0
    left1.y = 10
    right1.x = 10
    right1.y = 0

    left2.x = 100
    left2.y = 10
    right2.x = 110
    right2.y = 0

    test(left1, right1, left2, right2, False)


    print('Test passed')






