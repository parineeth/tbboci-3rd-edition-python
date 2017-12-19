
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



MAX_NUM_TESTS = 100
MAX_LENGTH = 10
MAX_VALUE     = 9



def handle_error() :
    print('Error occured ')
    sys.exit(1)



#Helper function for printing out the sizes of the individual pieces
def print_pieces(first_cut, total_length) :
    print('The rod piece lengths are : ', end='')

    cur_length = total_length
    while (cur_length > 0 and first_cut[cur_length] > 0) :
        print('{} '.format(first_cut[cur_length]) , end='')
        cur_length = cur_length - first_cut[cur_length]
    

    print('')   


#price: price[i] gives the price of a rod of length i. price[0] is 0
#total_length: the total length of the rod given to us. Should be >= 1
#Return value: the best value that can be fetched from the rod
def cut_rod(price, total_length) :
    #Initialize best_value to 0
    best_value = [0] * (total_length + 1)

    #first_cut[i] will indicate the length of the first piece when we cut  
    #the rod of length i. This is needed to print out where we should cut 
    #so that we get the best value
    first_cut = [0] * (total_length + 1)

    for  cur_length in range(1, total_length+1):
        #We are cutting a rod whose length is cur_length
        #The length of the first piece after the cut can range from 
        #1 to cur_length
        for  i in range(1, cur_length+1):
            if (price[i] + best_value[cur_length - i] > 
                    best_value[cur_length]) :
                best_value[cur_length] = (price[i] + 
                        best_value[cur_length - i])
                first_cut[cur_length] = i
            
    print_pieces(first_cut, total_length)

    return best_value[total_length]




def cut_rod_recursive(price, cur_length) :
    if (cur_length <= 0):
        return 0

    best_value = price[cur_length]
    for  i in range(1, cur_length):
        best_value = max(best_value, price[i] + cut_rod_recursive(price, cur_length - i))
    
    return best_value



def print_rod_info(price) :
    num_elems = len(price)

    print('Length: ', end='')
    for  i in range(num_elems):
        print('{} '.format(i) , end='')
    print('')

    print('Price : ', end='')
    for  cur_price in price:
        print('{} '.format(cur_price) , end='')
    

    print('')



def test() :
    #Randomly choose the length of rod
    length = random.randint(1, MAX_LENGTH)

    #Randomly fill in the prices. We have to fill in the prices from len = 0 to 
    #len = length 
    price = [random.randint(0, MAX_VALUE) for  i in range(length+1) ]

    #Price of rod of length 0 is 0
    price[0] = 0
    

    print_rod_info(price)

    #Find the result using an efficient technique
    result = cut_rod(price, length)

    print('Max value =  {}'.format(result) )


    #Find the result using the recursive technique
    expected_result = cut_rod_recursive(price, length)

    #The two results should match
    if (result != expected_result) :
        handle_error()
    

    print('________________________________________________')




if (__name__ == '__main__'):
    for  i in range(MAX_NUM_TESTS):
        test()


    print('Test passed')





