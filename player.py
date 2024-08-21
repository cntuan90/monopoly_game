"""
7.6HD Improved Custom Program

This module is used to add players and update properties of players
"""

from enum import Enum

__author__ = "NGOC TUAN CAO"

_BOARD_SIZE = 39


class PlayerStatus(Enum):
    """ Status of player """
    IJ = "IN JAIL"
    F = "FREE"

class Player:    
    def __init__(self, name):
        self.name: str = name #Player name
        self.money = 400 #Set money for each player initially, 
        self.position = 0 #Store the position of player
        self.properties: list[str] = [] #Store assets when player buy
        self.in_jail = PlayerStatus["F"] #Status of player (not in jail)


    def update_money(self, amount):
        """
        Update money of player
        """
        self.money += amount


    def move_position(self, steps):
        """
        Update the position of player
        """
        self.position += steps
        if self.position > _BOARD_SIZE:  # Passed GO cell
            self.update_money(100)
            print(f"{self.name} has passed a round and received $100, current money: {self.money}")
            self.position = self.position % 40


    def go_to_jail(self):
        """
        Put the player into jail
        """
        self.position = 10
        self.in_jail = PlayerStatus["IJ"]


    def get_out_of_jail(self):
        """
        Update the status of player (out of jail)
        """
        self.in_jail = PlayerStatus["F"]


    def __str__(self):
        list_properties: str = "" #Initially, the list is blank
        
        for i, property in enumerate(self.properties):
            list_properties += f"{i+1}.{property} "
            
        return f"{self.name}({self.in_jail.value}) - Money: ${self.money}, Position: {self.position}, Properties: {list_properties}"