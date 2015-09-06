# http://soundjax.com/beep-1.html
# structure the class
# define what the cla<ss does
# add comments
#

# add to string - complexity
# impr:
#   same ingredient twice
#   keeping sorted the steps

# ---------------------------------------------------------------
# Imports
# ---------------------------------------------------------------

from datetime import datetime, timedelta
import time
import pygame

# ---------------------------------------------------------------
# Class - RecipeStep
# ---------------------------------------------------------------


class RecipeStep:
    """One step in a recipe.

    Is defined by the time-offset (in minutes) from the start of cooking when we want to do it and the instruction
    """
    # ---------------------------------------------------------------
    # Initialisation
    # ---------------------------------------------------------------

    def __init__(self, instruction, time_offset_min):
        """Creates a new recipe-step

        Includes the instruction what to do and the time-offset from the start of the recipe"""
        self.time_offset_min = time_offset_min
        self.instruction = instruction

    # ---------------------------------------------------------------
    # Interface
    # ---------------------------------------------------------------

    def get_string(self, recipe_start_time):
        """Gets the string representing the step.

        The time when it should be carried out (computed by the recipe start time) and the instruction
        """
        return str((recipe_start_time + timedelta(0, 60*self.time_offset_min)).time()) + ": " + self.instruction

    def __str__(self):
        return "After " + str(self.time_offset_min) + " minutes, " + self.instruction

# ---------------------------------------------------------------
# Class - Recipe
# ---------------------------------------------------------------


class Recipe:
    """Cooking recipe.

    Is basically a set of ingredients (with their quantities) and a list of steps to carry out during cooking
    """
    # ---------------------------------------------------------------
    # Constants
    # ---------------------------------------------------------------

    QUANTITY = 'quantity'
    MEASURE = 'measure'

    # ---------------------------------------------------------------
    # Initialisation - how do we construct one
    # ---------------------------------------------------------------

    def __init__(self, name):
        """Construct an empty recipe (containing no ingredients of steps to carry out)"""
        self.name = name
        self.steps = []
        self.ingredients = {}

    # ---------------------------------------------------------------
    # Interface - what functionality is offered
    # ---------------------------------------------------------------

    def add_ingredient(self, ingredient, quantity=1, measure="pieces"):
        """Adds some quantity of the ingredient to the recipe"""
        if ingredient in self.ingredients:
            self.ingredients[ingredient][self.QUANTITY] += quantity
        else:
            self.ingredients[ingredient] = {self.QUANTITY: quantity, self.MEASURE: measure}

    def print_ingredients(self):
        """Prints the ingredients of the recipe"""
        print(self.get_ingredients_str())

    def add_step(self, recipe_step):
        """Adds another cooking step to the recipe"""
        self.steps.append(recipe_step)

    def print_steps(self):
        """Prints the steps of the recipe"""
        print(self.get_steps_str())

    def print_recipe(self):
        """Prints the whole recipe"""
        print("Recipe for " + self.name)
        print(str(self))
        print()

    def run_recipe(self):
        """Runs the recipe

        Prints the ingredients and then the individual steps one by one, when their time comes
        """
        self.print_ingredients()

        self.__sort_steps_by_time()
        recipe_start_time = datetime.now()
        print("Making " + self.name + ". Started at " + str(recipe_start_time.time()))

        for i in range(len(self.steps)):
            pygame.mixer.music.play()
            print(str(i + 1) + ": " + self.steps[i].get_string(recipe_start_time))
            if i != len(self.steps) - 1:
                print("\tNext step at " + self.steps[i + 1].get_string(recipe_start_time))
                time.sleep(self.steps[i + 1].time_offset_min - self.steps[i].time_offset_min)
            else:
                print("\tThis is the last step, don't screw it!")

        print("Should be ready now, enjoy :-)")

    # ---------------------------------------------------------------
    # Implementation
    # ---------------------------------------------------------------

    def __str__(self):
        return self.get_ingredients_str() + "\n" + self.get_steps_str()

    def get_steps_str(self):
        """Returns the string with the steps of the recipe"""
        self.__sort_steps_by_time()
        steps_str = "Steps for " + self.name + ":\n"
        for step in self.steps:
            steps_str += "\t" + str(step) + "\n"

        return steps_str

    def get_ingredients_str(self):
        """Returns the string with the ingredients of the recipe"""
        ingredients_str = "Ingredients for " + self.name + ":\n"
        for ingredient in self.ingredients:
            ingredients_str += "\t" + str(ingredient) + "\n"

        return ingredients_str

    def __sort_steps_by_time(self):
        """Sorts the steps of the recipe by the time when they should be carried out"""
        self.steps.sort(key=lambda step: step.time_offset_min)

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.music.load("beep.mp3")

    smoothie = Recipe("Smoothie")
    smoothie.add_ingredient("mango")
    smoothie.add_ingredient("banana")
    smoothie.add_ingredient("ground coconut", 2, "soup spoons")
    smoothie.add_ingredient("milk", 1, "dl")

    smoothie.add_step(RecipeStep("Peel mango and cut to pieces", 0))
    smoothie.add_step(RecipeStep("Peel bananas and cut to pieces", 1))
    smoothie.add_step(RecipeStep("Add everything to the mixer, with milk and coconut", 2))
    smoothie.add_step(RecipeStep("Mix for 120 seconds", 3))
    smoothie.add_step(RecipeStep("Drink", 5))

    print(smoothie)
    smoothie.run_recipe()