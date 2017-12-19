
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys




class Activity(object):

    def __init__(self,  input_id, start_time, end_time):
        self.id = input_id
        self.start_time = start_time
        self.end_time = end_time
    


def handle_error() :
    print('Error occured ')
    sys.exit(1)




#a: list of activities, where each activity has a start time and end time
#Return value: list having the index of the selected activities 
def activity_selection(a) :
    #Sort the activities in non-decreasing order of their end time
    a.sort(key = lambda x: x.end_time)

    selected = [] 

    #Keep a track of the current time as we process the activities
    cur_time = 0

    for  i, cur_activity in enumerate(a):
        #Pick the activity whose start time is on or after current time
        if (cur_activity.start_time >= cur_time) :
            selected.append(i)

            #Update the current time to the end time of the activity
            cur_time = cur_activity.end_time

    return selected





def test01() :
    a = []

    obj = Activity(1000, 0, 5)
    a.append(obj)

    obj = Activity(1001, 1, 2)
    a.append(obj)

    obj = Activity(1002, 3, 6)
    a.append(obj)

    selected = activity_selection(a)

    for  index in selected:
        print('Perform Activity : {}, Start time = {}, End time = {} '.format(a[index].id,
                a[index].start_time, a[index].end_time) )
    

    expected_result = 2

    if (len(selected) != expected_result):
        handle_error()

    print('__________________________________')




def test02() :
    a = []

    obj = Activity(1000, 0, 1)
    a.append(obj)

    obj = Activity(1002, 1, 5)
    a.append(obj)

    obj = Activity(1001, 2, 3)
    a.append(obj)

    obj = Activity(1003, 4, 7)
    a.append(obj)

    selected = activity_selection(a)

    for index in selected:
        print('Perform Activity : {}, Start time = {}, End time = {} '.format(a[index].id,
                a[index].start_time, a[index].end_time) )


    expected_result = 3

    if (len(selected) != expected_result):
        handle_error()

    print('__________________________________')




if (__name__ == '__main__'):
    test01()
    test02()

    print('Test passed')



