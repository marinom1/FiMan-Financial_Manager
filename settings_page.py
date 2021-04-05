import json
import os
def run_settings_page(profile):
    while (True):
        print("Type 1 to change your profile name")
        print("Type 2 to change your enabled features")
        print("Type 3 to exit settings")
        user_input = input("")
        if (user_input == "1"): #Change Profile Name
            print("Your current name is", profile[1])
            while (True):
                user_input = input("Enter in your new profile name")
                if (not user_input) or (user_input.isspace()):  # name is invalid if it's empty or contains only spaces
                    print("Please enter in a valid name")
                else:
                    profile[1] = user_input
                    break
            #Now update profiles.json with new name
            with open('profiles.json', "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["name"] = user_input

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully updated profile name to", profile[1])
            return profile

        elif (user_input == "2"):
            print("Your current enabled features are:", profile[2])

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

                # Check to make sure enabled_features contains valid input
                if (len(enabled_features) > 2) or (len(enabled_features) == 0):
                    print("Invalid input. Please reselect valid input")
                else:
                    features_are_valid = True
                profile[2] = enabled_features
                #Now update profiles.json with new enabled features
                with open("profiles.json", "r+") as file:
                    loaded_profiles = json.load(file)
                    loaded_profiles["profiles"][profile[0]]["features"] = list(enabled_features)

                os.remove("profiles.json")
                with open("profiles.json", "w") as file:
                    json.dump(loaded_profiles, file, indent=2, sort_keys=False)

                print("Successfully updated profile's enabled features to ", profile[2])
                return profile

        elif (user_input == "3"):
            print("Exiting Settings Page...\n")
            return profile
        else:
            print("Please enter a valid command.")


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
