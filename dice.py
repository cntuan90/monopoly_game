"""
7.6HD Improved Custom Program

This module is used to create a Dice
"""

import random

__author__ = "NGOC TUAN CAO"


# class Dice:
#     def __init__(self):
#         self.dice_value: int = random.randint(1, 6) #The value on the dice
    
#     def roll(self) -> int:
#         dice_value = random.randint(1, 6)
#         return dice_value
class Dice:
    def roll(self) -> int:
        return random.randint(1, 6)