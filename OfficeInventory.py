#!/usr/bin/env python 3.1

class OfficeInventory:
    """ DO I HAVE TO PUT COMMENT"""
    def __init__(self, items={}):
        if type(items) != type({}):
            raise TypeError("Wrong Type Asshole, use a list stupid!")
        self.passeditems=items
        return


    def add_inventory(self,items,quantity=1):
        self.__addremove_inventory(items,True,quantity)        
        return
                  
    def remove_inventory(self,items,quantity=1):
        self.__addremove_inventory(items,False,quantity)
        return
    

    def __addremove_inventory(self,items,addflag,quantity):
        if addflag == True:
            if type(items) == type({}):
                for eachitem in items.keys():
                    self.__add_inv(eachitem,items[eachitem],addflag)
            else:
                self.__add_inv(items,quantity,addflag)
        else:
            if type(items) == type({}):
                for eachitem in items.keys():
                    self.__remove_inv(eachitem,items[eachitem],addflag)
            else:
                self.__remove_inv(items,quantity,addflag)

    def __add_inv(self,item,quantity,addflag):
        # eg: passeditem[paper]=10
        if (not item in self.passeditems):
            self.passeditems[item] = 0
        self.passeditems[item] = self.passeditems[item] + quantity
        self.show_inv(item, quantity, addflag)


    def __remove_inv(self,item,quantity,addflag):
        # eg: passeditem[paper]=10
        if (item in self.passeditems):
            self.passeditems[item] = self.passeditems[item] - quantity
            self.show_inv(item, quantity, addflag)
        else:   
            print("You can't %s because you don't have anymore idiot!" % (item))
    
        
    def show_inv(self,item, quantity, addflag):
        print("Here is current Inventory: %s" % (self.passeditems))
        if addflag == True:
                  print("%d of %s was added to Office Inventory\n" % (quantity, item))
                  print("Here is new Inventory: %s" % (self.passeditems))
        elif addflag == False:
                  print("%d of %s was removed from Office Inventory" % (quantity, item))
                  print("Here is new Inventory: %s" % (self.passeditems))
