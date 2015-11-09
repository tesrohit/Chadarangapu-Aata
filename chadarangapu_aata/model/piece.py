__author__ = 'TESR'
'''
Each piece can be placed in seperate class!
'''

import logging
_logger = logging.getLogger(__name__)

class Rook():
    def __init__(self, colour, x = None, y = None):
        self.name = 'Rook'
        self.representation = "R"
        self.colour = colour
        self.x = x
        self.y = y

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""

class Knight():
    def __init__(self, colour, x = None, y = None):
        self.name = 'Knight'
        self.representation = "N"
        self.colour = colour
        self.x = x
        self.y = y

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""

    
        

class Bishop():
    def __init__(self, colour, x = None, y = None):
        self.name = 'Bishop'
        self.representation = "B"
        self.colour = colour
        self.x = x
        self.y = y

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""

    
        

class King():
    def __init__(self, colour, x = None, y = None):
        self.name = 'King'
        self.representation = "K"
        self.colour = colour
        self.x = x
        self.y = y

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""

    
        

class Queen():
    def __init__(self, colour, x = None, y = None):
        self.name = 'Queen'
        self.representation = "Q"
        self.colour = colour
        self.x = x
        self.y = y

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""

    
        

class Pawn():
    def __init__(self, colour, x = None, y = None):
        self.name = 'Pawn'
        self.representation = "P"
        self.colour = colour
        self.x = x
        self.y = y

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

        if horizontal and vertical:
            result = True
            return result
        return result

    
        

class Blank():
    def __init__(self, colour, x = None, y = None):
        self.name = 'Empty'
        self.representation = " "
        self.colour = colour
        self.x = x
        self.y = y

    def move(self, source1, source2, dest1, dest2):
        """Implementing the logic"""
        print "Invalid Position"
        return

    
        
