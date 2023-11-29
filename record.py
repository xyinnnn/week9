import time
from pprint import pprint
from lib import *

import pandas as pd
    

"""
record game play data
data = {
    "game_id": "", # 0
    "move_count": "", 8
    "start_time": "2023-11-22 12:00"
    "end_time": "2023-11-22 13:00"
    "duration": "", # 102387
    "winner": "", # X
}
"""

game_data = []
# 10 games
for x in range(10):
    game_id = x
    move_count = 0
    data = {}
    player1 = BotPlayer("X")
    player2 = BotPlayer("O")
    game = Game(player1, player2)
    start_time = time.time()
    data['game_id'] = game_id
    data['start_time'] = start_time
    while True:
        move_count += 1
        game.board.print_board()
        if not game.current_player.make_move(game.board):
            print("Invalid move, try again.")
            continue
        
        if game.board.check_winner(game.current_player.symbol):
            game.board.print_board()
            print(f"Player {game.current_player.symbol} wins!")
            data['winner'] = game.current_player.symbol
            data['move_count'] = move_count
            end_time = time.time()
            data['end_time'] = end_time
            data['duration'] = end_time - start_time
            break

        if game.board.is_full():
            game.board.print_board()
            print("It's a tie!")
            data['winner'] = "draw"
            data['move_count'] = move_count
            end_time = time.time()
            data['end_time'] = end_time
            data['duration'] = end_time - start_time
            break

        game.switch_player()

    game_data.append(data)

pprint(game_data)
pd.DataFrame(game_data).to_csv("./logs/database.csv")
