#!/usr/bin/python3

# Minimax Gothello player.

import sys
import workboard
import move
import gthclient


GAME_OVER = 1
CONTINUE = 0
ILLEGAL_MOVE = -1
WHITE = 1
BLACK = 2
OBSERVER = 3
BOARD_SIZE = 5
DEPTH = 3


class Player:
    """
    Gothello player using minimax algorithm
    me:     This player's color ('black' or 'white')
    client: gthclient object
    opp:    Enemy player's color ('black' or 'white')
    board_size: Size of board
    board:  Set of possible moves left with values letter+digit
    grid:   current state of the board as a dictionary of sets. Dict keys are 'black' or 'white' with values being
        a set of letter+digit combos signifying spots taken by those colors.
    """

    def __init__(self, depth, color, client):
        """
        :param depth: depth to search as int
        :param color: player's color as int
        """
        self.depth = depth
        self.board = workboard.Workboard()
        self.client = client
        self.color = color

    def play(self):
        """
        Commence playing a game of Gothello
        :return:
        """
        while True:

            if self.board.to_move == me:
                mv = self.board.find_best_move(DEPTH)  # mv is a Move object
                print("me:", mv.name())
                try:
                    self.client.make_move(mv.name())
                    self.board.try_move(mv)
                except gthclient.MoveError as e:
                    if e.cause == e.ILLEGAL:
                        print("me: made illegal move, passing")
                        self.client.make_move("pass")
            else:
                cont, mv = self.client.get_move()  # mv is a string eg "a1"
                print("opp:", move)
                if cont and move == "pass":
                    print("me: pass to end game")
                    self.client.make_move("pass")
                    break
                else:
                    if not cont:
                        break
                    self.board.try_move(move.Move.from_desc(mv))


if sys.argv[1] == "white":
    me = WHITE
elif sys.argv[1] == "black":
    me = BLACK
else:
    raise Exception("bad color arg")
clnt = gthclient.GthClient(me, "localhost", 0)
player = Player(DEPTH, me, clnt)
