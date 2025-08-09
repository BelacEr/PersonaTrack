"""
Functions to be created:
load_data() ➜ Reads databas.json and returns a Python list.

save_data(data) ➜  Saves the update list back to database.json.

add_person() ➜ Prompts user for details and returns a new person dict.

display_person(person) ➜  Prints a formatted view of a person's data.

list_people(people) ➜ Shows a summary (e.g, IDs + full names) of all  entries.

find_by_id(people_id) ➜ Searches for a person by ID; returns NOne if not found

edit_person(person) ➜  Let's the uses modify fields of an existing entry.

delete_person(people, id) ➜ Removes a person from the list.

"""

data = [
  {
    "id": 1,
    "first_name": "Alex",
    "middle_name": "James",
    "last_name": "Smith",
    "age": 30,
    "languages": ["English", "Spanish"],
    "country": "USA",
    "city": "New York",
    "social_media": {
      "twitter": "@alex_smith",
      "linkedin": "alex-smith"
    }
  }
]


import json

def enter_numbers(message):
    while True:
        try:
            return int(input(message))
            
        except ValueError:
            print("Enter only valid numbers")

def add_person():
    first_name = input("First name: ")
    middle_name = input("Midddle name: ")
    last_name = input("Last name: ")
    age = enter_numbers("Age: ")
    languages = input("Languages: ")    # NEED TO CHANGE
    country = input("Country: ")
    city = input("City: ")
    social_media = input("Social media: ")      # NEED TO CHANGE

    new_person = {
            "First name": first_name,
            "Middle name"; middle_name,
            "Last name": last_name,
            "Age": age,
            "Languages": languages,     # NEED TO CHANGE
            "Country": country,    
            "City": city,
            "Social media": social_media,   # NEED TO CHANGE
            }



def create_data(data):      # create database.json for the first time
    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    try:
        with open("database.json", "r") as file:
            return json.load(file)  # Returns a list.
    except FileNotFoundError:
        return []   # Emtpy list if file doesn't exist

def save_data(data):
    with open("database.json", "w") as file:
        json.dump(data, file, indent=2)    # indent for readibility.

if __name__ == '__main__':
    create_data(data)
    add_person()

