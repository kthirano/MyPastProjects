import prompt
from goody import irange


# List Node class and helper functions (to set up problem)

class LN:
    def __init__(self,value,next=None):
        self.value = value
        self.next  = next

def list_to_ll(l):
    if l == []:
        return None
    front = rear = LN(l[0])
    for v in l[1:]:
        rear.next = LN(v)
        rear = rear.next
    return front

def str_ll(ll):
    answer = ''
    while ll != None:
        answer += str(ll.value)+'->'
        ll = ll.next
    return answer + 'None'



# Tree Node class and helper functions (to set up problem)

class TN:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right

def list_to_tree(alist):
    if alist == None:
        return None
    else:
        return TN(alist[0],list_to_tree(alist[1]),list_to_tree(alist[2])) 
    
def str_tree(atree,indent_char ='.',indent_delta=2):
    def str_tree_1(indent,atree):
        if atree == None:
            return ''
        else:
            answer = ''
            answer += str_tree_1(indent+indent_delta,atree.right)
            answer += indent*indent_char+str(atree.value)+'\n'
            answer += str_tree_1(indent+indent_delta,atree.left)
            return answer
    return str_tree_1(0,atree) 


# Define pair_sum ITERATIVELY

def pair_sum(ll):
    if ll == None:
        return None
    if ll.next == None:
        return None
    part1 = part2 = LN(ll.value + ll.next.value)
    if ll.next == None:
        return part1
    ll = ll.next.next
    while ll != None:
        if ll.next == None:
            break
        part2.next = LN(ll.value + ll.next.value)
        part2 = part2.next
        ll = ll.next.next
    return part1



# Define pair_sum_r RECURSIVELY

def pair_sum_r(ll):
    if ll == None:
        return None
    if ll.next == None:
        return None
    part1 = LN(ll.value + ll.next.value)
    part1.next = pair_sum_r(ll.next.next)
    return part1



# Define count RECURSIVELY

def count(t,value):
    total = 0
    if t != None:
        if t.right != None:
            total += count(t.right, value)
        if t.left != None:
            total += count(t.left, value)
        if t.value == value:
            total += 1
    return total



# Define the derived StingVar_WithHistory using the StringVar base class defined in tkinter

from tkinter import StringVar

class StringVar_WithHistory(StringVar):
    def __init__(self):
        self.history = []
        StringVar.__init__(self)
        
        
    def set (self,value):
        if len(self.history) == 0:
            StringVar.set(self, value)
            self.history.append(value)
        else:
            if value != self.history[0]:
                StringVar.set(self, value)
                self.history.insert(0, value)
        
    def undo (self):
        if len(self.history) != 1 and len(self.history) != 0:
            StringVar.set(self, self.history[1])
            del self.history[0]


            
# OptionMenuUndo: acts like an OptionMenu, but also allows undoing the most recently
#   selected option, all the way back to the title (whose selection cannot be undone).
# It overrides the __init__ method and defines the new methods get, undo, and 
#   simulate_selections.
# It will work correctly if StringVar_WithHistory is defined correctly
from tkinter import OptionMenu
class OptionMenuUndo(OptionMenu):
    def __init__(self,parent,title,*option_tuple,**configs):
        self.result = StringVar_WithHistory()
        self.result.set(title)
        OptionMenu.__init__(self,parent,self.result,*option_tuple,**configs)

    # Get the current option  
    def get(self):                
        return self.result.get() # Call get on the StringVar_WithHistory attribute

    # Undo the most recent option
    def undo(self):
        self.result.undo()       # Call undo on the StringVar_WithHistory attribute
      
    # Simulate selecting an option (mostly for test purposes)
    def simulate_selection(self,option):
        self.result.set(option)  # Call set on the StringVar_WithHistory attribute


# Testing Script
def mystery(l):
    while l.next != None and l.next.next != None:
        t1 = l.next
        print ('\nt1 = l.next')
        print ('t1: ' + str_ll(t1))
        t2 = t1.next
        print ('t2 = t1.next')
        print ('t2: ' + str_ll(t2))
        t1.next = t2.next
        print ('t1.next = t2.next')
        print ('t1 : ' + str_ll(t1))
        t2.next = t1
        print ('t2.next = t1')
        print ('t2 : ' + str_ll(t2))
        l.next = t2
        print ('l.next = t2')
        print ('l : ' + str_ll(l))
        l = t1
        print ('l = t1')
        print ('l : ' + str_ll(l))
        print ('\nt1: ' + str_ll(t1))
        print ('t2: ' + str_ll(t2))
        print ('l : ' + str_ll(l))

if __name__ == '__main__':
    #import driver
    #driver.driver()
    x = list_to_ll([3,5,2,4,8,7])
    mystery(x)
    
#===============================================================================
#     print('Testing pair_sum')
#     ll = list_to_ll([])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1,2])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1,2,3,4,5,6,7,8])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1,2,3,4,5,6,7,8,9])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum(ll)))
#     print('original list              = ',str_ll(ll))
#      
#      
#     # Put in your own tests here
#  
#  
#     print('Testing pair_sum_r')
#     ll = list_to_ll([])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum_r(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum_r(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1,2])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum_r(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1,2,3,4,5,6,7,8])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum_r(ll)))
#     print('original list              = ',str_ll(ll))
#      
#     ll = list_to_ll([1,2,3,4,5,6,7,8,9])
#     print('\noriginal list              = ',str_ll(ll))
#     print('resulting list             = ',str_ll(pair_sum_r(ll)))
#     print('original list              = ',str_ll(ll))
#  
#     # Put in your own tests here
#  
#  
#     print('\nTesting count')
#     tree = list_to_tree(None)
#     print('\nfor tree = \n',str_tree(tree))
#     for i in [1]:
#         print('count(tree,'+str(i)+') = ', count(tree,i))
#            
#     tree = list_to_tree([1, [2, None, None], [3, None, None]])
#     print('\nfor tree = \n',str_tree(tree))
#     for i in irange(1,3):
#         print('count(tree,'+str(i)+') = ', count(tree,i))
#            
#     tree = list_to_tree([3, [2, None, [3, None, None]], [1, [3, None, None], None]])
#     print('\nfor tree = \n',str_tree(tree))
#     for i in irange(1,3):
#         print('count(tree,'+str(i)+') = ', count(tree,i))
#            
#     tree = list_to_tree([3, [2, [3, None, [2, None, None]], [3, None, None]], [1, [3, None, None], None]])
#     print('\nfor tree = \n',str_tree(tree))
#     for i in irange(1,3):
#         print('count(tree,'+str(i)+') = ', count(tree,i))
#            
#     # Put in your own tests here
#           
#   
# 
#     print('\nTesting OptionMenuUndo')
#     from tkinter import *
#     print('Simulate using StringVar_WithHistory or build/test actual GUI')
#     if prompt.for_bool('Simulate',default=True):
#         # Needed for obscure reasons: OptionMenu must still be placed in main
#         root = Tk()
#         root.title('Widget Tester')
#         main = Frame(root)
#         
#         # Construct an OptionMenuUndo object for simulation
#         omu = OptionMenuUndo(main, 'Choose Option', 'option1','option2','option3')
#         
#         # Initially its value is 'Choose Option'
#         print(omu.get(), '   should be Choose Option')
#         
#         # Select a new option
#         omu.simulate_selection('option1')
#         print(omu.get(), '         should be option1')
#         
#         # Select a new option
#         omu.simulate_selection('option2')
#         print(omu.get(), '         should be option2')
#         
#         # Select the same option (does nothing)
#         omu.simulate_selection('option2')
#         print(omu.get(), '         should still be option2')
#         
#         # Select a new option
#         omu.simulate_selection('option3')
#         print(omu.get(), '         should be option3')
#          
#         # Undo the last option: from 'option3' -> 'option2'
#         omu.undo()
#         print(omu.get(), '         should go back to option2')
#          
#         # Undo the last option: from 'option2' -> 'option1'
#         omu.undo()
#         print(omu.get(), '         should go back to option1')
#          
#         # Undo the last option: from 'option1' -> 'Choose Option'
#         omu.undo()
#         print(omu.get(), '   should go back to Choose Option')
#          
#         # Cannot undo the first option: does nothing
#         omu.undo()
#         print(omu.get(), '   should still be Choose Option')
# 
#          
#         # Cannot undo the first option: does nothing
#         omu.undo()
#         print(omu.get(), '   should still be Choose Option')
#         
#     else: #Build/Test real widget
# 
#         # #OptionMenuToEntry: with title, linked_entry, and option_tuple
#         # #get is an inherited pull function; put is a push function, pushing
#         # #  the selected option into the linked_entry (replacing what is there)
#         # 
#         root = Tk()
#         root.title('Widget Tester')
#         main = Frame(root)
#         main.pack(side=TOP,anchor=W)
#          
#         omu = OptionMenuUndo(main, 'Choose Option', 'option1','option2','option3')
#         omu.grid(row=1,column=1)
#         omu.config(width = 10)
#          
#         b = Button(main,text='Undo Option',command=omu.undo)
#         b.grid(row=1,column=2)
#          
#         root.mainloop()    
#===============================================================================
