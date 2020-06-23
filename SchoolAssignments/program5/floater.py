# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    RADIUS = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.RADIUS * 2, Floater.RADIUS * 2, 0, 5)
        self.randomize_angle()
        
    def update(self):
        numberoftheday = random()
        if numberoftheday < .3:
            anglechange = self.get_angle() + random() - 0.5
            self.set_angle(anglechange)
            speedchange = self.get_speed() + random() - 0.5
            if speedchange >= 3 and speedchange <= 7:
                self.set_speed(speedchange)
        self.move()

        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.RADIUS      , self._y-Floater.RADIUS,
                                self._x+Floater.RADIUS, self._y+Floater.RADIUS,
                                fill="red")