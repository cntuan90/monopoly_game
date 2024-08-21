"""
7.6HD Improved Custom Program

This program is used to create a Monopoly game with some basic features.
"""

from game_processor import MonopolyGame


__author__ = "NGOC TUAN CAO"


def game_setting(game: MonopolyGame):
    num_players: int #number of players
    
    try:
        game.duration = int(input("Enter the duration of the game (30 mins or 60 mins): ")) #Ask user to input the duration for the game
        num_players = int(input("Enter number of players (2-4): ")) #Ask user to input the number of players
    
        for i in range(num_players):
            name = input(f"Enter name of player {i+1}: ") #Enter the player name
            game.add_player(name)
            
    except (ValueError, IndexError) as ex:
        print(ex)


def main():
    game: MonopolyGame = MonopolyGame() #Initialise the game board of monopoly game
    
    print("Welcome to the Monopoly Game!")
    print()
    
    game_setting(game)
    
    game.play_game()
    

if __name__ == "__main__":
    main()