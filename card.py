"""
7.6HD Improved Custom Program

This module is used to create Card Deck (chance cards & community chest cards)
"""

from dataclasses import dataclass
import random
from player import Player
from typing import Callable

__author__ = "NGOC TUAN CAO"


@dataclass
class Card: 
    description: str
    action: Callable[[Player], None]
    

class CardDeck:    
    def __init__(self):
        self.community_chest_cards: list[Card]  = self.create_community_chest_cards() # Card deck for community chest
        self.chance_cards: list[Card] = self.create_chance_cards() # Card deck for chance
        random.shuffle(self.community_chest_cards)
        random.shuffle(self.chance_cards)


    def draw_community_chest(self) -> Card:
        """
        Draw a card from community chest cards
        """
        card = self.community_chest_cards.pop(0)
        self.community_chest_cards.append(card)  # Put the card back at the bottom
        return card


    def draw_chance(self) -> Card:
        """
        Draw a card from chance cards
        """
        card = self.chance_cards.pop(0)
        self.chance_cards.append(card)  # Put the card back at the bottom
        return card


    def create_community_chest_cards(self) -> list[Card]:
        """
        Initialise community chest cards
        """
        return [
            Card("Advance to GO. Collect $100.", self.advance_to_go),
            Card("Bank error in your favor. Collect $100.", self.bank_error),
            Card("Doctor's fees. Pay $80.", self.pay_doctor_fee),
            Card("From sale of stock you get $50.", self.sale_of_stock),
            Card("Go to Jail. Go directly to jail, do not pass GO, do not collect $200.", self.go_to_jail),
        ]


    def create_chance_cards(self) -> list[Card]:
        """
        Initialise chance cards
        """
        return [
            Card("Advance to GO. Collect $100.", self.advance_to_go),
            Card("Bank pays you dividend of $50.", self.bank_dividend),
            Card("Go back 3 cells.", self.go_back_3_cells),
            Card("Go to Jail. Go directly to jail!", self.go_to_jail),
            Card("Speeding fine $120.", self.speeding_fine),
        ]


    def advance_to_go(self, player: Player):
        """
        Move directly to start position and get $100
        """
        player.position = 0
        print(f"{player.name} move directly to start position and get $100")
        player.update_money(100)


    def bank_error(self, player: Player):
        """
        Get $200 because of bank error
        """
        print(f"{player.name} get $200 because of bank error")
        player.update_money(100)


    def pay_doctor_fee(self, player: Player):
        """
        Fee to pay doctor
        """
        print(f"{player.name} pay $80 fee for doctor")
        player.update_money(-80)


    def sale_of_stock(self, player: Player):
        """
        Get $50 from stock sale
        """
        print(f"{player.name} get $50 from stock sale")
        player.update_money(50)


    def go_to_jail(self, player: Player):
        """
        Put the player into jail
        """
        player.position = 10
        print(f"Put {player.name} into Jail!")
        player.go_to_jail()


    def bank_dividend(self, player: Player):
        """
        Receive $50 dividend from bank
        """
        print(f"{player.name} receive $50 dividend from bank!")
        player.update_money(50)


    def go_back_3_cells(self, player: Player):
        """
        Put the player back 3 cells
        """
        print(f"{player.name} goes back 3 cells!")
        player.move_position(-3)


    def speeding_fine(self, player: Player):
        """
        Get fined $15 because of speeding
        """
        print(f"{player.name} get fined $15 because of speeding!")
        player.update_money(-120)