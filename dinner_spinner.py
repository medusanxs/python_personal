#! python
from collections import defaultdict
import random

#def clear_current_restaurants():
    #with open('rest_list.txt') as f:

#def clear_current_recipes():
    #with open('recipe_list.txt')as f:


def get_current_restlist():
    with open("rest_list.txt") as f:
        global rest_list
        rest_list = defaultdict(list)
        for line in f:
            name, site_url = line.strip().split()
            rest_list[name].append(site_url)

def get_current_recipelist():
    with open("recipe_list.txt") as f:
        global recipe_list
        recipe_list = defaultdict(list)
        for line in f:
            name, recipe = line.strip().split()
            recipe_list[name].append(recipe)

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
    get_current_recipelist()
    get_current_restlist()
    global z
    z = rest_list.copy()
    z.update(recipe_list)
    #for key in z.keys():
        #print key

def add_recipe():
    new_name = raw_input("Name: ")
    new_recipe = raw_input("Recipe URL: ")
    with open("recipe_list.txt", "a") as f:
        x = new_name
        y = new_recipe
        f.write(x + ' ' + y)
    #recipe_list.update({x : y})

def add_restaurant():
    new_name = raw_input("Name: ")
    new_menu = raw_input("Menu URL: ")
    with open("rest_list.txt", "a") as f:
        x = new_name
        y = new_menu
        f.write(x + ' ' + y)
    #rest_list.update({x : y})


#add food to the dictionaries:
def get_food_adds():
    type_food =  raw_input("Restaurant or Recipe? ")
    if type_food == "Restaurant" or type_food == "restaurant":
        add_restaurant()
    elif type_food == "Recipe" or type_food == "recipe":
        add_recipe()
    else:
        print "Please choose 'restaurant' or 'recipe'"

def get_random_food():
    combine_lists()
    x = random.randint(0, len(rest_list) + len(recipe_list))
    for x in z:
        print x, z[x]

#~~~~~~~~CODE~~~~~~~~~~~

get_current_restlist()
get_current_recipelist()
get_food_adds()
print recipe_list
print rest_list
print "Recipes: ",
all_recipes()
print "Restaurants: ",
all_restaurants()
print "Combined list: ",
combine_lists()
print "Rando Calrithean picks this for dinner: ",
get_random_food()
