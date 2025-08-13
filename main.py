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
import json

from rich import print
from text_styles import *
from persona_tracks_module import *


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




while True:
    print("\nMenu: (1) Add (2) View (3) Edit (4) Delete (5) Exit")
    choice = enter_numbers("Choose an option: ")

    if choice == 1:
        add_person(data)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print(f"\n{INFO}Thank you for using {SUCCESS}PersonTrack!")
        break
    else:   # Less than 1, more than 5
        print(f"{WARNING}Make sure you enter a valid number for the menu.")

