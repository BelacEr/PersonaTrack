u"""
Functions to be created:
enter_numbers() ➜ Make sure the data input is an integer

load_data() ➜ Reads databas.json and returns a Python list.

save_data(data) ➜  Saves the update list back to database.json.

add_person() ➜ Prompts user for details and returns a new person dict.

display_person(person) ➜  Prints a formatted view of a person's data.

list_people(people) ➜ Shows a summary (e.g, IDs + full names) of all  entries.

find_by_id(people_id) ➜ Searches for a person by ID; returns NOne if not found

edit_person(person) ➜  Let's the uses modify fields of an existing entry.

delete_person(people, id) ➜ Removes a person from the list.

"""
from rich import print
from rich.prompt import Prompt
from text_styles import *
import json

data = []


def get_next_id(data):
    return max(p['id'] for p in data) + 1 if data else 1

def enter_numbers(message):
    while True:
        try:
            return int(ask(message))
        except ValueError:
            print("Enter only valid numbers")

def add_person(data):
    # Collect user input.
    first_name = ask("First name: ").strip()
    middle_name = ask("Midddle name: ").strip()
    last_name = ask("Last name: ").strip()
    age = enter_numbers("Age: ")
    languages = ask("Languages: ").split(',')    # NEED TO CHANGE
    country = ask("Country: ").strip()
    city = ask("City: ").strip()
    phone_number = ask("Phone number: ")    # NEED TO CHANGE
   
    # Email validation.
    while True:
        email = ask("Email: ").strip()
        if "@" in email and "." in email.split("@")[-1]:
            break
        print(f"{ERROR}Invalid email (must contain '@' and domain)")


    # Initialize social_media as dictionary
    social_media = {}
    while True:
        platform = ask("Social media (or leave blank to stop): ").strip()
        if not platform:
            break
        username = ask(f"Username for {platform}: ").strip()
        social_media[platform] = username

    new_person = {
            "id": get_next_id(data),
            "First name": first_name,
            "Middle name": middle_name,
            "Last name": last_name,
            "Age": age,
            "Languages": languages,     # NEED TO CHANGE
            "Country": country,    
            "City": city,
            "Social media": social_media,   # NEED TO CHANGE
            "Phone number": phone_number,
            "Email": email,
            }

    data.append(new_person) # Add to in-memory list.
    save_data(data)         # Persist to JSON
    print("✅ Person added and saved.")


def save_data(data):
    if not isinstance(data, (list, dict)):  # Basic validation
        raise ValueError("Data must be a list or dictionary.")
    with open("database.json", "w") as file:
        json.dump(data, file, indent=2)

def load_data():
    try:
        with open("database.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file is missing or invalid

if __name__ == '__main__':
    add_person(data)
