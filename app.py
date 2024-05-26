from icecream import ic
from enum import Enum
from print_color import print
import json

"""
data structure
cars = { 'color': 'green', 'ownersname': 'Jimmy', 'brand': 'Land Rover', 'model': 'Series IIA', 'year': 1965 }

"""

cars = list([{ 'color': 'red', 'ownersname': 'Jonsnow', 'brand': 'Ferari', 'model': '911', 'year': 1999 },{ 'color': 'green', 'ownersname': 'Jimmy', 'brand': 'Land Rover', 'model': 'Series IIA', 'year': 2010 }])

# [{ 'color': 'green', 'ownersname': 'Jimmy', 'brand': 'Land Rover', 'model': 'Series IIA', 'year': 1965}]

# class syntax
class Actions(Enum):
    SHOW_ALL = 1
    ADD = 2
    DELETE = 3
    UPDATE = 4
    DELETE_ALL_DATA = 5
    INFO = 6
    EXIT = 7

# Function to load data from the JSON file
def load_data_from_file():
    global cars
    try:
        with open('data.json', 'r') as file:
            cars = json.load(file)
        print("Data loaded successfully!", color='green')
    except FileNotFoundError:
        print("data.json file not found. Starting with an empty list.", color='red')
    except json.JSONDecodeError:
        print("Error decoding JSON from data.json. Starting with an empty list.", color='red')



def manu():
    for action in Actions: print(f'{action.value} - {action.name}' ,color='blue' )
    return Actions( int(input("Enter your selection:")))   



def show_all_cars():
    for index,car in enumerate(cars):
        print(f'({index}){car['color']} - {car['ownersname']} - {car['brand']} - {car['model']} - {car['year']}',color='yellow')



def add():
    cars.append({ 'color': input("car color?"), 'ownersname': input("owner name?"), 'brand': input("car brand"), 'model': input("car model"), 'year':input("car year")})



def upd_cars():
     victim = find_car()
     cars[victim]={ 'color': input("car color?:"), 'ownersname': input("owner name?:"), 'brand': input("car brand:"), 'model': input("car model:"), 'year':input("car year:")}



def del_cars():
    victim = find_car()
    print("Car was deleted successfully", color='red')
    cars.pop(victim)



def find_car():
    show_all_cars()
    victim=int(input("select number from the list of the car that Yoy wish to UPD "))
    print(f'{cars[victim]} car detalis deleted from the list',color='magenta')
    return victim



def del_all_data():
     print("This action will clear all the data. Do you wish to proceed", color='red')
     while True:
        confirmation = input("please enter y/n: ")
        if confirmation.lower() == 'y':
            global cars
            with open('data.json', 'w') as file:
                json.dump([], file)
            cars = []
            print("All cars data was cleared sucssesfuluy.", color='red')
            break
        elif confirmation.lower() == 'n':
            print("Data was not deleted", color='green')
            break
        else:
            print("input invalid", color='red')



def info_all_cars():
    print(f'there are {len(cars)} cars in the garage at this moment', color='green')



def close_program():
    with open('data.json', 'w') as file:
        json.dump(cars, file, indent=4)
    print("All changes are saved Goodbay!", color='green')
    exit()    


if __name__ =="__main__":
    load_data_from_file()
    while True:
     user_selection=manu()
     if user_selection == Actions.EXIT: close_program()
     if user_selection == Actions.SHOW_ALL: show_all_cars()
     if user_selection == Actions.ADD: add()
     if user_selection == Actions.DELETE: del_cars()
     if user_selection == Actions.UPDATE: upd_cars()
     if user_selection == Actions.DELETE_ALL_DATA: del_all_data()
     if user_selection == Actions.INFO: info_all_cars()
