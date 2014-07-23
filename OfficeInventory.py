#!/usr/bin/env python 3.1

class OfficeInventory:
    """ DO I HAVE TO PUT COMMENT"""
    def __init__(self, items={}):
        if type(items) != type({}):
            raise TypeError("Wrong Type Asshole, use a list stupid!")
        self.passeditems = items
        return


    def add_inventory(self,items,quantity=1):
        self.__addremove_inventory(items,"addinv",quantity)        
        return
                  
    def remove_inventory(self,items,quantity=1):
        self.__addremove_inventory(items,"removeinv",quantity)
        return
    

    def __addremove_inventory(self,items,addflag,quantity):
        if addflag == "addinv":
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
        self.__show_inv(item, quantity, addflag)


    def __remove_inv(self,item,quantity,addflag):
        # eg: passeditem[paper]=10
        if (item in self.passeditems):
            self.passeditems[item] = self.passeditems[item] - quantity
            if self.passeditems[item] < 0:
                self.passeditems[item] = 0
            self.__show_inv(item, quantity, addflag)
        else:   
            print("You can't remove %s because you never had idiot!" % (item))
    
        
    def __show_inv(self,item, quantity, addflag):
        if addflag == "addinv":
                  print("%d of %s was added to Office Inventory\n" % (quantity, item))
                  self.show_inventory()
        else:
                  print("%d of %s was removed from Office Inventory" % (quantity, item))
                  self.show_inventory()

    def show_inventory(self):
        print("Here is the current Inventory")
        for items in self.passeditems.keys():
                print("Item: %s   Quantity: %d" % (items, self.passeditems[items]))




class HomeWork:
    """ Creates Homework"""
    def __init__(self,subject="math"):
        self.__set_subject(subject)
        return

    def __set_subject(self, subject):
        if subject == "math":
            return {"paper":2,"pen":1}
        elif subject == "online gaming":
            return {"computer":1,"mouse":1}
        elif subject == "art":
            return {"paper":1,"ruler":1}
        else:
            return False

    def get_inventory_from_office(self,OffInvObj,subject):
        subjectrequirements = self.__set_subject(subject)
        for item in subjectrequirements.keys():
            OffInvObj.remove_inventory(item,subjectrequirements[item])
        OffInvObj.show_inventory



    
