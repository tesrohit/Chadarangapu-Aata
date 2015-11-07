__author__ = 'TESR'

class Piece(object):  # Abstract Class for every piece
    def move(self, source1, source2,  dest1, dest2):
        pass

class Rook(Piece):
    def __init__(self, colour):
        self.name = 'Rook'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""


class Knight(Piece):
    def __init__(self, colour):
        self.name = 'Knight'
        self.colour = colour

    def move(self, dest1, dest2):
        """Implementing the logic"""


class Bishop(Piece):
    def __init__(self, colour):
        self.name = 'Bishop'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""


class King(Piece):
    def __init__(self, colour):
        self.name = 'King'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""


class Queen(Piece):
    def __init__(self, colour):
        self.name = 'Queen'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""


class Pawn(Piece):
    def __init__(self, colour):
        self.name = 'Pawn'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        result = False
        vertical = False
        horizontal = False
        print str(source1) + " " + str(source2) + " " + str(dest1) + " " + str(dest2)
        if source1 == 1:
            if dest1 == 2:
                vertical = True
            elif dest1 == 3:
                vertical = True
        else:
            if (dest1 - source1) == 1:
                vertical = True

        if source2 == dest2:
            horizontal = True

        if (horizontal and vertical):
            result = True
            return result
        return result
        """Implementing the logic"""


class Blank(Piece):
    def __init__(self, colour):
        self.name = 'Empty'
        self.colour = colour

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""
        print "Invalid Position"
        return
