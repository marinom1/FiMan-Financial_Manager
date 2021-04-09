import tkinter as tk
from tkinter import font as tkfont
import json
import os
from landing_page import load_existing_profiles
from home_page_gui import *

#from https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
#helpful with connecting textbox to button https://codeloop.org/how-to-create-textbox-in-python-tkinter/

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
        f.write('{\n\t"profiles": []\n}')

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

there_are_existing_profiles, loaded_profiles = load_existing_profiles()

current_profile_ID = -1

#Global variables used during registration process
new_name = ""
new_enabled_features = [-1]
enabled_feature1 = 0
enabled_feature2 = 0 #0 is false, 1 is true
new_balance = 0.01
new_budget = 0.01

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen, PageEleven, PageTwelve, PageThirteen): #If making new page, be sure to add it in here
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        test_var = tk.StringVar()
        test_var.set("this is a test")
        self.show_frame("StartPage")



    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame): #Welcome to FiMan
    def __init__(self, parent, controller):
        def exit_program():
            exit(0)
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to FiMan! A Financial Manager Software Application")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Register new profile",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Login to existing profile",
                            command=lambda: controller.show_frame("PageSix"))
        button3 = tk.Button(self, text="Exit FiMan", command=lambda: exit_program())
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame): #Register a new profile (Enter name)

    def store_name(self, new_name_var):
        name = new_name_var.get()
        print("new_name_var is:", name)
        global new_name
        new_name = name

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 1 of 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="Please enter your name")
        label1.pack()
        new_name_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_name_var)
        entry.pack()
        button = tk.Button(self, text="Next",
                           command=lambda: [self.store_name(new_name_var), controller.show_frame("PageTwo")])
        button.pack()


class PageTwo(tk.Frame): #Register a new profile (Choose Features)

    def store_details(self, feature1_var, feature2_var):
        print("Is feature 1 checked off:",feature1_var.get())
        print("Is feature 2 checked off:", feature2_var.get())
        global new_enabled_features
        new_enabled_features = []
        print("type of new_enabled_features is:",type(new_enabled_features))
        if feature1_var.get():
            print("Does this run")
            new_enabled_features.append("1")
        if feature2_var.get():
            new_enabled_features.append("2")
        print("new_name is", new_name)
        print("new_enabled_features is:", new_enabled_features)



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 2 of 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #Budget Manager descriptions
        label1 = tk.Label(self, text="Budget Manager: The The Budget Manager allows users to ")
        label1.pack()
        label2 = tk.Label(self, text="-Set their current balance-Set a target balance")
        label2.pack()
        label3 = tk.Label(self, text="-View helpful financial notifications")
        label3.pack()
        label4 = tk.Label(self, text="-Keep track of deposits, withdrawals, and recurring expenses")
        label4.pack()
        #Stock Market tool descriptions
        label5 = tk.Label(self, text="2. Stock Market Tool: The Stock Market Tool allows users to")
        label5.pack()
        label6 = tk.Label(self, text="-Select a sector to focus on that will filter for news that is specific to that sector")
        label6.pack()
        label7 = tk.Label(self, text="-Allow users to view a list of stocks and their recent performance")
        label7.pack()
        label8 = tk.Label(self, text="-Allows users to view a news feed regarding recent events in the general stock market")
        label8.pack()
        #End of descriptions
        label9 = tk.Label(self,text="Please check off the features you would like to enable (Can change later)")
        label9.pack()
        #Checkboxes
        feature1_var = tk.IntVar()
        feature2_var = tk.IntVar()
        checkbutton1 = tk.Checkbutton(self, text="Budget Manager", variable=feature1_var)
        checkbutton1.pack()
        checkbutton2 = tk.Checkbutton(self, text="Stock Market Tool", variable=feature2_var)
        checkbutton2.pack()

        button = tk.Button(self, text="Next",
                           command=lambda: [ self.store_details(feature1_var,feature2_var), controller.show_frame("PageThree")])
        button.pack()


class PageThree(tk.Frame): # Register a new profile (Enter balance)
    def print_balance(self, new_balance_var):
        balance = new_balance_var.get()
        print("new_name_var is:", balance)
        global new_balance
        new_balance = balance

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 3 of 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="Please enter your balance")
        label1.pack()
        new_balance_var = tk.DoubleVar()
        entry = tk.Entry(self, width=15, textvariable=new_balance_var)
        entry.pack()
        button = tk.Button(self, text="Next",
                           command=lambda: [self.print_balance(new_balance_var), controller.show_frame("PageFour")])
        button.pack()

class PageFour(tk.Frame): # Register a new profile (Enter budget)
    def print_balance(self, new_budget_var):
        budget = new_budget_var.get()
        print("new_name_var is:", budget)
        global new_budget
        new_budget = budget

    def write_new_profile_to_file(self):
        """Make the new profile official in profiles.json"""
        global new_name
        global new_enabled_features
        global new_balance
        global new_budget
        # if there aren't any existing profiles in profiles.json
        if there_are_existing_profiles == False:
            # Must create the json object from scratch first since it does not exist yet
            data = {}
            data['profiles'] = []
            data['profiles'].append({
                'name': new_name,
                'features': new_enabled_features,
                'total_balance': new_balance,
                'budget': new_budget,
                'expenses': []
            })
            with open('profiles.json', 'w') as outfile:
                json.dump(data, outfile, indent=2, sort_keys=False)

        # else if there are already existing profiles in profiles.json
        elif there_are_existing_profiles == True:
            # Simply append the new profile data to the profiles.json file
            loaded_profiles['profiles'].append({
                'name': new_name,
                'features': new_enabled_features,
                'total_balance': new_balance,
                'budget': new_budget,
                'expenses': []
            })
            with open('profiles.json', 'w') as outfile:
                json.dump(loaded_profiles, outfile, indent=2, sort_keys=False)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 4 of 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="Please enter your budget")
        label1.pack()
        new_balance_var = tk.DoubleVar()
        entry = tk.Entry(self, width=15, textvariable=new_balance_var)
        entry.pack()
        button = tk.Button(self, text="Next",
                           command=lambda: [self.print_balance(new_balance_var), self.write_new_profile_to_file(), controller.show_frame("PageFive")])
        button.pack()

class PageFive(tk.Frame): #Registration Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registration Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageSix(tk.Frame): #Login to Existing Profile

    def __init__(self, parent, controller):
        def get_profile_ID(i):
            print("Profile ID in Login to Existing Profile is:",i)
            global current_profile_ID
            current_profile_ID = i
            print("The current_profile_ID is:", current_profile_ID)

        def refresh_profiles():
            print("Does this print 1")
            there_are_existing_profiles, loaded_profiles = load_existing_profiles()
            #Destroy the existing stuff
            for widget in PageFour.winfo_children(self):
                widget.destroy()

            label = tk.Label(self, text="Please select your profile", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            print("len of loaded profiles here is:", len(loaded_profiles["profiles"]))
            for i in range(len(loaded_profiles["profiles"])):
                # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
                button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"],
                                   command=lambda name=i: [get_profile_ID(name), controller.show_frame("PageSeven")])

                button.pack()
            button1 = tk.Button(self, text="Click here to refresh profiles",
                                command=lambda: [refresh_profiles()])
            button1.pack()
            print("Does this print 2")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please select your profile", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global there_are_existing_profiles
        global loaded_profiles
        there_are_existing_profiles, loaded_profiles = load_existing_profiles()
        for i in range(len(loaded_profiles["profiles"])):
            # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
            button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"],
                               command=lambda name=i: [get_profile_ID(name), controller.show_frame("PageSeven")])

            button.pack()
        button1 = tk.Button(self, text="Click here to refresh profiles",
                           command=lambda: [refresh_profiles()])
        button1.pack()

class PageSeven(tk.Frame): #Login Successful
    def __init__(self, parent, controller):
        var = tk.StringVar()
        var.set("")
        def show_profile_details():
            var.set(loaded_profiles["profiles"][current_profile_ID])
        def restore_default_text():
            var.set("")
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Login Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global current_profile_ID
        print("current_profile_ID in Login Successful page is:", current_profile_ID)
        label1 = tk.Label(self, textvariable=var)
        label1.pack()
        button = tk.Button(self, text="Go to your Home Page",
                           command=lambda: [restore_default_text(), controller.show_frame("PageEight")])
        button.pack()
        button1 = tk.Button(self, text="Click to see your profile details to make sure you logged into the right profile",
                           command=lambda: show_profile_details())
        button1.pack()

class PageEight(tk.Frame): # Home Page

    def __init__(self, parent, controller):
        var = tk.StringVar()
        var.set("")
        def show_profile_details():
            there_are_existing_profiles, loaded_profiles = load_existing_profiles()
            var.set(loaded_profiles["profiles"][current_profile_ID])

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Home Page")
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, textvariable=var)
        label1.pack()

        button1 = tk.Button(self, text="Settings",
                            command=lambda: controller.show_frame("PageNine"))
        button2 = tk.Button(self, text="Budget Manager",
                            command=lambda: controller.show_frame("PageFour"))
        button3 = tk.Button(self, text="Stock Market",
                            command=lambda: controller.show_frame("PageFour"))
        button4 = tk.Button(self, text="Logout", command=lambda: controller.show_frame("StartPage"))
        button5 = tk.Button(self, text="Click to refresh/see your profile details", command=lambda: show_profile_details())
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()

class PageNine(tk.Frame): # Settings - Michael

    def __init__(self, parent, controller):
        var = tk.StringVar()
        var.set("")

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Settings")
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, textvariable=var)
        label1.pack()

        button1 = tk.Button(self, text="Change Profile Name",
                            command=lambda: controller.show_frame("PageTen"))
        button2 = tk.Button(self, text="Change enabled features",
                            command=lambda: controller.show_frame("PageTwelve"))
        button3 = tk.Button(self, text="Exit Settings",
                            command=lambda: controller.show_frame("PageEight"))

        button1.pack()
        button2.pack()
        button3.pack()


class PageTen(tk.Frame): # Settings - Change Name

    def store_name(self, new_name_var):
        name = new_name_var.get()
        print("new_name_var is:", name)
        global new_name
        new_name = name
        # Now update profiles.json with new name
        with open('profiles.json', "r+") as file:
            loaded_profiles = json.load(file)
            loaded_profiles["profiles"][current_profile_ID]["name"] = new_name

        os.remove("profiles.json")
        with open("profiles.json", "w") as file:
            json.dump(loaded_profiles, file, indent=2, sort_keys=False)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Please enter your new name")
        label1.pack()
        new_name_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_name_var)
        entry.pack()
        button = tk.Button(self, text="Next",
                           command=lambda: [self.store_name(new_name_var), controller.show_frame("PageEleven")])
        button.pack()

class PageEleven(tk.Frame): # Name change Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Name Change Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to the home page",
                           command=lambda: controller.show_frame("PageEight"))
        button.pack()

class PageTwelve(tk.Frame): #Settings - Choose Enabled Features
        def store_details(self, feature1_var, feature2_var):
            global new_enabled_features
            new_enabled_features = []
            if feature1_var.get():
                new_enabled_features.append("1")
            if feature2_var.get():
                new_enabled_features.append("2")
            # Now update profiles.json with new features
            with open('profiles.json', "r+") as file:
                loaded_profiles = json.load(file)
                loaded_profiles["profiles"][current_profile_ID]["features"] = new_enabled_features
            os.remove("profiles.json")
            with open("profiles.json", "w") as file:
                json.dump(loaded_profiles, file, indent=2, sort_keys=False)

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="Change Features", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            # Budget Manager descriptions
            label1 = tk.Label(self, text="Budget Manager: The The Budget Manager allows users to ")
            label1.pack()
            label2 = tk.Label(self, text="-Set their current balance-Set a target balance")
            label2.pack()
            label3 = tk.Label(self, text="-View helpful financial notifications")
            label3.pack()
            label4 = tk.Label(self, text="-Keep track of deposits, withdrawals, and recurring expenses")
            label4.pack()
            # Stock Market tool descriptions
            label5 = tk.Label(self, text="2. Stock Market Tool: The Stock Market Tool allows users to")
            label5.pack()
            label6 = tk.Label(self,
                              text="-Select a sector to focus on that will filter for news that is specific to that sector")
            label6.pack()
            label7 = tk.Label(self, text="-Allow users to view a list of stocks and their recent performance")
            label7.pack()
            label8 = tk.Label(self,
                              text="-Allows users to view a news feed regarding recent events in the general stock market")
            label8.pack()
            # End of descriptions
            label9 = tk.Label(self, text="Please check off the features you would like to enable (Can change later)")
            label9.pack()
            # Checkboxes
            feature1_var = tk.IntVar()
            feature2_var = tk.IntVar()
            checkbutton1 = tk.Checkbutton(self, text="Budget Manager", variable=feature1_var)
            checkbutton1.pack()
            checkbutton2 = tk.Checkbutton(self, text="Stock Market Tool", variable=feature2_var)
            checkbutton2.pack()

            button = tk.Button(self, text="Next",
                               command=lambda: [self.store_details(feature1_var, feature2_var),
                                                controller.show_frame("PageThirteen")])
            button.pack()

class PageThirteen(tk.Frame): # Enabled Features Change Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enabled Features Change Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to the home page",
                           command=lambda: controller.show_frame("PageEight"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("700x500")
    app.mainloop()