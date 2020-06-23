# A Hunter is derived from a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    TARGET = 200
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)
        Pulsator.__init__(self, x,y)
        self.randomize_angle()
    def update(self, obj):
        self.eaten.add(obj)
        self.radius += 1
        self.counter= 0
        return self.eaten
    def count(self):
        self.counter += 1
        if self.counter > Pulsator.COUNTER:
            self.radius -= 1
            self.counter = 0
        self.move()
    def findangle(self, setofunits):
        xcomponent = setofunits[0] - self._x
        ycomponent = setofunits[1] - self._y
        return atan2(ycomponent, xcomponent)
    def finddistance(self, setofunits):
        xcomponent = setofunits[0] - self._x
        ycomponent = setofunits[1] - self._y
        rootthis = xcomponent ** 2 + ycomponent ** 2
        return rootthis ** (1/2)
    def chaseclosest(self, listofprey):
        mindistance = 201
        minobject = None
        for preys in listofprey:
            thedistance = self.finddistance(preys.get_location())
            if thedistance < mindistance:
                mindistance = thedistance
                minobject = preys
        if minobject != None:
            fangle = self.findangle(minobject.get_location())
            self.set_angle(fangle)
        else:
            self.randomize_angle()
    
