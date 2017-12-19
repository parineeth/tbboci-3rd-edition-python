
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys



class Box(object):

    def __init__(self, x=0, y=0, z=0): 
        self.height = x
        self.length = y
        self.breadth = z
    





def handle_error() :
    print('Test failed ')
    sys.exit(1)



#a: list of boxes of different dimensions. Should contain at least one box
#Result: maximum height of the stack of boxes that can be constructed.
#Assumption is that multiple instances of each box are available
def max_stack_height(a) :
    num_input_boxes = len(a)
    boxes = [] 

    #For each box, all 3 orientations are possible. Length will always be
    #greater than breadth 
    for  cur_box in a:
        new_box = Box()
        new_box.height = cur_box.height
        new_box.length = max(cur_box.length, cur_box.breadth)
        new_box.breadth = min(cur_box.length, cur_box.breadth)
        boxes.append(new_box)
    
        new_box = Box()
        new_box.height  = cur_box.length
        new_box.length  = max(cur_box.breadth, cur_box.height)
        new_box.breadth = min(cur_box.breadth, cur_box.height)
        boxes.append(new_box)

        new_box = Box()
        new_box.height  = cur_box.breadth
        new_box.length  = max(cur_box.length, cur_box.height)
        new_box.breadth = min(cur_box.length, cur_box.height)
        boxes.append(new_box)
    
    num_boxes = 3 * num_input_boxes

    #Sort the boxes so that the boxes with larger base area appear first
    boxes.sort(key = lambda x: -1 * x.length * x.breadth)

    best_height = []
    for  cur_box in boxes:
        best_height.append(cur_box.height)
    
    for  i in range(1, num_boxes):
        for  j in range(i):
            #We can place box i on box j, only if base of box i 
            #is smaller than the base of box j
            if (boxes[i].length < boxes[j].length 
            and boxes[i].breadth < boxes[j].breadth): 
                if (best_height[i] < 
                best_height[j] + boxes[i].height) :
                    best_height[i] = (best_height[j] + 
                                boxes[i].height)
                
    #Find the stack with the maximum height
    result = max(best_height)

    return result



def test() :
    a =  [Box(100, 120, 320), Box(10, 20, 30), Box(40, 60, 70), Box(40, 50, 60)] 

    result = max_stack_height(a)

    print('Max stack height = {}'.format(result) )

    if (result != 600):
        handle_error()




if (__name__ == '__main__'):
    test()
    print('Test passed ')



