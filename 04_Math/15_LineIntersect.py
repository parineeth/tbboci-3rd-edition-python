
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




def handle_error() :
    print('Test failed')
    sys.exit(1)




#slope1: slope of the first line
#c1: y-intercept of the first line
#slope2: slope of the second line
#c2: y-intercept of the second line
#Return value: True if the lines intersect, False otherwise
def do_lines_intersect(slope1, c1, slope2, c2) :
    epsilon = 0.0001
    intersect = False

    if (abs(slope1 - slope2) < epsilon)  :
        #Both lines have the same slope. Check the y-intercept
        if (abs(c1 - c2) < epsilon) :
            #The y-intercepts are the same. 
            #So both lines are the same lines.
            #We consider such lines to intersect with each other
            intersect = True        
        else :
            #The lines are parallel and not coincident on each other
            #So these lines will not intersect
            intersect = False
        
    else :
        #The two lines have different slopes. They will intersect
        intersect = True

    return intersect



def test(slope1, c1, slope2, c2, expected_result) :

    result = do_lines_intersect(slope1, c1, slope2, c2)

    print('Lines (slope = {}, y-intercept = {})  and (slope = {}, y-intercept = {} '.format(slope1, c1, slope2, c2) , end='')

    if (result):
        print('intersect')
    else:
        print('do NOT intersect')

    if (result != expected_result):
        handle_error()  




if (__name__ == '__main__'):
    #Same slope, different y-intercept. Should NOT intersect    
    slope1 = 1.0
    slope2 = 1.0
    c1 = 1.0
    c2 = 2.0
    expected_result = False
    test(slope1, c1, slope2, c2, expected_result)


    #Same y-intercept, different slope. Should intersect    
    slope1 = 2.0
    slope2 = 1.0
    c1 = 1.0
    c2 = 1.0
    expected_result = True
    test(slope1, c1, slope2, c2, expected_result)


    #Different y-intercept, different slope. Should intersect   
    slope1 = 1.0
    slope2 = 2.0
    c1 = 3.0
    c2 = 4.0
    expected_result = True
    test(slope1, c1, slope2, c2, expected_result)


    #Same y-intercept, same slope. Identical lines, should intersect    
    slope1 = 1.0
    slope2 = 1.0
    c1 = 1.0
    c2 = 1.0
    expected_result = True
    test(slope1, c1, slope2, c2, expected_result)

    print('Test passed')








