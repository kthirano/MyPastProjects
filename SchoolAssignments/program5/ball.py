# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    RADIUS = 5
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Ball.RADIUS * 2, Ball.RADIUS * 2, 0, 5)
        self.randomize_angle()
        
    def update(self):
        self.move()
        
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.RADIUS      , self._y-Ball.RADIUS,
                                self._x+Ball.RADIUS, self._y+Ball.RADIUS,
                                fill="blue")

        