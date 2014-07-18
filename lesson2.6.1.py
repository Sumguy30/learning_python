#!/usr/bin/env python 3.1

fridge={"eggs":10,"milk":10,"cheddar":10,"jack_cheese":10,"ham":10,"pepper":10,"onion":10,"feta_cheese":10,"spinach":10}

class Fridge:
    """This class implements a fridge where ingredients can be
      added and removed individually, or in groups.
      The fridge will retain a count of every ingredient added or removed,
      and will raise an error if a sufficient quantity of an ingredient
      isn't present.
      Methods:
      has(food_name [, quantity]) - checks if the string food_name is in the
  fridge.  Quantity will be set to 1 if you don't specify a number.
      has_various(foods) - checks if enough of every food in the dictionary is in
  the fridge
      add_one(food_name) - adds a single food_name to the fridge
      add_many(food_dict) - adds a whole dictionary filled with food
      get_one(food_name) - takes out a single food_name from the fridge
      get_many(food_dict) - takes out a whole dictionary worth of food.
      get_ingredients(food) - If passed an object that has the __ingredients__
              method, get_many will invoke this to get the list of ingredients.
    """
    def __init__(self, items={}):
        """Optionally pass in an initial dictionary of items"""
        if type(items) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
        self.items = items
        return

    # the docstring and intervening portions of the class would be here, and
    # __add_multi should go afterwards.
    def __add_multi(self, food_name, quantity):
        """
          __add_multi(food_name, quantity) - adds more than one of a
          food item. Returns the number of items added
          This should only be used internally, after the type checking has been
          done"""

        if (not food_name in self.items):
            self.items[food_name] = 0
        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self, food_name):
        """
          add_one(food_name) - adds a single food_name to the fridge
          returns True
          Raises a TypeError if food_name is not a string.
        """
        if type(food_name) != type(""):
            raise TypeError("add_one requires a string, given a %s" % (food_name))
        else:
            self.__add_multi(food_name,1)
        return True

    def add_many(self,food_dict):
        """
          add_many(food_dict) - adds a whole dictionary filled with food as
  keys and
              quantities as values.
          returns a dictionary with the removed food.
          raises a TypeError if food_dict is not a dictionary
          returns False if there is not enough food in the fridge.
        """
        if type(food_dict) != type({}):
            raise TypeError("add_many requires a dictionary, got a %s" % food_dict)

        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return
    
            
    def has(self, food_name, quantity=1):
        """has(food_name, [quantity]) - checks if the string food_name is in the
          fridge.  Quantity defaults to 1
          Returns True if there is enough, False otherwise.
        """

        

def make_omelet_q3 (fridge,omelet_type):
    print(fridge)
    if type(fridge) != type({}):
        raise TypeError("Fridge is not a dictionary")
        return
    elif type(fridge) == type({}):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        if omelet_ingredients == None:
            return None
        fridge = remove_from_fridge(fridge,omelet_ingredients)
        print(fridge)
        return make_food(omelet_ingredients, omelet_type)


    
def remove_from_fridge (fridge,omelet_ingredients):
    for omelet_ingreds in omelet_ingredients.keys():
        if fridge[omelet_ingreds] >= omelet_ingredients[omelet_ingreds]:
            fridge[omelet_ingreds]=fridge[omelet_ingreds]-omelet_ingredients[omelet_ingreds]
        else:
            raise LookupError("not enough %s in fridge" % (omelet_ingreds))
    return fridge

def make_omelet (omelet_type):
    """This will make an omelet.  You can either pass in a dictionary
       that contains all of the ingredients for your omelet, or provide
       a string to select a type of omelet this function already knows
       about"""
    if type(omelet_type) == type({}):
        print("omelet_type is a dictionary with ingredients")
        return make_food(omelet_type, "omelet")
    elif type(omelet_type) == type(""):
        omelet_ingredients = get_omelet_ingredients(omelet_type)
        if omelet_ingredients == None:
            return None
        return make_food(omelet_ingredients, omelet_type)
    else:
        #print("I don't think I can make this kind of omelet: %s" (omelet_type))
        raise TypeError("I don't think I can make this kind of omelet: %s" % (omelet_type))
    

def get_omelet_ingredients(omelet_name):
    """This contains a dictionary of omelet names that can be produced,
   and their ingredients"""
    # All of our omelets need eggs and milk
    ingredients={"eggs":2,"milk":1}
    if omelet_name == "cheese":
        ingredients["cheddar"]=2
    elif omelet_name == "western":
        ingredients["jack_cheese"] = 2
        ingredients["ham"] = 1
        ingredients["pepper"] = 1
        ingredients["onion"] = 1
    elif omelet_name == "greek":
        ingredients["feta_cheese"] = 2
        ingredients["spinach"] = 2
    else:
        print("sorry punk, we don't have that shit!")
        return None
    return ingredients


def make_food(ingredients_needed, food_name):
    """make_food(ingredients_needed, food_name)
       Takes the ingredients from ingredients_needed and makes food_name"""
    for ingredient in ingredients_needed.keys():
        print("Adding %d of %s to make a %s" % (ingredients_needed[ingredient],ingredient, food_name))
    print("Made %s" % (food_name))
    return food_name
