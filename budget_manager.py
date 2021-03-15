import json
import os

def run_budget_manager(profile):
    while (True):
        print("Type 1 to adjust your total wealth")
        print("Type 2 to adjust your budget")
        print("Type 3 to enter an expense")
        print("Type 4 to exit Budget Manager")
        user_input = int(input(""))
        if (user_input == 1):
            print("Your current total wealth is", profile[3])
            while (True):
                user_input = float(input("Enter in your new total wealth"))
                check_float = isinstance(user_input, float)
                if check_float == False:
                    print("Please enter in a valid amount (ex: 10.00)")
                else:
                    profile[3] = user_input
                    break
            #Now update profiles.json with new wealth
            with open('profiles.json', "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["total_wealth"] = user_input

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully updated profile name to", profile[1])
            print("This is what I am returning:",profile[0],profile[1],profile[2],profile[3],profile[4])
            return profile

        elif (user_input == 2):
            print("Your current budget for this month is:", profile[4])
            while(True):
                user_input = float(input("Please enter your new monthly budget (ex: 10.00): "))
                check_float = isinstance(user_input, float)
                if check_float == False:
                    print("Please enter a valid amount")
                else:
                    profile[4] = user_input
                    break
                #Now update profiles.json with new enabled features
            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["budget"] = user_input

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully updated profile's budget to ", profile[4])
            print("This is what I am returning:", profile[0],profile[1],profile[2],profile[3],profile[4])
            return profile

        elif (user_input == 3):
            print("Your current budget for this month is:", profile[4])
            while (True):
                user_input_ex = float(input("Please enter your expense (ex: 5.00): "))
                check_float = isinstance(user_input_ex, float)
                if check_float == False:
                    print("Please enter a valid amount")
                else:
                    profile[4] = profile[4] - user_input_ex
                    break
            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["budget"] = profile[4]

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully added expense. Updated profile's budget to ", profile[4])
            print("This is what I am returning:", profile[0],profile[1],profile[2],profile[3],profile[4])
            return profile
        elif (user_input == 4):
            print("Exiting Budget Manager... \n")
            return profile
            break
