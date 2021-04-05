from settings_page import *
from budget_manager import *
def run_home_page(profile):
    while (True):
        print("Home Page Now running - Your profile ID number is:",profile[0])
        print("Welcome "+profile[1]+"! Your enabled features are", profile[2])

        print("Type 1 to open settings page")
        print("Type 2 to open Budget Manager")
        print("Type 3 to Logout back to the landing page")
        user_input = input("")
        if(user_input == "1"):
            profile = run_settings_page(profile)
        elif(user_input == "2"):
            profile = run_budget_manager(profile)
        elif(user_input == "3"):
            print("Logging out of your profile.")
            break
        else:
            print("Please enter a valid command")