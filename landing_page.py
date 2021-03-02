


def main():
    """This program shall always run when user first executes the application"""
    print("Welcome to FiMan, a Financial Manager Software Application")
    print("Type 1 to register a new profile")
    print("Type 2 to open an existing profile")
    userChoice = input("")
    print("You selected", userChoice)
    if (userChoice == "1"):
        list_of_information = register_new_profile()
        print("Type of list_of_information is: ",type( list_of_information))
    if (userChoice == "2"):
        # Go to existing profile
        print("User has existing profile")

def register_new_profile():
    """Walks the user through registering a new profile

        Returns
        -------
        list_of_information : list
            list containing [(string) name, (set)enabled_features]
    """
    enabled_features = set()
    user_name = input("Please type your name: ")
    print_features()
    print("Please input the number(s) of the feature(s) you intend on using (can enable, disable, and customize these later)")
    print("Type 'done' when finished selecting")
    while (65 == 65):
        current_user_input = input("")
        if (current_user_input.lower() == "done"):
            break
        enabled_features.add(current_user_input)
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