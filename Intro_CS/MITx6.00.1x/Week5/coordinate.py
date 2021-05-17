from typing import Coroutine


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x
    
    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    
    def distance(self, other):
        x_diff_sq = (self.x - other.x) **2
        y_diff_sq = (self.y - other.y) **2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'


#Tests
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c)