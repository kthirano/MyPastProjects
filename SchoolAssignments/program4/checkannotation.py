# Submitter: nschultz(Schultz-Cox, Neil)
# Partner  : kthirano(Hirano, Kohsuke)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set the name below to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        
        def is_list():
            #print (annot, value)
            mastercheck = check_history
            if type(value) != list:
                raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1])
            if len(annot) == 1 and type(annot[0]) == type:
                for item in value:
                    if isinstance(item, annot[0]) == False:
                        mastercheck += 'list[' + str(value.index(item)) + '] check: ' + str(annot[0])
                        raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1]
                                              + '\n' + mastercheck)
            else:
                if len(annot) > 1:
                    if len(annot) != len(value):
                        raise AssertionError(repr(param) + " failed annotation check(wrong number of elements): value = '" + str(value) + "'\n annotation had " + str(len(annot)) + " elements" + str(annot))
                index = 0
                for x in range(len(value)):
                    if type(annot[0]) != type:
                        temp = mastercheck
                        temp += 'list[' + str(index) + '] check: ' + str(annot[0]) + '\n'
                        self.check(param, annot[0], value[index], temp)
                    elif isinstance(value[index],annot[index]) == False:
                        mastercheck += 'list[' + str(index) + '] check: ' + str(annot[index])
                        raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1]
                                             + "\n" + mastercheck)
                    index += 1                    
                
                
        def is_tuple():
            mastercheck = check_history
            if type(value) != tuple:
                raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1])
            if len(annot) == 1 and type(annot[0]) == type:
                for item in value:
                    if isinstance(item, annot[0]) == False:
                        mastercheck += 'tuple[' + str(value.index(item)) + '] check: ' + str(annot[0])
                        raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1]
                                              + '\n' + mastercheck)
            else:
                if len(annot) > 1:
                    if len(annot) != len(value):
                        raise AssertionError(repr(param) + " failed annotation check(wrong number of elements): value = '" + str(value) + "'\n annotation had " + str(len(annot)) + " elements" + str(annot))
                index = 0
                for x in range(len(value)):
                    if type(annot[0]) != type:
                        temp = mastercheck
                        temp += 'list[' + str(index) + '] check: ' + str(annot[0]) + '\n'
                        self.check(param, annot[0], value[index], temp)
                    elif isinstance(value[index],annot[index]) == False:
                        mastercheck += 'tuple[' + str(index) + '] check: ' + str(annot[index])
                        raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1]
                                             + "\n" + mastercheck)
                    index += 1  
        
        
        def is_dict():
            mastercheck = check_history
            if type(value) != dict:
                raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1])
            if len(annot) > 1:
                raise AssertionError(repr(param) + " annotation inconsistency: dict should have " + str(len(value)) + " item but had " + str(len(annot)) + "\nannotation = " + str(annot))
            annotkey = list(annot.keys())[0]
            annotval = list(annot.values())[0]
            for k, v in value.items():
                if isinstance(k, annotkey) == False:
                    mastercheck += "dict key check: " + str(annotkey)
                    raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(k) + "'\n was type " + str(type(k)).split("'")[1] + " ...should be type " + str(annotkey).split("'")[1] + "\n" + mastercheck)
                if isinstance(v, annotval) == False:
                    mastercheck += "dict value check: " + str(annotval)
                    raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(v) + "'\n was type " + str(type(v)).split("'")[1] + " ...should be type " + str(annotval).split("'")[1] + "\n" + mastercheck)
        
        
        def is_set():
            mastercheck = check_history
            if type(value) != set:
                raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type set")
            if len(annot) > 1:
                raise AssertionError(repr(param) + " annotation inconsistency: set should have " + str(len(value)) + " item but had " + str(len(annot)) + "\nannotation = " + str(annot))
            annotkey = list(annot)[0]
            for k in value:
                if isinstance(k, annotkey) == False:
                    mastercheck += "set value check: " + str(annotkey)
                    raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(v) + "'\n was type " + str(type(v)).split("'")[1] + " ...should be type " + str(annotkey).split("'")[1] + "\n" + mastercheck)
        
        
        def is_frozenset():
            mastercheck = check_history
            if type(value) != frozenset:
                raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type frozenset")
            if len(annot) > 1:
                raise AssertionError(repr(param) + " annotation inconsistency: frozenset should have " + str(len(value)) + " value but had " + str(len(annot)) + "\nannotation = " + str(annot))
            annotkey = list(annot)[0]
            for k in value:
                if isinstance(k, annotkey) == False:
                    mastercheck += "frozenset value check: " + str(annotkey)
                    raise AssertionError(repr(param) + " failed annotation check(wrong type): value = '" + str(v) + "'\n was type " + str(type(v)).split("'")[1] + " ...should be type " + str(annotkey).split("'")[1] + "\n" + mastercheck)

        
        
        def is_lambda(): 
            mastercheck = check_history
            if len(annot.__code__.co_varnames) == 0 or len(annot.__code__.co_varnames) > 1:
                raise AssertionError(repr(param) + " annotation inconsistency: predicate should have " + str(value) + " parameter but had " + str(len(annot.__code__.co_varnames)) + "\npredicate = " + str(annot))
            if type(value) == list:
                for x in value:
                    try:
                        annot(x)
                    except:
                        mastercheck = "list[" + str(value.index(x)) + "]: " + str(annot)
                        raise AssertionError(repr(param) + " failed annotation check: value = " + str(value) + "\npredicate = " + str(annot) + "\n" + mastercheck)
                for x in value:
                    if annot(x) == False:
                        raise AssertionError(repr(param) + " failed annotation check: value = " + str(x) + "\npredicate = " + str(annot))
            else:
                try:
                    annot(value)
                except:
                    raise AssertionError(repr(param) + " failed annotation check: value = " + str(value) + "\npredicate = " + str(annot) + "\n" + mastercheck)
                if annot(value) == False:
                    raise AssertionError(repr(param) + " failed annotation check: value = " + str(value) + "\npredicate = " + str(annot))
    

        def is_object():
            try:
                annot.__check_annotation__
            except AttributeError:
                raise AssertionError
            except AssertionError:
                raise AssertionError
            except:
                raise AssertionError
            
            
        # Decode your annotation here; then check against argument
        if annot == None:
            return None
        elif type(annot) is type:
            if isinstance(value, annot) == False:
                raise AssertionError(str(param) + " failed annotation check(wrong type): value = '" + str(value) + "'\n was type " + str(type(value)).split("'")[1] + " ...should be type " + str(annot).split("'")[1])
        elif isinstance(annot, list):
            is_list()
        elif isinstance(annot, tuple):
            is_tuple()
        elif isinstance(annot, dict):
            is_dict()
        elif isinstance(annot, set):
            is_set()
        elif isinstance(annot, frozenset):
            is_frozenset()
        elif callable(annot):
            is_lambda()
        else:
            is_object()
            
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict: the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        self.param_dict = param_arg_bindings()
        self.annotation_dict = self._f.__annotations__
        
        if self._checking_on == False or Check_Annotation.checking_on == False:
            return self._f(*args, **kargs)
        
        try:
            # Check the annotation for every parameter (if there is one)
            for k, v in self.param_dict.items():
                if k in self.annotation_dict:
                    self.check(k, self.annotation_dict[k], v)
            # Compute/remember the value of the decorated function
            self.returned_value = self._f(*args, **kargs)
            # If 'return' is in the annotation, check it
            if "return" in self.annotation_dict:
                self.param_dict["_return"] = self.returned_value
                self.check("_return", self.annotation_dict["return"], self.returned_value)
            # Return the decorated answer
            return self.returned_value
            #remove after adding real code in try/except
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #===================================================================
            # print(80*'-')
            # for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #     print(l.rstrip())
            # print(80*'-')
            #===================================================================
            raise




  
if __name__ == '__main__':     
    #an example of testing a simple annotation
    #def f(x : [[str]]): pass
    #f = Check_Annotation(f)
    #f([['a','b'],['c','d']])
    #f([['a','b'],[4,'d']])
    #===========================================================================
    # def f(x:int): pass
    # f = Check_Annotation(f)
    # f(3)
    # #f('a')
    #  
    # def f(x : int) -> str: return 0
    # f = Check_Annotation(f)
    # f(2)
    #  
    # def f(x: int, y: int) -> str:
    #     masterstr = ''
    #     for  i in range (x+y):
    #         masterstr += 'b'
    #     return masterstr
    #===========================================================================
    #===========================================================================
    # def f(x : {str : int}): pass
    # f = Check_Annotation(f)
    # f({'a':1,'b':2})
    #===========================================================================
    
    #===========================================================================
    # def f(x : {Check_All_OK(str,lambda x : len(x)<=3):Check_Any_OK(str,int)}): pass
    # print (type(f))
    # f = Check_Annotation(f)
    # f({'a' : 1, 'b': 2, 'c':'c'})Z
    #===========================================================================
    import driver
    driver.default_show_exception=True
    driver.default_show_exception_message=True
    driver.default_show_traceback=True
    driver.driver()
    
