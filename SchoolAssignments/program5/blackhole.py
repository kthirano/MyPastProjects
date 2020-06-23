# A Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    RADIUS = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.RADIUS * 2, Black_Hole.RADIUS * 2)
        self.eaten = set()
        self.counter = 0
        self.radius = Black_Hole.RADIUS
    
    def update(self, obj):
        self.eaten.add(obj)
        return self.eaten
    
    def count(self):
        self.counter += 1
    
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill="black")
        
    def contains(self, xy):
        return self.distance(xy) <= self.radius
