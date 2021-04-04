import json
import os
import random

def run_budget_manager(profile): # profile = [profile index, profile name, profile enabled features, profile balance, profile budget, profile expenses]
    while (True):
        print("Your current balance is:", profile[3], "\nYour current budget is", profile[4], "\n")
        print("Type 1 to adjust your total balance")
        print("Type 2 to adjust your budget")
        print("Type 3 to enter an expense")
        print("Type 4 to remove an expense")
        print("Type 5 to see a notification")
        print("Type 6 to exit Budget Manager")
        user_input = input("")
        if (user_input == "1"): # Adjust total balance
            print("Your current total balance is", profile[3])
            while (True):
                try:
                    user_input = float(input("Enter in your new total balance"))
                except:
                    print("Please enter in a valid amount (ex: 10.00)")
                else:
                    profile[3] = user_input
                    break
            # Now update profiles.json with new balance
            with open('profiles.json', "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["total_balance"] = user_input

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully updated balance. \n")

        elif (user_input == "2"): # Adjust budget
            print("Your current budget for this month is:", profile[4])
            while(True):
                try:
                    user_input = float(input("Please enter your new monthly budget (ex: 10.00): "))
                except:
                    print("Please enter in a valid amount (ex: 10.00)")
                else:
                    profile[4] = user_input
                    break
            # Now update profiles.json with new enabled features
            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["budget"] = user_input

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully updated profile's budget. \n")

        elif (user_input == "3"): #Enter an expense
            print("Your current budget for this month is:", profile[4])
            while (True):
                try:
                    user_input_ex = float(input("Please enter your expense (ex: 5.00): "))
                except:
                    print("Please enter in a valid amount (ex: 10.00)")
                else:
                    user_input_desc = input("Please enter a description for the expense (ex: Netflix Subscription)")
                    user_input_date = input("Please enter the date of the expense (ex: 04/15/21)")
                    profile[3] = profile[3] - user_input_ex
                    profile[4] = profile[4] - user_input_ex
                    expense_info = [user_input_ex, user_input_desc, user_input_date]
                    profile[5].append(expense_info)
                    break

            #Now update profiles.json
            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["total_balance"] = profile[3]
                loaded_profiles["profiles"][profile[0]]["budget"] = profile[4]
                loaded_profiles["profiles"][profile[0]]["expenses"] = profile[5]

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)


            print("Successfully added expense. \n")

        elif (user_input == "4"): # Remove expense
            while (True):
                for i in range(len(profile[5])):
                    print(i+1, ". ", profile[5][i][1], "\n")
                try:
                    user_input = int(input("Which expense would you like to remove? (Enter the number of the expense)"))
                except:
                    print("Please enter in a valid expense (ex: 1, 2, 3)")
                else:
                    profile[3] = profile[3] + profile[5][user_input - 1][0]
                    profile[4] = profile[4] + profile[5][user_input - 1][0]
                    profile[5].pop(user_input-1)

                    break
            # Now update profiles.json
            with open("profiles.json", "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][profile[0]]["total_balance"] = profile[3]
                loaded_profiles["profiles"][profile[0]]["expenses"] = profile[5]
                loaded_profiles["profiles"][profile[0]]["budget"] = profile[4]

            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

            print("Successfully removed expense. \n")

        elif (user_input == "5"): # Notification Feature
            print(generate_notification(profile)+ "\n")

        elif (user_input == "6"): # Exit Budget Manager Feature
            print("Exiting Budget Manager... \n")
            return profile
        else:
            print("Please enter a valid command.")

def generate_notification(profile): # profile = [profile index, profile name, profile enabled features, profile balance, profile budget]
    """Returns string with the notification"""
    x = random.randint(1,5) #generate random int between 1 and 4
    if (x == 1):
        if (profile[3] > 3400):
            return "You have more money than the average American has in the bank (> $3,400)"
        else:
            return "You have less money than the average American has in the bank (> $3,400)"
    elif (x == 2):
        if (profile[4] > 5102):
            return "The average american spends $5,102 in a month. Your budget is currently more than that"
        else:
            return "The average american spends $5,102 in a month. Your budget is currently less than that"
    elif(x==3):
        return "Are you taking into consideration your retirement plan?"
    elif(x==4):
        return "Only 30% of American households have a long-term financial plan"
