from settings_page import *
def run_home_page(profile):
    while (True):
        print("Home Page Now running - Your profile ID number is:",profile[0])
        print("Welcome "+profile[1]+"! Your enabled features are", profile[2])

        print("Type 1 to open settings page")
        print("Type 2 to do something else")
        print("Type 3 to Logout back to the landing page")
        user_input = int(input(""))
        if(user_input == 1):
            profile = run_settings_page(profile)
        elif(user_input == 2):
            print("You selected 2. This doesn't do anything yet.")
        elif(user_input == 3):
            print("Logging out of your profile.")
            break