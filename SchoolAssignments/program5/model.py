import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
lastobject = ''
balls       = []
eaters      = []
hunters     = []

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls,eaters, hunters
    running     = False
    cycle_count = 0
    balls       = []
    eaters      = []
    hunters     = []


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running, cycle_count
    cycle_count += 1
    running = True
    update_all()
    running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global lastobject
    lastobject = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global balls, lastobject, eaters
    found = False
    dimensions = [x,y]
    for b in balls:
        if b.contains(dimensions) == True:
            found = True
            remove(b)
    for e in eaters:
        if e.contains(dimensions) == True:
            found = True
            remove(e)
    for h in hunters:
        if h.contains(dimensions) == True:
            found = True
            remove(h)
    if found == False and str(lastobject) != 'Remove':
        if str(lastobject) != '':
            masterstr = str(lastobject)
            masterstr += '(' + str(x) + ',' + str(y) + ')'
            add(eval(masterstr))


#add simulton s to the simulation
def add(s):
    global balls, eaters
    if 'prey' in str(type(s)) or 'prey' in str(type(s).__bases__):
        balls.append(s)
    elif 'hunter' in str(type(s)) or 'hunter' in str(type(s).__bases__):
        hunters.append(s)
    else:
        eaters.append(s)

# remove simulton s from the simulation    
def remove(s):
    global balls, eaters, eaters
    if 'prey' in str(type(s).__bases__):
        balls.remove(s)
    elif 'hunter' in str(type(s)) or 'hunter' in str(type(s).__bases__):
        hunters.remove(s)
    else:
        eaters.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return balls

#call update for every simulton in the simulation
def update_all():
    global cycle_count, balls, eaters, hunters
    if running:
        cycle_count += 1
        for b in balls:
            b.update()
        for h in hunters:
            h.count()
            h.chaseclosest(balls)
            if h.radius == 0:
                hunters.remove(h)
            for b in balls:
                if h.contains(b.get_location()):
                    h.update(b)
                    balls.remove(b)
        for e in eaters:
            e.count()
            if e.radius == 0:
                eaters.remove(e)
            for b in balls:
                if e.contains(b.get_location()):
                    e.update(b)
                    balls.remove(b)
                    

#delete from the canvas every simulton in the simulation; then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    for e in eaters:
        e.display(controller.the_canvas)
    for h in hunters:
        h.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")

