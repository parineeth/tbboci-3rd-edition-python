
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys


#Helper function to print the combination
#a: input list
#is_selected: if is_selected[i] is True, then ith element in input is selected
#subset_size: Total number of elements to be selected 
def print_combination(a, is_selected, subset_size) :
    print('{', end='')

    num_printed = 0
    for i, cur_value in enumerate(a):
        if (is_selected[i]) :
            print('{} '.format(cur_value) , end='')
            num_printed += 1
            if (num_printed >= subset_size):
                break

    print('}')



#a: input list containing the elements  
#is_selected: if is_selected[i] = True, then the ith element 
#   of the input_list is present in the current subset
#pos: current position in the input 
#subset_size: total number elements that should be present in the final subset
#cur_num_selections: currently how many elements have been selected
def generate_combinations(a, is_selected, pos, subset_size, cur_num_selections):
    if (cur_num_selections == subset_size) :
        print_combination(a, is_selected, subset_size)
        return #Terminate the recursion
    

    if (pos >= len(a)) :
        return #Terminate the recursion
    

    #Exclude the item from the subset
    is_selected[pos] = False

    generate_combinations(a, is_selected, pos+1, subset_size,
                cur_num_selections)

    #Include the item in the subset
    is_selected[pos] = True

    generate_combinations(a, is_selected, pos+1, subset_size,
                cur_num_selections + 1)








def test(a, subset_size) :
    length = len(a)
    is_selected = [False] * length

    print('Number of elements in subset = {}'.format(subset_size) )

    generate_combinations(a, is_selected, 0, subset_size, 0)


    print('______________________________\n')



if (__name__ == '__main__'):
    a = [0, 1, 2, 3, 4]
    length = len(a)

    #Compute 5C0 to 5C5
    for  subset_size in range(length + 1):
        test(a, subset_size)


    print('Test passed')





