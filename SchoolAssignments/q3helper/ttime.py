from goody import type_as_str

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        if self.hour > 23 or self.hour < 0 or type(self.hour) != int:
            raise AssertionError(str(self.hour)+" not appropriate hour")
        if self.minute > 59 or self.minute < 0 or type(self.minute) != int:
            raise AssertionError(str(self.minute)+" not appropriate minute")
        if self.second > 59 or self.second < 0 or type(self.second) != int:
            raise AssertionError(str(self.second)+" not appropriate second")
        
    def __getitem__(self, request):
        output = []
        length = 0
        if type(request) == int:
            length = 1
        else:
            length = len(request)
        for x in range(length):
            rq = 0
            if type(request) == int:
                rq = request
            else:
                rq = request[x]
            if rq == 1:
                output.append(self.hour)
            elif rq == 2:
                output.append(self.minute)
            elif rq == 3:
                output.append(self.second)
            else:
                raise IndexError(str(rq) + " not a valid input")
        if len(output) == 1:
            return output[0]
        else:
            return tuple(output)
    
    def __repr__(self):
        return "Time({},{},{})".format(self.hour, self.minute, self.second)
    
    def __str__(self):
        def truestr(x: int) -> str:
            if x < 10:
                return str(0) + str(x)
            else:
                return str(x)
        ampm = "am"
        true_hour = self.hour
        if self.hour >= 12:
            ampm = "pm"
            if self.hour > 12:
                true_hour = self.hour - 12
        if self.hour == 0:
            true_hour = 12
        return "{}:{}:{}".format(true_hour, truestr(self.minute), truestr(self.second)) + ampm
        
    def __bool__(self):
        if self.hour == 0 and self.minute == 0 and self.second == 0:
            return False
        else:
            return True
    
    def __len__(self):
        return self.hour * 3600 + self.minute * 60 + self.second
    
    def __eq__(self, otherTime):
        if type(otherTime) != Time:
            return False
        elif len(self) == len(otherTime):
            return True
        else:
            return False
        
    def __lt__(self, otherTime):
        if type(otherTime) == Time:
            if len(self) < len(otherTime):
                return True
            else:
                return False
        elif type(otherTime) == int:
            if len(self) < otherTime:
                return True
            else:
                return False
        else:
            raise TypeError
    
    def __add__(self, someTime):
        if type(someTime) != int:
            raise TypeError(str(someTime) +" not an int")
        newT = Time(self.hour, self.minute, self.second)
        for onesec in range(someTime):
            newT.second += 1
            if newT.second == 60:
                newT.minute += 1
                newT.second = 0
            if newT.minute == 60:
                newT.hour += 1
                newT.minute = 0
            if newT.hour == 24:
                newT.hour = 0
        return newT
    def __radd__(self, someTime):
        if type(someTime) != int:
            raise TypeError(str(someTime) +" not an int")
        newT = Time(self.hour, self.minute, self.second)
        for onesec in range(someTime):
            newT.second += 1
            if newT.second == 60:
                newT.minute += 1
                newT.second = 0
            if newT.minute == 60:
                newT.hour += 1
                newT.minute = 0
            if newT.hour == 24:
                newT.hour = 0
        return newT
    
    def __call__(self, hour, minute, second):
        if hour > 23 or hour < 0 or type(hour) != int:
            raise AssertionError(str(self.hour)+" not appropriate hour")
        if minute > 59 or minute < 0 or type(minute) != int:
            raise AssertionError(str(self.minute)+" not appropriate minute")
        if second > 59 or second < 0 or type(second) != int:
            raise AssertionError(str(self.second)+" not appropriate second")
        
        self.hour = hour
        self.minute = minute
        self.second = second
        




if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Time before doing bsc tests

    print('Start simple testing')
    t = Time()

    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback =True
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
    driver.driver()



        
        
        
        
        
