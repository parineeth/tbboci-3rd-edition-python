
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys


#Helper function for printing a subset
#input_list: list containing the input elements 
#selection: if bit i is 1 in selection, then element i is present in subset
def printSubset(input_list, selection): 
    print('{', end='')

    for i, cur_value in enumerate(input_list):
        if (selection & (1 << i)): 
            print('{} '.format(cur_value) , end='')

    print('}')  


#Main function for generating the subsets
#input_list: list containing the input elements
def generateSubsets(input_list): 
    num_subsets = 1 << len(input_list)

    for i in range(num_subsets): 
        printSubset(input_list, i)



def test(input_list):
    generateSubsets(input_list)

    print('______________________________\n')





def print_subset_r( input_list, is_selected) :
    print('{', end='')

    for i, cur_value in enumerate(input_list):
        if (is_selected[i]) :
            print('{} '.format(cur_value) , end='')
        
     
    print('}')



#input_list: list containing the elements for which we have to find the power set 
#is_selected:  list used for computation. If is_selected[i] = True, then
#the ith element of the list is present in the current subset
#pos:  current position in the  input_list which is being processed
def generate_subsets_r( input_list, is_selected, pos) :
    #Recursion termination condition
    if (pos >= len(input_list)) :
        print_subset_r( input_list, is_selected)
        return 
    

    is_selected[pos] = False
    generate_subsets_r(input_list, is_selected, pos+1)

    is_selected[pos] = True
    generate_subsets_r(input_list, is_selected, pos+1)









def test_r( input_list) :
    is_selected = [False] * len(input_list)

    generate_subsets_r( input_list, is_selected, 0)

    print('______________________________\n')



if (__name__ == '__main__'):
    list1 = []
    list2 = [0]
    list3 = [0, 1, 2]

    test(list1)
    test(list2)
    test(list3)

    print('Test passed')





