#!/usr/bin/python3

# Random-move Gothello player.

import random
import sys
import gthclient


class Minimax:
    """
    Gothello player using minimax algorithm
    me:     This player's color ('black' or 'white')
    client: gthclient object
    opp:    Enemy player's color ('black' or 'white')
    boardsize: Size of board
    board: Set of possible moves left with values letter+digit
    grid: current state of the board as a dictionary of sets. Dict keys are 'black' or 'white' with values being
        a set of letter+digit combos signifying spots taken by those colors.
    """

    def __init__(self, color, boardsize):
        """
        :param color: This player's color ('black' or 'white')
        :param boardsize: Size of board

        """
        self.me = color
        self.client = gthclient.GthClient(self.me, "localhost", 0)
        self.opp = gthclient.opponent(self.me)
        self.boardsize = boardsize
        self.board = {letter + digit for letter in self.letter_range('a') for digit in self.letter_range('1')}
        self.grid = {"white": set(), "black": set()}

    def letter_range(self, letter):
        """
        Get range of letter or digit coordinate
        :param letter: letter or digit as string
        :return: range of letters or digits
        """
        for i in range(self.boardsize):
            yield chr(ord(letter) + i)

    def show_position(self):
        """
        Print current grid where white is "O", black is "*", empty space is "."
        :return:
        """
        for digit in self.letter_range('1'):
            for letter in self.letter_range('a'):
                pos = letter + digit
                if pos in self.grid["white"]:
                    piece = "O"
                elif pos in self.grid["black"]:
                    piece = "*"
                else:
                    piece = "."
                print(piece, end="")
            print()

    def score_position(self):
        """
        Score current grid as # player's pieces minus # of opp's pieces
        :return: int
        """
        return len(self.grid[self.me]) - len(self.grid[self.opp])

    def play(self):
        """
        Commence playing a game of Gothello
        :return:
        """
        side = "black"  # black always goes first

        while True:
            self.show_position()
            if side == self.me:
                move = random.choice(list(self.board))
                print("me:", move)
                try:
                    self.client.make_move(move)
                    self.grid[self.me].add(move)
                    self.board.remove(move)
                except gthclient.MoveError as e:
                    if e.cause == e.ILLEGAL:
                        print("me: made illegal move, passing")
                        self.client.make_move("pass")
            else:
                cont, move = self.client.get_move()
                print("opp:", move)
                if cont and move == "pass":
                    print("me: pass to end game")
                    self.client.make_move("pass")
                    break
                else:
                    if not cont:
                        break
                    self.board.remove(move)
                    self.grid[self.opp].add(move)

            side = gthclient.opponent(side)
