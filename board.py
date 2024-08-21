"""
7.6HD Improved Custom Program

This module is used to initialise the game board
"""

from player import Player
from card import CardDeck

__author__ = "NGOC TUAN CAO"


class Board:
    def __init__(self):
        self.board = self.create_board() #To store the properties of each cell

    def create_board(self) -> list[dict]:
        """
        Initialise the game board with every specific cell properties
        """
        return [
            {"name": "GO", "action": self.pass_go},
            {"name": "Mediterranean Avenue", "price": 60, "available": True, "owner": ""},
            {"name": "Community Chest", "action": self.draw_community_chest},
            {"name": "Baltic Avenue", "price": 60, "available": True, "owner": ""},
            {"name": "Income Tax", "fee": 200},
            {"name": "Reading Railroad", "price": 200, "available": True, "owner": ""},
            {"name": "Oriental Avenue", "price": 100, "available": True, "owner": ""},
            {"name": "Chance", "action": self.draw_chance},
            {"name": "Vermont Avenue", "price": 100, "available": True, "owner": ""},
            {"name": "Connecticut Avenue", "price": 120, "available": True, "owner": ""},
            {"name": "Visiting Jail or in Jail", "action": self.visit_jail},
            {"name": "St. Charles Place", "price": 140, "available": True, "owner": ""},
            {"name": "Electric Company", "price": 150, "available": True, "owner": ""},
            {"name": "States Avenue", "price": 140, "available": True, "owner": ""},
            {"name": "Virginia Avenue", "price": 160, "available": True, "owner": ""},
            {"name": "Pennsylvania Railroad", "price": 200, "available": True, "owner": ""},
            {"name": "St. James Place", "price": 180, "available": True, "owner": ""},
            {"name": "Community Chest", "action": self.draw_community_chest},
            {"name": "Tennessee Avenue", "price": 180, "available": True, "owner": ""},
            {"name": "New York Avenue", "price": 200, "available": True, "owner": ""},
            {"name": "Free Parking", "action": self.free_parking},
            {"name": "Kentucky Avenue", "price": 220, "available": True, "owner": ""},
            {"name": "Chance", "action": self.draw_chance},
            {"name": "Indiana Avenue", "price": 220, "available": True, "owner": ""},
            {"name": "Illinois Avenue", "price": 240, "available": True, "owner": ""},
            {"name": "B&O Railroad", "price": 200, "available": True, "owner": ""},
            {"name": "Atlantic Avenue", "price": 260, "available": True, "owner": ""},
            {"name": "Ventnor Avenue", "price": 260, "available": True, "owner": ""},
            {"name": "Water Works", "price": 150, "available": True, "owner": ""},
            {"name": "Marvin Gardens", "price": 280, "available": True, "owner": ""},
            {"name": "Go To Jail", "action": self.go_to_jail},
            {"name": "Pacific Avenue", "price": 300, "available": True, "owner": ""},
            {"name": "North Carolina Avenue", "price": 300, "available": True, "owner": ""},
            {"name": "Community Chest", "action": self.draw_community_chest},
            {"name": "Pennsylvania Avenue", "price": 320, "available": True, "owner": ""},
            {"name": "Short Line", "price": 200, "available": True, "owner": ""},
            {"name": "Chance", "action": self.draw_chance},
            {"name": "Park Place", "price": 350, "available": True, "owner": ""},
            {"name": "Luxury Tax", "fee": 75},
            {"name": "Boardwalk", "price": 400, "available": True, "owner": ""},
        ]


    def pass_go(self, player: Player, card_deck):
        """
        Receive $100 when pass a round
        """
        player.update_money(100)


    def draw_community_chest(self, player: Player, card_deck: CardDeck):
        """
        Draw a card from community chest cards
        """
        card = card_deck.draw_community_chest()
        card.action(player)


    def draw_chance(self, player: Player, card_deck: CardDeck):
        """
        Draw a card from chance cards
        """
        card = card_deck.draw_chance()
        card.action(player)


    def free_parking(self, player: Player, card_deck):
        """
        Stand on card park, do nothing
        """
        print(f"{player} is in free parking!")


    def visit_jail(self, player: Player, card_deck):
        """
        Just visiting a jail
        """
        print(f"{player} is visiting jail!")


    def go_to_jail(self, player: Player, card_deck):
        """
        Put the player into jail
        """
        print(f"Put {player.name} into Jail!")
        player.go_to_jail()