 # Garage
    This is a simple Python script for managing a list of cars.
    All CRUD actions are available.
    The data is saved to and loaded back up or each iteration.
    Getting started
    After cloning the project make sure to set up venv, and download the requirements.

 # Functions
    load_data_from_file: Loads car data from data.json into the global cars list.
    manu: Prints the available actions.
    validate_user_selection: Validates the user's selection and returns the corresponding action.
    show_all_cars: Displays all cars in the list.
    add: Adds a new car to the list.
    upd_cars: Updates the details of an existing car.
    del_cars: Deletes a car from the list.
    info_all_cars: Displays the total cars at  garage at that moment.
    delete_all_data: Clears all car data after user confirmation.
    close_program: Saves the car list to 'data.json' and exits the program.

# data structure:
cars = { 'color': 'green', 'ownersname': 'Jimmy', 'brand': 'Land Rover', 'model': 'Series IIA', 'year': 1965 }


# data base:
cars = []

# program actions:
    action(Enum):
        SHOW_ALL = 1
        ADD = 2
        DELETE = 3
        UPDATE = 4
        DELETE_ALL_DATA = 5
        INFO = 6
        EXIT = 7



