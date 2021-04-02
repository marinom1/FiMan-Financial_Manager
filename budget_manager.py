import json
import os

def run_budget_manager(profile): # profile = [profile index, profile name, profile enabled features, profile balance, profile budget]
    while (True):
        print("Your current balance is:", profile[3], "Your current budget is",profile[4])
        print("Type 1 to adjust your total balance")
        print("Type 2 to adjust your budget")
        print("Type 3 to enter an expense")
        print("Type 4 to remove an expense")
        print("Type 5 to exit Budget Manager")
        user_input = input("")
        if (user_input == "1"): #Adjust total balance
            print("Your current total balance is", profile[3])
            while (True):
                try:
                    user_input = float(input("Enter in your new total balance"))
                except:
                    print("Please enter in a valid amount (ex: 10.00)")
                else:
                    profile[3] = user_input
                    break
            #Now update profiles.json with new balance
            with open('profiles.json', "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["total_balance"] = user_input

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully updated balance to", profile[3], "\n")

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
                    profile[5].append(user_input_ex)
                    break
            #Now update profiles.json
            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["budget"] = profile[4]
                loaded_profiles["profiles"][profile[0]]["expenses"] = profile[5]

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)


            print("Successfully added expense. Updated profile's budget to", profile[4], "\n")

        elif (user_input == "4"):
            while (True):
                for i in range(len(profile[5])):
                    print(i+1, ". ", profile[5][i], "\n")
                try:
                    user_input = int(input("Which expense would you like to remove? (Enter the number of the expense)"))
                except:
                    print("Please enter in a valid expense (ex: 1, 2, 3)")
                else:
                    profile[4] = profile[4] + profile[5][user_input - 1]
                    profile[5].pop(user_input-1)

                    break

            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["expenses"] = profile[5]
                loaded_profiles["profiles"][profile[0]]["budget"] = profile[4]

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully removed expense. Updated profile's budget to", profile[4], "\n")

        elif (user_input == "5"): #Exit Budget Manager Feature
            print("Exiting Budget Manager... \n")
            return profile
        else:
            print("Please enter a valid command.")
