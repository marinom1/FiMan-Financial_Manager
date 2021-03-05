
def main():
    """This program shall always run when user first executes the application"""
    print("Welcome to FiMan, a Financial Manager Software Application")
    valid_input = False
    while (valid_input == False):
        print("Type 1 to register a new profile")
        print("Type 2 to open an existing profile")
        print("Type 3 to exit program")
        userChoice = input("")
        print("You selected", userChoice)
        if (userChoice == "1"):
            valid_input = True
            list_of_information = register_new_profile() #User will go through registration, then their info is stored in list_of_information
            print("New Profile Registered Successfully! Name:",list_of_information[0], "- Features:", list_of_information[1])
        elif (userChoice == "2"):
            # Go to existing profile
            #TODO - Continuation of login process
            valid_input = True
            print("User has existing profile")
        elif (userChoice == "3"):
            valid_input = True
            print("Exiting program...")
            exit(0)
        else:
            print("Please type a valid command.")

def register_new_profile():
    """Walks the user through registering a new profile

        Returns
        -------
        list_of_information : list
            list containing [(string) name, (set)enabled_features]
    """

    name_is_valid = False
    while(name_is_valid == False):
        user_name = input("Please type your name: ")
        if (not user_name) or (user_name.isspace()): #name is invalid if it's empty or contains only spaces
            print("Please enter in a valid name")
        else:
            name_is_valid = True
    print_features()
    features_are_valid = False
    enabled_features = set()
    while (features_are_valid == False):
        enabled_features = set()
        print("Input the number(s) of the feature(s) you intend on using (can enable, disable, and customize these later)")
        print("Type 'done' when finished selecting")
        while (65 == 65):
            current_user_input = input("")
            if (current_user_input.lower() == "done"):
                break
            elif (current_user_input == "1" or current_user_input == "2"):
                enabled_features.add(current_user_input)
            else:
                print(current_user_input, "is not a valid input. Not accepting.")

        #Check to make sure enabled_features contains valid input
        if (len(enabled_features) > 2) or (len(enabled_features) == 0):
            print("Invalid input. Please reselect valid input")
        else:
            features_are_valid = True

    #Return the name and enabled features for the the new profile in a list
    list_of_information = [user_name, enabled_features]
    return list_of_information

def print_features():
    """Prints each feature and their descriptions for the user"""
    print("Here is a list of our available features:")
    print("1: Budget Manager")
    print("The budget manager allows users to\n -Set their current balance\n -Set a target balance\n -View helpful financial notifications\n -Keep track of deposits, withdrawals, and recurring expenses")
    print("2: Stock Market Tool")
    print("The Stock Market Tool allows users to\n -Select a sector to focus on that will filter for news that is specific to that sector\n -Allow users to view a list of stocks and their recent performance\n -Allow users to view a news feed regarding recent events in the general stock market\n")



main()