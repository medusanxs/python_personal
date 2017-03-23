#Revision of dinner spinner -
# including json
#~~~~~~Imports~~~~~~

import json
import random


#~~~~~~Functions~~~~~~

def get_recipes_json():
    global recipes_old
    with open("recipe_list.txt", "r+") as f:
        try:
            recipes_old = json.load(f)
        except ValueError as e:
            recipes_old = {}

def get_restaurants_json():
    global rest_old
    with open("rest_list.txt", "r+") as f:
        try:
            rest_old = json.load(f)
        except ValueError as e:
            rest_old = {}


Imports into dict from file, if empty - creates empty dict, appends, then outputs to file:
def add_to_rest_json():
    global rest_list
    with open("rest_list.txt", "r+") as f:
        try:
            rest_list = json.load(f)
        except ValueError as e:
            rest_list = {}
        print "Add Restaurant!"
        new_name = raw_input("Name: ")
        new_url = raw_input("Menu URL: ")
        x = new_name
        y = new_url
        f.seek(0)
        rest_list[x] = y
        f.write(json.dumps(rest_list))

def add_to_recipe_json():
    global recipe_list
    with open("recipe_list.txt", "r+") as f:
        try:
            recipe_list = json.load(f)
        except ValueError as e:
            recipe_list = {}
        print "Add Recipe!"
        new_name = raw_input("Name: ")
        new_url = raw_input("Recipe URL: ")
        x = new_name
        y = new_url
        recipe_list[x] = y
        f.seek(0)
        f.write(json.dumps(recipe_list))

#Print the Restaurant options when requested
def show_restold():
    for i in rest_old.keys():
        print i

#Print the Recipe options when requested
def show_recipeold():
    for i in recipes_old.keys():
        print i





#~~~~~~~~~CODE~~~~~~~~
