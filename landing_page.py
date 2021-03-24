import json
import os

from home_page import *

def main():
    """This program shall always run when user first executes the application"""
    while (True):
        print("Welcome to FiMan, a Financial Manager Software Application")

        # Load data from profiles.json
        there_are_existing_profiles, loaded_profiles = load_existing_profiles()

        # "Landing Page"
        valid_input = False
        while valid_input == False:
            print("Type 1 to register a new profile")
            print("Type 2 to open an existing profile")
            print("Type 3 to exit program")
            user_choice = input("")
            print("You selected", user_choice, "\n")
            if (user_choice == "1"):  # Register new profile
                valid_input = True
                list_of_information = register_new_profile()  # User will go through registration, then their info is stored in list_of_information
                write_new_profile_data_to_file(there_are_existing_profiles, loaded_profiles, list_of_information)
                print("New Profile Registered Successfully! Name:", list_of_information[0], "- Features:",
                      list_of_information[1], "- Total Wealth:", list_of_information[2],
                      "- Budget:", list_of_information[3])
                valid_input = False

                # This resolved a bug i encountered when creating the very first profile, then trying to login to it right away gave an error
                there_are_existing_profiles, loaded_profiles = load_existing_profiles()

            elif (user_choice == "2"):  # Go to existing profile

                if (os.stat("profiles.json").st_size == 0):
                    print("There are no existing profiles. Please register a profile.")
                else:
                    valid_input = True
                    for i in range(len(loaded_profiles["profiles"])):
                        print(i, loaded_profiles["profiles"][i]["name"])
                    print("")
                    while(True):
                        chosenProfile = int(input("Please enter in the number of your profile: "))
                        if (chosenProfile < 0) or (chosenProfile >= len(loaded_profiles["profiles"])):
                            print("Invalid input. Please select again")
                        else:
                            user_name = loaded_profiles["profiles"][chosenProfile]["name"]
                            user_features = loaded_profiles["profiles"][chosenProfile]["features"]
                            user_wealth = loaded_profiles["profiles"][chosenProfile]["total_wealth"]
                            user_budget = loaded_profiles["profiles"][chosenProfile]["budget"]
                            break

                    print("Successfully logged into " + user_name + "!")
                    profile = [chosenProfile, user_name, user_features, user_wealth, user_budget] #Pack the chosen profile's data into a list to send to the home page
                    print("Now loading home page\n")
                    run_home_page(profile)

            elif (user_choice == "3"): # Exit program
                valid_input = True
                print("Exiting program...")
                exit(0)
            elif (user_choice == "debug"): # I can test stuff in here
                test_name = input("Enter a username and I will check if it exists")
                found_username = False
                for i in range(len(loaded_profiles["profiles"])):
                    if (loaded_profiles["profiles"][i]["name"] == test_name):
                        print(test_name, "exists!")
                        found_username = True
                        break

                if (found_username == False):
                    print("Sorry,", test_name, "does not exist in our system")

            else:
                print("Please type a valid command.")

def register_new_profile():
    """Walks the user through registering a new profile

        Returns
        -------
        list_of_information : list
            list containing [(string) name, (set)enabled_features]
    """

    user_name = ""
    name_is_valid = False
    while name_is_valid == False:
        user_name = input("Please type your name: ")
        if (not user_name) or (user_name.isspace()):  # name is invalid if it's empty or contains only spaces
            print("Please enter in a valid name")
        else:
            name_is_valid = True
    print_features()
    features_are_valid = False
    enabled_features = set()
    while features_are_valid == False:
        enabled_features = set()
        print(
            "Input the number(s) of the feature(s) you intend on using (can enable, disable, and customize these later)")
        print("Type 'done' when finished selecting")
        while (65 == 65):
            current_user_input = input("")
            if current_user_input.lower() == "done":
                break
            elif current_user_input == "1" or current_user_input == "2":
                enabled_features.add(current_user_input)
            else:
                print(current_user_input, "is not a valid input. Not accepting.")
        if (len(enabled_features) > 2) or (len(enabled_features) == 0):
            print("Invalid input. Please reselect valid input")
        else:
                    features_are_valid = True
    total_wealth = 0.00
    budget = 0.00
    wealth_is_valid = False
    while wealth_is_valid == False:
        total_wealth = float(input("Please enter your current total wealth (ex: 10.00): "))
        check_float = isinstance(total_wealth, float)
        if check_float == False:
            print("Please enter a valid amount")
        else:
            wealth_is_valid = True
    budget_is_valid = False
    while budget_is_valid == False:
        budget = float(input("Please enter your current monthly budget (ex: 10.00): "))
        check_float = isinstance(budget, float)
        if check_float == False:
            print("Please enter a valid amount")
        else:
            budget_is_valid = True
    # Check to make sure enabled_features contains valid input



    # Return the name and enabled features for the the new profile in a list
    list_of_information = [user_name, enabled_features, total_wealth, budget]
    return list_of_information


def print_features():
    """Prints each feature and their descriptions for the user"""
    print("Here is a list of our available features:")
    print("1: Budget Manager")
    print(
        "The budget manager allows users to\n -Set their current balance\n -Set a target balance\n -View helpful "
        "financial notifications\n -Keep track of deposits, withdrawals, and recurring expenses")
    print("2: Stock Market Tool")
    print(
        "The Stock Market Tool allows users to\n -Select a sector to focus on that will filter for news that is "
        "specific to that sector\n -Allow users to view a list of stocks and their recent performance\n -Allow users "
        "to view a news feed regarding recent events in the general stock market\n")


def load_existing_profiles():
    """First, this function will ensure that the file profiles.json exists. If it doesn't, then we create it.
    Then, this function checks if there are already existing profiles. If there are, we load them into program.
    If there are no existing profiles, then make the boolean existing_profiles False

    Returns
    -------
    there_are_existing_profiles : bool
        boolean that tells us if there are existing profiles already in profiles.json

    loaded_profiles : json
        existing data from profiles.json if there are existing profiles, empty dict if there are none
    """

    # Check if profiles.json exists first
    if os.path.isfile("profiles.json"):
        print("Found profiles.json - Loading Profiles Now")
    else:
        print("profiles.json doesn't exist - Creating profiles.json")
        f = open("profiles.json", "w")
        f.write("")  # dont think this is needed anymore

    if os.stat("profiles.json").st_size == 0:  # if profiles.json is empty (A.K.A no existing profiles)
        there_are_existing_profiles = False
    else:
        there_are_existing_profiles = True

    if (there_are_existing_profiles):
        with open('profiles.json') as json_file:
            loaded_profiles = json.load(json_file)

    else:  # No profiles made previously
        loaded_profiles = {}

    return there_are_existing_profiles, loaded_profiles


def write_new_profile_data_to_file(there_are_existing_profiles, loaded_profiles, list_of_information):
    """After getting the user's profile details, store the information in our json file

        Parameters
        ----------
        there_are_existing_profiles : bool
            Boolean that tells us if profiles.json has existing profiles in it already
       loaded_profiles : json
            existing data from profiles.json if there are existing profiles, empty dict if there are none
       list_of_information : list
            list containing [(string) name, (set)enabled_features]
    """
    # if there aren't any existing profiles in profiles.json
    if there_are_existing_profiles == False:
        # Must create the json object from scratch first since it does not exist yet
        data = {}
        data['profiles'] = []
        data['profiles'].append({
            'name': list_of_information[0],
            'features': list(list_of_information[1]),
            'total_wealth': list_of_information[2],
            'budget': list_of_information[3]
        })
        with open('profiles.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, sort_keys=False)

    # else if there are already existing profiles in profiles.json
    elif there_are_existing_profiles == True:
        # Simply append the new profile data to the profiles.json file
        loaded_profiles['profiles'].append({
            'name': list_of_information[0],
            'features': list(list_of_information[1]),
            'total_wealth': list_of_information[2],
            'budget': list_of_information[3]
        })
        with open('profiles.json', 'w') as outfile:
            json.dump(loaded_profiles, outfile, indent=2, sort_keys=False)

