#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Vashistha                                           #
# Script      : blackjackGame.py                                          #
# Py Versions : 3.5                                                       #
# Required    : random                                                    #
# Execute     : python blackjackGame.py                                   #
#=========================================================================#

import random

## Define Cards
suits = ['Heart','Diamond','Spade','Club']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

## Shuffles the objects in suits and ranks
random.shuffle(suits)
random.shuffle(ranks)

print("Suits: {}\nRanks: {}\n".format(suits,ranks))

class Bank():
    
    initial_bankroll = 0
    total_bet = 0
    cardvalue = 0
    def __init__(self,bankroll=0):
        self.bankroll = bankroll
        self.initial_bankroll = bankroll
    
    def bet(self,betamt=0):
        while True:
            try:
                while True:
                    print("\nBankroll Amount: {}".format(mybank.bankroll))
                    betamt = int(input("Please enter your bet amount from your Bankroll: "))
                    if (betamt < 1) or (betamt > mybank.bankroll):
                        print("\nERROR! Your bet amount should be greater than 0 and shouldn't exceed your Bankroll Amount!\n")
                        continue
                    else:
                        break
            except:
                print("\nInvalid Amount. Please enter only integer values.\n")
                continue
            else:
                print("\nEntered bet amount: {}".format(betamt))
                self.bankroll = self.bankroll - betamt
                self.total_bet = self.initial_bankroll - self.bankroll
                break

        print("Current Bank Roll: {} || Bet Amount: {}\n".format(self.bankroll,self.total_bet))
        
    def hit(self):
        ## Select 2 Random Cards from Deck for Player/Computer and Display 2 Cards.
        pc_suit = random.choice(suits)
        pc_rank = random.choice(ranks)
        print("\nCard from Deck: {} of {}\n".format(pc_rank,pc_suit))

        ## Value of Player's/Computer's New Card.
        self.cardvalue = values[pc_rank]
        print("New Card Value: {}".format(self.cardvalue))
        return self.cardvalue


## Define Bankroll and validate for proper values.
while True:
    try:
        while True:
            bankroll = int(input("Please enter your Bankroll amount: "))
            if bankroll < 1:
                print("\nError! The Bankroll amount should be greater than 0.\n")
                continue
            else:
                break

    except:
        print("\nError. Please enter a valid integer value for Bankroll amount.\n")
        continue
    else:
        print('\nBank Roll Amount Entered: {}\n'.format(bankroll))
        break


## Initialize the Bank class and assign bankroll argument value.
mybank = Bank(bankroll)

## Call bet method in Bank Class and Accept Bet Amount and deduct the same from Bankroll.
mybank.bet()


## Select 2 Random Cards for Computer and display 1 Card.
cc1_suit = random.choice(suits)
cc1_rank = random.choice(ranks)
cc2_suit = random.choice(suits)
cc2_rank = random.choice(ranks)
print("\nCOMPUTER's Selected Cards:\nCard1: {} of {}\nCard2: Face Down!\n".format(cc1_rank,cc1_suit))


## Select 2 Random Cards from Deck for Player and Display 2 Cards.
pc1_suit = random.choice(suits)
pc1_rank = random.choice(ranks)
pc2_suit = random.choice(suits)
pc2_rank = random.choice(ranks)
print("\nPLAYER's Selected Cards:\nCard1: {} of {}\nCard2: {} of {}\n".format(pc1_rank,pc1_suit,pc2_rank,pc2_suit))

## Sum of Players' Cards amount.
p_Total = values[pc1_rank] + values[pc2_rank]
print("PLAYER's SUM: {}".format(p_Total))


## PLAYER Turn to select HIT or STAY!
while playing == True:
    player_inp = int(input("Please Select your move.\n1 = HIT\n2 = STAY\n3 = BET\nYour Move: "))
    if player_inp == 1:
        print("User Selected: HIT!")
        PRES = mybank.hit()
        p_Total = p_Total + PRES
        print("Player's Card Total is: {}".format(p_Total))
        if p_Total > 21:
            print("BUST! You lost this hand!\n")
            playing = False
        else:
            continue
    elif player_inp == 2:
        print("User Selected: STAY!\n")
        ## COMPUTER's Turn.
        print("\nCOMPUTER's Turn!")
        c_Total = values[cc1_rank] + values[cc2_rank]
        print("COMPUTER's Current Cards:\nCard1: {} of {}\nCard2: {} of {}".format(cc1_rank,cc1_suit,cc2_rank,cc2_suit))
        while True:
            if c_Total > 21:
                print("\nComputer's Card Sum: {}".format(c_Total))
                print("BUST! Computer Loses. You won this hand!\n")
                playing = False
                break
            elif c_Total > p_Total:
                print("COMPUTER's Cards Value: {}, your Cards Value: {}".format(c_Total,p_Total))
                print("COMPUTER Won! You lost this hand!")
                playing = False
                break
            else :
                print("Computer Goes for a HIT!")
                CRES = mybank.hit()
                c_Total = c_Total + CRES
                continue

    elif player_inp == 3:
        print("User Selected: BET!")
        mybank.bet()
        continue
    else:
        print("Invalid Choice")
        continue
