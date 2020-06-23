from collections import defaultdict


class History:
    def __init__(self):
        self.records = defaultdict(list)
    
    def __getattr__(self,name):
        prevcount = name.count('_prev')
        if prevcount == 0:
            raise NameError("does not contain _prev")
        attributename = name.split('_')[0]
        if attributename not in self.records:
            raise NameError("attribute " + attributename + " not found")
        if prevcount >= len(self.records[attributename]):
            return None
        else:
            templist = self.records[attributename]
            return templist[prevcount]


    def __getitem__(self,index):
        if index > 0:
            raise IndexError("index cannot be positive")
        final_dict = dict()
        for key in self.records:
            tempname = str(key)
            for x in range(index * -1):
                tempname+='_prev'
            if (index != 0):
                final_dict[key] = self.__getattr__(tempname)
            else:
                templist = self.records[key]
                final_dict[key] = templist[0]
        return final_dict

    
    def __setattr__(self,name,value):
        if "_prev" in name:
            raise NameError("cannot contain _prev")
        else:
            if 'records' in self.__dict__:
                self.records[name].insert(0,value)
            self.__dict__[name] = value
            





if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test History before doing bsc tests

    print('Start simple testing')


    
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_traceback =True
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
    driver.driver()
