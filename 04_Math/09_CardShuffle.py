
#Copyright (C) 2017 Interview Druid, Parineeth M. R.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from __future__ import print_function
import sys
import random



def handle_error()  :
    print('Test failed')
    sys.exit(1)





#Performs a perfect shuffle of cards
def card_shuffle(cards) :
    for  i in range(len(cards) - 1, -1,-1):
        #Pick a random position from 0 to i
        rand_num = random.randint(0, i)

        #Swap the card at the random position with the card at i
        cards[i], cards[rand_num] = cards[rand_num], cards[i]  


#Performs a shuffle of cards
def incorrect_shuffle(cards) :
    for  i in range(len(cards) - 1, -1,-1):
        rand_num = random.randint(0, len(cards) - 1)

        #Swap the card at the random position with the card at i
        cards[i], cards[rand_num] = cards[rand_num], cards[i]



if (__name__ == '__main__'):
    cards = [i for i in range(0, 52)]

    card_shuffle(cards)

    print('Test passed ')





