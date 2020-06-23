# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    COUNTER = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x ,y)
        self.radius = Black_Hole.RADIUS
    def count(self):
        self.counter += 1
        if self.counter > Pulsator.COUNTER:
            self.radius -= 1
            self.counter = 0
    def update(self, obj):
        self.eaten.add(obj)
        self.radius += 1
        return self.eaten