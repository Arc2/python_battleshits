from random import randint
from typing import Tuple

from board import Board

board = Board(10)

print("Let's play Battleships!")
board.print_with_fog()


class Player:
    def __init__(self, id_):
        self.id = id_
        self.board = Board(10)

    def get_ships_locations(self) -> Board:
        board = Board(10)
        ships_locations = (
            (1, 1), (2, 1),
            (2, 3),
            (8, 1),
            (4, 3), (4, 4),
            (6, 2), (6, 3), (6, 4),
            (4, 7), (5, 7), (6, 7), (7, 7),
            (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)
        )
        for location in ships_locations:
            board.fields[location[0]][location[1]].has_ship = True
        return board

    def get_shot_location(self) -> Tuple[int, int]:
        return randint(0, 9), randint(0, 9)


player1 = Player(1)
player2 = Player(2)
player1.board = player1.get_ships_locations()
player2.board = player2.get_ships_locations()

turn = 0
while True:
    turn += 1
    print(f"Turn {turn}")
    if turn % 10 == 0:
        print('Player 1 board as seen by Player 1:')
        player1.board.print()
        print()
        print('Player 2 board as seen by Player 1:')
        player2.board.print_with_fog()
    if turn % 2 == 0:
        coords = player1.get_shot_location()
        player2.board.shoot(*coords)
        print(f'Player 1 shot {coords}')
        input()
    else:
        coords = player2.get_shot_location()
        player1.board.shoot(*coords)
        print(f'Player 2 shot {coords}')
        input()
