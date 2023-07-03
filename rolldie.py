# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 13:36:59 2023

@author: Jacks
dice
"""

# MAKE THIS WORK FOR N NUMBER OF DIE

import random
import os

def num_die():
    while True:
        try:
            num_dice = input('Number of die: ')
            valid_responses = ['1', 'one', '2', 'two']
            if num_dice not in valid_responses:
                raise ValueError('1 or 2 only')
            else:
                return num_dice
        except ValueError as err:
            print(err)

def roll_dice():
    min_val = 1
    max_val = 6
    roll_again = 'y'
    
    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_die()
        
        if amount == '2' or amount == 'two':
            print('Rolling the dice...')
            dice1 = random.randint(min_val, max_val)
            dice2 = random.randint(min_val, max_val)
            
            print('The values are: ')
            print('Dice one: ', dice1)
            print('Dice two: ', dice2)
            print('Total: ', dice1+dice2)
            
            roll_again = input('Roll again? ')
        else:
            print('Rolling the die...')
            dice1 = random.randint(min_val, max_val)
            print(f'The value is: {dice1}')
            
            roll_again = input('Roll again? ')
            
if __name__ == '__main__':
    roll_dice()