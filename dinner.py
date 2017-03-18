#! /usr/local/python
import random


#~~~GLOBAL VARIABLES ~~~
#list of acceptable foods:
#list_of_food = []

#I think adding a dictionary for food:recipe or restuarant:menu would be best here
#add food dictionary:
#add_food = raw_input("What food would you like to add?")

#separate food into appropriate sections/lists:
#type_food = raw_input("Is this a recipe or a restaurant?")

#Name of item/restaurant:
#name_food = raw_input("What is the name of the recipe/restaurant?")

#URL/recipe:
#recipe_food = raw_input("What is the recipe or URL of the menu?")

#dictionaries of foods : recipes/URL:
rest_list = {}
recipe_list = {}

#combined dictionary (python 3):
#combined_list = {**rest_list, **home_list}



#~~~Functions~~~~~

#print out all restaurants:
def all_restaurants():
    for key in rest_list.keys():
        print key

#print out all recipes:
def all_recipes():
    for key in recipe_list.keys():
        print key

#combined dictionary (python 2):
def combine_lists():
    z = rest_list.copy()
    z.update(recipe_list)
    for key in z.keys():
        print key
#get entire list of foods:
#def get_list():
#    x = random.randint(0, len(list_of_food) - 1)
#    print list_of_food[x]

#add food to list of foods:
#def add_food():
#    list_of_food.append(raw_input("What food would you like to add?"))

#new_name = raw_input("Name: ")
#new_recipe = raw_input("Recipe URL: ")

def add_recipe():
    new_name = raw_input("Name: ")
    new_recipe = raw_input("Recipe URL: ")
    x = "'" + new_name + "'"
    y = new_recipe
    recipe_list.update({x : y})

def add_restaurant():
    new_name = raw_input("Name: ")
    new_menu = raw_input("Menu URL: ")
    x = "'" + new_name + "'"
    y = new_menu
    rest_list.update({x : y})


#add food to the dictionaries:
def get_food_adds():
    type_food =  raw_input("Restaurant or Recipe? ")
    if type_food == "Restaurant" or type_food == "restaurant":
        add_restaurant()
    elif type_food == "Recipe" or type_food == "recipe":
        add_recipe()
    else:
        print "Please choose 'restaurant' or 'recipe'"


#~~~~~~~~CODE~~~~~~~~~~~
get_food_adds()
print recipe_list
print rest_list
print "Recipes: ",
all_recipes()
print "Restaurants: ",
all_restaurants()
print "Combined list: ",
combine_lists()
