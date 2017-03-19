#attempting json to dictionary, dictionary to json
#! python

import json

#http://docs.python-guide.org/en/latest/scenarios/json/
#json.dumps(inserthere) to export to json
#parsed_json = json.loads(json_string)

def get_recipes_json():
    global recipes_old
    with open("recipe_list.txt") as f:
        recipes_old = json.loads(f.read())

def get_restaurants_json():
    global rest_old
    with open("rest_list.txt") as f:
        rest_old = json.loads(f.read())

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
    f = open("recipe_list.txt", "r+")
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


#~~~~~~~~
add_to_recipe_json()
# add_to_rest_json()
