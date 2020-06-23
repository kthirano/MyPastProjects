from hunter import Hunter
from random import shuffle

#this object is basically a hunter but every time it eats an object it changes color
# and if after 20 cycles it doesn't eat anything it will start rapidly changing colors
# and decrease in size slowly

class Special(Hunter):
    colorchoice = ["red", "blue", "green", "pink", "orange", "yellow", "purple"]
    def __init__(self, x, y):
        Hunter.__init__(self, x, y)
        self.mycolor = "red"
    def getrandomcolor(self):
        shuffle(Special.colorchoice)
        return Special.colorchoice[0]
    def count(self):
        self.counter += 1
        if self.counter > 20:
            self.mycolor = self.getrandomcolor()
        if self.counter > 30:
            self.radius -= 1
            self.counter = 0
        self.move()
    def update(self, obj):
        self.eaten.add(obj)
        self.radius += 1
        self.counter= 0    
        self.mycolor = self.getrandomcolor()
        return self.eaten
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius      , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill=self.mycolor)
