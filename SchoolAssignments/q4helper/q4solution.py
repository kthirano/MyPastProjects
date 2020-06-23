from predicate import is_prime

# primes is used to test code you write below
def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1
         
# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file; add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v



def running_count(iterable,p):
    count = 0
    for x in iterable:
        if p(x)== True:
            count += 1
        yield count

        
            
def stop_when(iterable,p):
    masterstr = ''
    for x in iterable:
        if p(x) == True:
            return masterstr
        masterstr += str(x)



def yield_and_skip(iterable):
    masterlist = []
    reflist = list(iterable)
    x = 0
    while x < len(reflist):
        if type(reflist[x]) == int:
            masterlist.append(reflist[x])
            x += reflist[x]
        else:
            masterlist.append(reflist[x])
        x += 1
    return masterlist



def windows(iterable,n,m=1):
    reflist = list(iterable)
    onindex = 0
    makelist = []
    while onindex + (n-m) <= len(reflist):
        makelist.append(reflist[onindex])
        onindex += 1
        if len(makelist) == n:
            yield makelist
            makelist = []
            onindex -= (n - m)
        
            

def alternate(*iterables):
    refiterables = []
    for x in iterables:
        refiterables.append(list(x))
    masterlist = []
    madechanges = True
    onindex = 0
    while madechanges == True:
        madechanges = False
        for eachiter in refiterables:
            if onindex < len(eachiter):
                masterlist.append(eachiter[onindex])
                madechanges = True
            else:
                return masterlist
        onindex += 1
    return masterlist



def myzip(*iterables):
    refiterables = []
    for x in iterables:
        refiterables.append(list(x))
    mastertuple = list()
    onindex = 0
    madechanges = True
    while madechanges == True:
        madechanges = False
        for eachiter in refiterables:
            if onindex < len(eachiter):
                mastertuple.append(eachiter[onindex])
                madechanges = True
            else:
                mastertuple.append(None)
        onindex += 1
        if madechanges == True:
            yield tuple(mastertuple)
            mastertuple = list()



class Ordered:
    def __init__(self, startset):
        self.myset = startset
    
    def __iter__(self):
        def relevant(x, y):
            for values in x:
                if values not in y:
                    return False
            return True
        
        alreadyminned = []
        while len(alreadyminned) != len(self.myset) or relevant(alreadyminned, self.myset) == False:
            for values in alreadyminned:
                if values not in self.myset:
                    alreadyminned.remove(values)
            if len(alreadyminned) == 0:
                x = min(self.myset)
            else:
                x = min([element for element in self.myset if element > max(alreadyminned)])
            alreadyminned.append(x)
            yield x
            
                



if __name__ == '__main__':
   
    
    # Test running_count; you can add your own test cases
    print('\nTesting running_count')
    for i in running_count('bananastand',lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
     
    for i in running_count(hide('bananastand'),lambda x : x in 'aeiou'): # is vowel
        print(i,end=' ')
    print()
     
     
    # Test stop_when; you can add your own test cases
    print('\nTesting stop_when')
    for c in stop_when('abcdefghijk', lambda x : x >='d'):
        print(c,end='')
    print()
 
    for c in stop_when(hide('abcdefghijk'), lambda x : x >='d'):
        print(c,end='')
    print('\n')
 
    # Test group_when; you can add your own test cases
    print('\nTesting yield_and_skip')
    for i in yield_and_skip([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2]):
        print(i,end=' ')
    print()
     
    for i in yield_and_skip(hide([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2])):
        print(i,end=' ')
    print()
 
  
    # Test windows; you can add your own test cases
    print('\nTesting windows')
    for i in windows('abcdefghijk',4,2):
        print(i,end=' ')
    print()
      
    print('\nTesting windows on hidden')
    for i in windows(hide('abcdefghijk'),4,2):
        print(i,end=' ')
    print()
  
   
    # Test alternate; add your own test cases
    print('\nTesting alternate')
    for i in alternate('abcde','fg','hijk'):
        print(i,end='')
    print()
          
    for i in alternate(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
          
    for i in alternate(primes(20), hide('fghi'),hide('jk')):
        print(i,end='')
    print()
   
   
    # Test myzip; add your own test cases
    print('\nTesting myzip')
    for i in myzip('abcde','fg','hijk'):
        print(i,end='')
    print()
           
    for i in myzip(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print()
           
    for i in myzip(primes(20), hide('fghi'),hide('jk')):
        print(i,end='')
    print('\n')
          
       
          
        
    # Test Ordered; add your own test cases
    print('\nTesting Ordered')
    s = {1, 2, 4, 8, 16}
    i = iter(Ordered(s))
    print(next(i))
    print(next(i))
    s.remove(8)
    print(next(i))
    print(next(i))
    s.add(32)
    print(next(i))
    print()
       
    s = {1, 2, 4, 8, 16}
    i = iter(Ordered(s))
    print([next(i), next(i), s.remove(8), next(i), next(i), s.add(32), next(i)])
        
    s = {1, 2, 4, 8}
    for v in Ordered(s):
        s.discard(8)
        s.add(10)
        print(v) 
    print('\n')
    
    s = {1, 2, 4, 16}
    i = iter(Ordered(s))
    print ([next(i), s.remove(2), next(i), s.remove(4), next(i)])
    print ()
    s = {1, 2, 4, 8, 16}
    i = iter(Ordered(s))
    print ([next(i), s.remove(2), next(i), s.remove(4), s.remove(8), next(i)])
      
         
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
