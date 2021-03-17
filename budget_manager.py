import json
import os

def run_budget_manager(profile): # profile = [profile index, profile name, profile enabled features, profile wealth, profile budget]
    while (True):
        print("Your current wealth is:", profile[3], "Your current budget is",profile[4])
        print("Type 1 to adjust your total wealth")
        print("Type 2 to adjust your budget")
        print("Type 3 to enter an expense")
        print("Type 4 to exit Budget Manager")
        user_input = input("")
        if (user_input == "1"): #Adjust total wealth
            print("Your current total wealth is", profile[3])
            while (True):
                try:
                    user_input = float(input("Enter in your new total wealth"))
                except:
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

            print("Successfully updated wealth to", profile[3], "\n")

        elif (user_input == "2"): #Adjust budget
            print("Your current budget for this month is:", profile[4])
            while(True):
                try:
                    user_input = float(input("Please enter your new monthly budget (ex: 10.00): "))
                except:
                    print("Please enter in a valid amount (ex: 10.00)")
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

            print("Successfully updated profile's budget to ", profile[4], "\n")

        elif (user_input == "3"): #Enter an expense
            print("Your current budget for this month is:", profile[4])
            while (True):
                try:
                    user_input_ex = float(input("Please enter your expense (ex: 5.00): "))
                except:
                    print("Please enter in a valid amount (ex: 10.00)")
                else:
                    profile[4] = profile[4] - user_input_ex
                    break
            #Now update profiles.json
            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["budget"] = profile[4]

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully added expense. Updated profile's budget to", profile[4], "\n")

        elif (user_input == "4"): #Exit Budget Manager Feature
            print("Exiting Budget Manager... \n")
            return profile
        else:
            print("Please enter a valid command.")
