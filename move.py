# Heavily based on https://github.com/pdx-cs-ai/gothello-gthd/blob/master/Move.java
BOARD_SIZE = 5


class Move:
    """
    Grid coords in range 0-BOARD_SIZE where 1st is the column(x) value and second is the row(y) value
    Coord -1, -1 is a pass
    """
    def __init__(self, desc):
        """
        Create a move object given a string description
        :param desc: Two character string coord or the string "pass"
        """
        if desc == "pass":
            self.x = -1
            self.y = -1
        elif desc.len != 2:
            raise Exception('Moves must be 2 char')
        else:
            self.x = self.move_letter(desc[0])
            self.y = self.move_digit(desc[1])

    @classmethod
    def from_coords(cls, x, y):
        """
        Create a move object given coordinates
        :param x: x coord as int
        :param y: y coord as int
        """
        return cls(x, y)

    def move_digit(self, char):
        """
        given a char number return coord as int
        :param char: number as single char
        :return: coord as int
        """
        switcher = {}
        for i in range(BOARD_SIZE):
            switcher[str(i+1)] = i
        if char not in switcher:
            raise Exception("Bad digit")
        else:
            return switcher[char]

    def move_letter(self, char):
        """
        given a char letter return coord as int
        :param char: letter as single char
        :return: coord as int
        """
        switcher = {}
        alpha_num = 97
        for i in range(BOARD_SIZE):
            switcher[chr(alpha_num)] = i
            alpha_num += 1
        if char not in switcher:
            raise Exception("Bad letter")
        else:
            return switcher[char]

    def is_pass(self):
        """
        check if move is a pass
        :return: True of pass, false otherwise
        """
        return self.x == -1 and self.y == -1

    def name(self):
        if self.is_pass():
            return "pass"
        elif not (0 <= self.y <= BOARD_SIZE):
            raise Exception("bad y coord in square")
        switcher = {}
        alpha_num = 97
        for i in range(BOARD_SIZE):
            switcher[i] = chr(alpha_num) + str(self.y+1)
            alpha_num += 1
        if (self.x+1) not in switcher:
            raise Exception("bad x coord in square")
        else:
            return switcher[self.x+1]