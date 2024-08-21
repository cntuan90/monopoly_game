"""
7.6HD Improved Custom Program

This module is used to handle all actions related to game (monopoly game)
"""

from player import Player
from dice import Dice
from board import Board
from card import CardDeck
import time

__author__ = "NGOC TUAN CAO"

_RENTAL_FEE_RATE = 0.2


class MonopolyGame:
    def __init__(self):
        self.players: list[Player]  = [] #Numbers of players
        self.game_board = Board() #the game board for players
        self.first_dice = Dice() #the 1st dice
        self.second_dice = Dice() #the 2nd dice
        self.card_deck = CardDeck() #card deck for players to draw
        self.start_time = 0 #The time to start the game
        self.duration = 0 #The game ends after this duration, set by player (minutes)

    def add_player(self, name):
        """
        Create players for the game
        """
        self.players.append(Player(name))
        
        
    # def sell_asset(self, player: Player):
    #     """
    #     Handle selling asset when a player is out of money
    #     """
    #     selected_asset: int = -1 #Index of asset in list properties, initially equal to -1
        
    #     if len(player.properties) > 0:
    #         while selected_asset < 1 or selected_asset > len(player.properties):
    #             print("Assets available for sale:")
    #             for idx, asset in enumerate(player.properties, 1):
    #                 print(f"{idx}: {asset}")
                    
    #             try:
    #                 selected_asset = int(input(f"Enter the number belonging to your asset as above to sell: "))
    #                 sold_asset_name: str = player.properties[selected_asset - 1]
                
    #                 for cell in self.game_board.board:
    #                     if cell["name"] == sold_asset_name:
    #                         player.update_money(cell["price"])
    #                         print(f"{player.name} has sold {sold_asset_name} for ${cell["price"]}, current money: {player.money}")
    #                         cell["available"] = True
                            
    #                 player.properties.pop(selected_asset - 1)
    #             except (ValueError, IndexError) as ex:
    #                 print(ex)
    #     else:
    #         print(f"{player.name} has no assets to sell.")


    def sell_asset(self, player: Player):
        """
        Handle selling asset when a player is out of money
        """
        while player.properties:
            try:
                print()
                print("Assets available for sale:")
                for i, asset in enumerate(player.properties, 1):
                    print(f"{i}: {asset}")
                    
                selected_asset = int(input("Enter the number of the asset to sell: ")) - 1
                if 0 <= selected_asset < len(player.properties):
                    asset_name = player.properties[selected_asset]
                    for cell in self.game_board.board:
                        if cell["name"] == asset_name:
                            player.update_money(cell["price"])
                            print(f"{player.name} sold {asset_name} for ${cell['price']}. Current money: ${player.money}")
                            cell["available"] = True
                            player.properties.pop(selected_asset)
                            return
            except (ValueError, IndexError) as ex:
                print(ex)
        print(f"{player.name} has no assets to sell.")


    def play_game(self):
        """
        Check if players are more than 1 to continue playing game
        """
        choice: str = "n" # Initially euqal to No
        self.start_time = int(time.time())
        
        while len(self.players) > 1:
            self.check_duration() #To decide the winner based on duration set
            
            for i, player in enumerate(self.players):
                print()
                print(player)
                if player.money <= 0:
                    choice = input(f"{player.name} is out of money, do you want to sell an asset showing above (y/n): ").lower()
                    if choice == "y":
                        self.sell_asset(player)
                    else:
                        self.players.pop(i)
                else:
                    self.player_turn(player)
                    
        self.game_winner()
    
    
    def game_winner(self):
        """
        Inform the winner of the game
        """
        if self.players:
            print(f"The winner is {self.players[0].name}")
            
    
    def calculate_total_assets(self, player: Player) -> int:
        """
        Calculate total asset for a player
        """
        total_assets = player.money
        for asset in player.properties:
            for cell in self.game_board.board:
                if cell["name"] == asset:
                    total_assets += cell["price"]
        return total_assets
    
    
    def check_duration(self) -> None:
        """
        Check the duration time and asset of each players to decide the winner
        """
        current_time = int(time.time())
        if (current_time - self.start_time) > (self.duration * 60):
            winner = max(self.players, key=self.calculate_total_assets)
            print()
            print(f"Time is out! The winner is {winner.name} with total assets of ${self.calculate_total_assets(winner)}")
            exit()
        
        
    # def check_duration(self):
    #     """
    #     Check the duration time and asset of each players to decide the winner
    #     """
    #     current_time: int #the current time
    #     player_total_assets: int #the total amount of money including assets of a player
    #     winner: Player  #The winner
        
    #     winner_total_assets:int = 0 #the total amount of money including assets of winner, initially equal to 0
    #     current_time = int(time.time())
        
    #     if ((current_time - self.start_time) > (self.duration * 60)):
    #         for player in (self.players):
    #             player_total_assets = player.money #the total amount of money including assets, initially equal to 0
                
    #             for asset in self.players[0].properties:
    #                 for i, cell in enumerate(self.game_board.board):
    #                     if asset == cell["name"]:
    #                         player_total_assets += cell["price"]
                            
    #             if player_total_assets > winner_total_assets:
    #                 winner_total_assets = player_total_assets
    #                 winner = player
            
    #         print()
    #         print(f"Time is out! The winner is {winner.name} with the total assets ${winner_total_assets}")
    #         exit()


    def player_turn(self, player: Player):
        """
        Check if player is in jail or make a move
        """
        self.check_duration()
        
        if player.in_jail.name == "IJ":
            self.handle_jail(player)
        else:
            self.handle_move(player)


    def handle_jail(self, player: Player):
        """
        Player needs to roll 2 dice at same number to get out the jail
        """
        first_dice = self.first_dice.roll()
        second_dice = self.second_dice.roll()
        print(f"{player.name} rolls {first_dice} and {second_dice}")
        
        if first_dice == second_dice:
            print(f"{player.name} is released from jail!")
            player.get_out_of_jail()
            self.handle_move(player)


    def handle_move(self, player: Player):
        """
        Roll dice and make a move
        """
        quit_game: str = "" #Initially, equal to ""
        
        first_dice = self.first_dice.roll()
        second_dice = self.second_dice.roll()
        quit_game = input("Enter q to quit game or any letter to roll the dice: ").lower()
        if quit_game == "q":
            exit()
        
        print(f"{player.name} rolls {first_dice} and {second_dice}")
        
        player.move_position(first_dice + second_dice)
        self.process_cell(player)
        
        if first_dice == second_dice:
            print(f"{player.name} rolls a double and gets another turn!")
            self.handle_move(player)


    def process_cell(self, player: Player):
        """
        Decide what player need to do when landing on a cell
        There are 3 kinds of cell properties
            1. action (i.e. drawing card, visiting jail)
            2. price (i.e. buying building)
            3. fee (i.e. paying tax)
        """
        cell: dict #The property of a cell to show detail
        
        cell = self.game_board.board[player.position]
        
        print(f"{player.name} lands on {cell['name']}")
        
        if "action" in cell:
            cell["action"](player, self.card_deck)
        elif "price" in cell:
            self.handle_property(player, cell)
        elif "fee" in cell:
            self.handle_fee(player, cell)


    def handle_property(self, player: Player, cell: dict):
        """
        Interacting with property cells
        """
        rent: int #renting fee when player land on other player's asset
        choice: str #Ask user to buy asset or not
        
        if cell["available"]:
            if player.money >= cell["price"]:
                choice = input(f"Do you want to buy {cell['name']} for ${cell['price']}? (y/n): ").lower()
                
                if choice == 'y':
                    print(f"{player.name} buys {cell['name']} for ${cell['price']}")
                    player.update_money(-cell["price"])
                    player.properties.append(cell["name"])
                    
                    ### Update cell status
                    cell["available"] = False
                    cell["owner"] = player.name
        else:
            if cell["owner"] != player.name:
                rent = cell["price"] * _RENTAL_FEE_RATE # paying renting fee when land on other's player assets
                print(f"{player.name} pays ${rent} rent to {cell['owner']}")
                
                player.update_money(-rent)
                
                for p in self.players:
                    if p.name == cell["owner"]:
                        p.update_money(rent) # update money for owner


    def handle_fee(self, player: Player, cell):
        """
        Charge fee when landing on tax cell
        """
        print(f"{player.name} pays ${cell['fee']}")
        player.update_money(-cell['fee'])