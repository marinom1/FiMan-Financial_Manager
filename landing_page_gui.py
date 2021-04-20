import tkinter as tk
<<<<<<< HEAD
import json, os, webbrowser, requests
from config import FinnhubIOKey
=======
import webbrowser
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119
from datetime import datetime as dt
from functools import partial
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
from landing_page import load_existing_profiles
from home_page import *
from stock_market import *

# "template" from https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# Inspiration: https://stackoverflow.com/questions/4066974/scrolling-multiple-tkinter-listboxes-together

# Upon first starting FiMan, attempt to load data from profiles.json first
there_are_existing_profiles, loaded_profiles = load_existing_profiles()
current_profile_ID = -1

# Global variables used during registration process
new_name = ""
new_enabled_features = [-1]
enabled_feature1 = 0  # 0 is false, 1 is true
enabled_feature2 = 0  # 0 is false, 1 is true
new_balance = 0.01
new_budget = 0.01


class FiMan(tk.Tk):
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

        for F in (
<<<<<<< HEAD
            StartPage, 
            PageOne, 
            PageTwo, 
            PageThree, 
            PageFour, 
            PageFive, 
            PageSix, 
            PageSeven, 
            PageEight, 
            PageNine, 
            PageTen, 
            PageEleven, 
            PageTwelve, 
            PageThirteen, 
            StockMarketHomePage, 
            SMSectorsPage, 
            SMCompaniesAndTickersPage, 
            SMNewsAndArticlesPage,
            SMCompanySearchPage
            # SMSavedCompaniesAndTickersPage
        ): # If making new page, be sure to add it in here
=======
                StartPage,
                PageOne,
                PageTwo,
                PageThree,
                PageFour,
                PageFive,
                PageSix,
                PageSeven,
                PageEight,
                PageNine,
                PageTen,
                PageEleven,
                PageTwelve,
                PageThirteen,
                StockMarketHomePage,
                SMSectorsPage,
                SMCompaniesAndTickersPage,
                SMNewsAndArticlesPage,
                # SMSavedCompaniesAndTickersPage,
                BudgetManagerHomePage,
                BMAdjustBalance,
                BMAdjustBudget,
                BMEnterDeposit,
                BMEnterExpense,
                BMBudgetHistory
                # SMSymbolLookupPage
                # SMSavedCompaniesAndTickersPage
        ):  # If making new page, be sure to add it in here
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119

            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):  # Welcome to FiMan
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to FiMan!\n A Financial Manager Software Application",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Register", width=8,
                            command=lambda: [update_page_one(), controller.show_frame("PageOne")])
        button1.pack()
        button2 = tk.Button(self, text="Login", width=8,
                            command=lambda: [update_page_six(), controller.show_frame("PageSix")])
        button2.pack()
        button3 = tk.Button(self, text="Exit", width=8, command=lambda: exit(0))
        button3.pack()

        def update_page_one():
            app.frames["PageOne"].destroy()
            app.frames["PageOne"] = PageOne(parent, controller)
            app.frames["PageOne"].grid(row=0, column=0, sticky="nsew")

        def update_page_six():
            app.frames["PageSix"].destroy()
            app.frames["PageSix"] = PageSix(parent, controller)
            app.frames["PageSix"].grid(row=0, column=0, sticky="nsew")


class PageOne(tk.Frame):  # Register a new profile (Enter name)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 1 of 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="Enter Full Name")
        label1.pack()
        new_name_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_name_var)
        entry.pack()
        button = tk.Button(self, text="Next", command=lambda: [check_name(new_name_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
        button1.pack()

        def check_name(new_name_var):
            name_already_taken = False
            name = new_name_var.get()
            list_of_existing_profile_names = []
            if there_are_existing_profiles:
                for i in range(len(loaded_profiles["profiles"])):
                    list_of_existing_profile_names.append(loaded_profiles["profiles"][i]["name"])
            if name in list_of_existing_profile_names:
                name_already_taken = True
            if (name.isspace()) or (name == "") or name_already_taken:  # invalid name
                # Destroy the existing stuff
                for widget in PageFour.winfo_children(self):
                    widget.destroy()
                label = tk.Label(self, text="Step 1 of 4", font=controller.title_font)
                label.pack(side="top", fill="x", pady=10)
                if name.isspace() or name == "":
                    label1 = tk.Label(self, text="Please enter a VALID name - That name is blank")
                    label1.pack()
                elif name_already_taken:
                    label1 = tk.Label(self, text="Please enter a VALID name - That name is already taken")
                    label1.pack()
                new_name_var = tk.StringVar()
                entry = tk.Entry(self, width=15, textvariable=new_name_var)
                entry.pack()
                button = tk.Button(self, text="Next", command=lambda: [check_name(new_name_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
                button1.pack()
            else:  # valid input, store their name and move to next registration step
                print("new_name_var is:", name)
                global new_name
                new_name = name
                controller.show_frame("PageTwo")


class PageTwo(tk.Frame):  # Register a new profile (Choose Features)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 2 of 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # Budget Manager descriptions
        label1 = tk.Label(self, text="1. The Budget Manager allows users to:")
        label1.pack()
        label2 = tk.Label(self, text="- Set their current balance")
        label2.pack()
        label3 = tk.Label(self, text="- Set a target balance")
        label3.pack()
        label4 = tk.Label(self, text="- View helpful financial notifications")
        label4.pack()
        label5 = tk.Label(self, text="- Keep track of deposits, withdrawals, and recurring expenses")
        label5.pack()
        labelSpace = tk.Label(self, text="")
        labelSpace.pack()
        # Stock Market tool descriptions
        label6 = tk.Label(self, text="2. The Stock Market Tool allows users to:")
        label6.pack()
        label7 = tk.Label(self,
                          text="- Select a sector to focus on that will filter for news that is specific to that sector")
        label7.pack()
        label8 = tk.Label(self, text="- Allow users to view a list of stocks and their recent performance")
        label8.pack()
        label9 = tk.Label(self,
                          text="- Allows users to view a news feed regarding recent events in the general stock market")
        label9.pack()
        labelSpace = tk.Label(self, text="")
        labelSpace.pack()
        # End of descriptions
        label10 = tk.Label(self, text="Please check off the features you would like to enable (Can change later)")
        label10.pack()

        # Checkboxes
        feature1_var = tk.IntVar()
        feature2_var = tk.IntVar()
        checkbutton1 = tk.Checkbutton(self, text="Budget Manager", variable=feature1_var)
        checkbutton1.pack()
        checkbutton2 = tk.Checkbutton(self, text="Stock Market Tool", variable=feature2_var)
        checkbutton2.pack()

        button = tk.Button(self, text="Next", command=lambda: [check_valid_input(self, feature1_var, feature2_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
        button1.pack()

        def check_valid_input(self, feature1_var, feature2_var):
            self.store_details(feature1_var, feature2_var)
            if not new_enabled_features:  # If user didnt select any features
                # Destroy the existing stuff
                for widget in PageTwo.winfo_children(self):
                    widget.destroy()
                label = tk.Label(self, text="Step 2 of 4", font=controller.title_font)
                label.pack(side="top", fill="x", pady=10)

                # Budget Manager descriptions
                label1 = tk.Label(self, text="1. The Budget Manager allows users to:")
                label1.pack()
                label2 = tk.Label(self, text="- Set their current balance")
                label2.pack()
                label3 = tk.Label(self, text="- Set a target balance")
                label3.pack()
                label4 = tk.Label(self, text="- View helpful financial notifications")
                label4.pack()
                label5 = tk.Label(self, text="- Keep track of deposits, withdrawals, and recurring expenses")
                label5.pack()
                labelSpace = tk.Label(self, text="")
                labelSpace.pack()
                # Stock Market tool descriptions
                label6 = tk.Label(self, text="2. The Stock Market Tool allows users to:")
                label6.pack()
                label7 = tk.Label(self,
                                  text="- Select a sector to focus on that will filter for news that is specific to that sector")
                label7.pack()
                label8 = tk.Label(self, text="- Allow users to view a list of stocks and their recent performance")
                label8.pack()
                label9 = tk.Label(self,
                                  text="- Allows users to view a news feed regarding recent events in the general stock market")
                label9.pack()
                labelSpace = tk.Label(self, text="")
                labelSpace.pack()
                # End of descriptions
                label10 = tk.Label(self,
                                   text="CHECK OFF AT LEAST 1 BOX - Please check off the features you would like to enable (Can change later)")
                label10.pack()

                # Checkboxes
                feature1_var = tk.IntVar()
                feature2_var = tk.IntVar()
                checkbutton1 = tk.Checkbutton(self, text="Budget Manager", variable=feature1_var)
                checkbutton1.pack()
                checkbutton2 = tk.Checkbutton(self, text="Stock Market Tool", variable=feature2_var)
                checkbutton2.pack()

                button = tk.Button(self, text="Next",
                                   command=lambda: [check_valid_input(self, feature1_var, feature2_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
                button1.pack()
            else:  # Valid user input
                controller.show_frame("PageThree")

    def store_details(self, feature1_var, feature2_var):
        global new_enabled_features
        new_enabled_features = []
        if feature1_var.get():
            new_enabled_features.append("1")
        if feature2_var.get():
            new_enabled_features.append("2")


class PageThree(tk.Frame):  # Register a new profile (Enter balance)
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
        button = tk.Button(self, text="Next", command=lambda: [check_valid_input(new_balance_var), ])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
        button1.pack()

        def check_valid_input(new_balance_var):
            try:
                balance = new_balance_var.get()
                if balance < 0:
                    print("balance is number but is negative")
                    raise ValueError('balance is number but is negative')
                balance = round(balance, 2)  # Rounds balance to 2 decimal places
                global new_balance
                new_balance = balance
                controller.show_frame("PageFour")
            except:
                for widget in PageThree.winfo_children(self):
                    widget.destroy()
                label = tk.Label(self, text="Step 3 of 4", font=controller.title_font)
                label.pack(side="top", fill="x", pady=10)
                label1 = tk.Label(self, text="Please enter a valid balance")
                label1.pack()
                new_balance_var = tk.DoubleVar()
                entry = tk.Entry(self, width=15, textvariable=new_balance_var)
                entry.pack()
                button = tk.Button(self, text="Next",
                                   command=lambda: [check_valid_input(new_balance_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
                button1.pack()


class PageFour(tk.Frame):  # Register a new profile (Enter budget)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 4 of 4", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="Please enter your budget")
        label1.pack()
        new_budget_var = tk.DoubleVar()
        entry = tk.Entry(self, width=15, textvariable=new_budget_var)
        entry.pack()
        button = tk.Button(self, text="Next", command=lambda: [check_valid_input(new_budget_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
        button1.pack()

        def check_valid_input(new_budget_var):
            try:
                print("i will now test the .get()")
                budget = new_budget_var.get()
                print("new_budget_var succeeds the .get call")
                if budget < 0:
                    print("budget is number but is negative")
                    raise ValueError('budget is number but is negative')
                print("I got past the if statement")
                budget = round(budget, 2)  # Rounds budget to 2 decimal places
                global new_budget
                new_budget = budget
                write_new_profile_to_file()
                controller.show_frame("PageFive")
            except:
                print("invalid new_budget_var inputted")
                for widget in PageThree.winfo_children(self):
                    widget.destroy()
                label = tk.Label(self, text="Step 4 of 4", font=controller.title_font)
                label.pack(side="top", fill="x", pady=10)
                label1 = tk.Label(self, text="Please enter a valid budget")
                label1.pack()
                new_budget_var = tk.DoubleVar()
                entry = tk.Entry(self, width=15, textvariable=new_budget_var)
                entry.pack()
                button = tk.Button(self, text="Next",
                                   command=lambda: [check_valid_input(new_budget_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
                button1.pack()

        def write_new_profile_to_file():
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
                    'deposits': [],
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
                    'deposits': [],
                    'expenses': []
                })
                with open('profiles.json', 'w') as outfile:
                    json.dump(loaded_profiles, outfile, indent=2, sort_keys=False)


class PageFive(tk.Frame):  # Registration Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registration Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button_home = tk.Button(self, text="Home", width=8, command=lambda: controller.show_frame("PageEight"))
        button_home.pack()
        buttonRegistration = tk.Button(self, text="Landing", width=8,
                                       command=lambda: controller.show_frame("StartPage"))
        buttonRegistration.pack()

<<<<<<< HEAD
class PageSix(tk.Frame): # Login to Existing Profile
    def __init__(self, parent, controller):
        def get_profile_ID(i):
            print("Profile ID in Login to Existing Profile is:",i)
            global current_profile_ID
            current_profile_ID = i
            print("The current_profile_ID is:", current_profile_ID)

        def refresh_profiles():
            print("Does this print 1")
            there_are_existing_profiles, loaded_profiles = load_existing_profiles()
            # Destroy the existing stuff
            for widget in PageFour.winfo_children(self):
                widget.destroy()

            label = tk.Label(self, text="Please select your profile", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            print("len of loaded profiles here is:", len(loaded_profiles["profiles"]))
            for i in range(len(loaded_profiles["profiles"])):
                # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
                button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"], command=lambda name=i: [get_profile_ID(name), controller.show_frame("PageSeven")])

                button.pack()
            button1 = tk.Button(self, text="Refresh", width=10, command=lambda: [refresh_profiles()])
            button1.pack()
            backButton = tk.Button(self, text="Back", width=10, command=lambda: controller.show_frame("StartPage"))
            backButton.pack()
            print("Does this print 2")
=======
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119

class PageSix(tk.Frame):  # Login to Existing Profile
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please select your profile", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global there_are_existing_profiles
        global loaded_profiles
        there_are_existing_profiles, loaded_profiles = load_existing_profiles()
<<<<<<< HEAD
        for i in range(len(loaded_profiles["profiles"])):
            # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
            button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"], command=lambda name=i: [get_profile_ID(name), controller.show_frame("PageSeven")])
            button.pack()
        button1 = tk.Button(self, text="Refresh", width=10, command=lambda: [refresh_profiles()])
        button1.pack()
        backButton = tk.Button(self, text="Back", width=10, command=lambda: controller.show_frame("StartPage"))
        backButton.pack()
=======
        if (there_are_existing_profiles):
            for i in range(len(loaded_profiles["profiles"])):
                # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
                button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"],
                                   command=lambda name=i: [get_profile_ID(name), controller.show_frame("PageSeven")])
                button.pack()
        else:
            label2 = tk.Label(self, text="No existing profiles...\nPlease register a profile first",
                              font=controller.title_font)
            label2.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(self, text="Back", width=8,
                            command=lambda: controller.show_frame("StartPage"))
        button2.pack()
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119

        def get_profile_ID(i):
            global current_profile_ID
            current_profile_ID = i
            label = tk.Label(self, text="Please select your profile", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            if there_are_existing_profiles:
                for i in range(len(loaded_profiles["profiles"])):
                    # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
                    button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"],
                                       command=lambda name=i: [get_profile_ID(name),
                                                               controller.show_frame("PageSeven")])
                    button.pack()
            else:
                label2 = tk.Label(self, text="No existing profiles...\nPlease register a profile first",
                                  font=controller.title_font)
                label2.pack(side="top", fill="x", pady=10)
            button2 = tk.Button(self, text="Back", width=8,
                                command=lambda: controller.show_frame("StartPage"))
            button2.pack()


class PageSeven(tk.Frame):  # Login Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global current_profile_ID
        print("current_profile_ID in Login Successful page is:", current_profile_ID)
<<<<<<< HEAD
        label1 = tk.Label(self, textvariable=var)
        label1.pack()
        button = tk.Button(self, text="Home", width=12, command=lambda: [restore_default_text(), controller.show_frame("PageEight")])
=======
        if there_are_existing_profiles:
            label2 = tk.Label(self, text="Welcome " + loaded_profiles["profiles"][current_profile_ID]["name"] + "!",
                              font=controller.title_font)
            label2.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home Page", width=12, command=lambda: [controller.show_frame("PageEight")])
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119
        button.pack()


class PageEight(tk.Frame):  # Home Page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Home", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        if there_are_existing_profiles:
            label1 = tk.Label(self, text="Welcome " + loaded_profiles["profiles"][current_profile_ID]["name"] + "!",
                              font=controller.title_font)
            label1.pack()
        button1 = tk.Button(self, text="Budget Manager", width=17, command=lambda: [update_budget_manager_home_page(),
                                                                                    controller.show_frame(
                                                                                        "BudgetManagerHomePage")])
        button1.pack()
        button2 = tk.Button(self, text="Stock Market", width=17,
                            command=lambda: controller.show_frame("StockMarketHomePage"))
        button2.pack()
        button3 = tk.Button(self, text="Settings", width=17, command=lambda: controller.show_frame("PageNine"))
        button3.pack()
        button4 = tk.Button(self, text="Logout", width=17, command=lambda: controller.show_frame("StartPage"))
        button4.pack()

        def update_budget_manager_home_page():  # Removes need for refresh button on PageSix
            app.frames["BudgetManagerHomePage"].destroy()
            app.frames["BudgetManagerHomePage"] = BudgetManagerHomePage(parent, controller)
            app.frames["BudgetManagerHomePage"].grid(row=0, column=0, sticky="nsew")


class PageNine(tk.Frame):  # Settings - Michael
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Settings", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="")
        label1.pack()
        button1 = tk.Button(self, text="Change Profile Name", width=21,
                            command=lambda: controller.show_frame("PageTen"))
        button1.pack()
        button2 = tk.Button(self, text="Change enabled features", width=21,
                            command=lambda: controller.show_frame("PageTwelve"))
        button2.pack()
        button3 = tk.Button(self, text="Exit Settings", width=21, command=lambda: controller.show_frame("PageEight"))
        button3.pack()


class PageTen(tk.Frame):  # Settings - Change Name
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Please enter your new name")
        label1.pack()
        new_name_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_name_var)
        entry.pack()
        button = tk.Button(self, text="Next", command=lambda: [store_name(new_name_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("PageNine")])
        button1.pack()

        def store_name(new_name_var):
            name_already_taken = False
            name = new_name_var.get()
            list_of_existing_profile_names = []
            there_are_existing_profiles, loaded_profiles = load_existing_profiles()
            for i in range(len(loaded_profiles["profiles"])):
                list_of_existing_profile_names.append(loaded_profiles["profiles"][i]["name"])
            global new_name
            new_name = name
            if name in list_of_existing_profile_names:
                name_already_taken = True
            if name.isspace() or name == "" or name_already_taken:  # invalid
                # Destroy the existing stuff
                for widget in PageTwo.winfo_children(self):
                    widget.destroy()
                if name.isspace() or name == "":
                    label1 = tk.Label(self, text="Please enter non blank name")
                    label1.pack()
                elif name_already_taken:
                    label1 = tk.Label(self, text="Please choose another name - name already taken")
                    label1.pack()
                new_name_var = tk.StringVar()
                entry = tk.Entry(self, width=15, textvariable=new_name_var)
                entry.pack()
                button = tk.Button(self, text="Next", command=lambda: [store_name(new_name_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("PageNine")])
                button1.pack()
            else:  # Valid
                # Now update profiles.json with new name
                print("Valid name")
                with open('profiles.json', "r+") as file:
                    loaded_profiles = json.load(file)
                    loaded_profiles["profiles"][current_profile_ID]["name"] = new_name
                os.remove("profiles.json")
                with open("profiles.json", "w") as file:
                    json.dump(loaded_profiles, file, indent=2, sort_keys=False)
                controller.show_frame("PageEleven")


class PageEleven(tk.Frame):  # Name change Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Name Change Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home", command=lambda: controller.show_frame("PageEight"))
        button.pack()


class PageTwelve(tk.Frame):  # Settings - Choose Enabled Features
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Change Features", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # Budget Manager descriptions
        label1 = tk.Label(self, text="1. The Budget Manager allows users to:")
        label1.pack()
        label2 = tk.Label(self, text="- Set their current balance")
        label2.pack()
        label3 = tk.Label(self, text="- Set a target balance")
        label3.pack()
        label4 = tk.Label(self, text="- View helpful financial notifications")
        label4.pack()
        label5 = tk.Label(self, text="- Keep track of deposits, withdrawals, and recurring expenses")
        label5.pack()

        labelSpace = tk.Label(self, text="")
        labelSpace.pack()

        # Stock Market tool descriptions
        label6 = tk.Label(self, text="2. The Stock Market Tool allows users to:")
        label6.pack()
        label7 = tk.Label(self,
                          text="- Select a sector to focus on that will filter for news that is specific to that sector")
        label7.pack()
        label8 = tk.Label(self, text="- Allow users to view a list of stocks and their recent performance")
        label8.pack()
        label9 = tk.Label(self,
                          text="- Allows users to view a news feed regarding recent events in the general stock market")
        label9.pack()

        # End of descriptions
        label10 = tk.Label(self, text="Please check off the features you would like to enable (Can change later)")
        label10.pack()

        # Checkboxes
        feature1_var = tk.IntVar()
        feature2_var = tk.IntVar()
        checkbutton1 = tk.Checkbutton(self, text="Budget Manager", variable=feature1_var)
        checkbutton1.pack()
        checkbutton2 = tk.Checkbutton(self, text="Stock Market Tool", variable=feature2_var)
        checkbutton2.pack()

        button = tk.Button(self, text="Next", command=lambda: [check_valid_input(self, feature1_var, feature2_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("PageNine")])
        button1.pack()

        def check_valid_input(self, feature1_var, feature2_var):
            global new_enabled_features
            new_enabled_features = []
            if feature1_var.get():
                new_enabled_features.append("1")
            if feature2_var.get():
                new_enabled_features.append("2")
            if not new_enabled_features:  # If user didnt select any features
                # Destroy the existing stuff
                for widget in PageTwo.winfo_children(self):
                    widget.destroy()
                label = tk.Label(self, text="Change Features", font=controller.title_font)
                label.pack(side="top", fill="x", pady=10)

                # Budget Manager descriptions
                label1 = tk.Label(self, text="1. The Budget Manager allows users to:")
                label1.pack()
                label2 = tk.Label(self, text="- Set their current balance")
                label2.pack()
                label3 = tk.Label(self, text="- Set a target balance")
                label3.pack()
                label4 = tk.Label(self, text="- View helpful financial notifications")
                label4.pack()
                label5 = tk.Label(self, text="- Keep track of deposits, withdrawals, and recurring expenses")
                label5.pack()
                labelSpace = tk.Label(self, text="")
                labelSpace.pack()
                # Stock Market tool descriptions
                label6 = tk.Label(self, text="2. The Stock Market Tool allows users to:")
                label6.pack()
                label7 = tk.Label(self,
                                  text="- Select a sector to focus on that will filter for news that is specific to that sector")
                label7.pack()
                label8 = tk.Label(self, text="- Allow users to view a list of stocks and their recent performance")
                label8.pack()
                label9 = tk.Label(self,
                                  text="- Allows users to view a news feed regarding recent events in the general stock market")
                label9.pack()
                labelSpace = tk.Label(self, text="")
                labelSpace.pack()
                # End of descriptions
                label10 = tk.Label(self,
                                   text="CHECK OFF AT LEAST 1 BOX - Please check off the features you would like to enable (Can change later)")
                label10.pack()

                # Checkboxes
                feature1_var = tk.IntVar()
                feature2_var = tk.IntVar()
                checkbutton1 = tk.Checkbutton(self, text="Budget Manager", variable=feature1_var)
                checkbutton1.pack()
                checkbutton2 = tk.Checkbutton(self, text="Stock Market Tool", variable=feature2_var)
                checkbutton2.pack()

                button = tk.Button(self, text="Next",
                                   command=lambda: [check_valid_input(self, feature1_var, feature2_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("PageNine")])
                button1.pack()
            else:  # Valid user input
                self.store_details(feature1_var, feature2_var)
                controller.show_frame("PageThirteen")

    def store_details(self, feature1_var, feature2_var):
        # Now update profiles.json with new features
        with open('profiles.json', "r+") as file:
            loaded_profiles = json.load(file)
            loaded_profiles["profiles"][current_profile_ID]["features"] = new_enabled_features
        os.remove("profiles.json")
        with open("profiles.json", "w") as file:
            json.dump(loaded_profiles, file, indent=2, sort_keys=False)


class PageThirteen(tk.Frame):  # Enabled Features Change Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enabled Features Change Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home", command=lambda: controller.show_frame("PageEight"))
        button.pack()


"""STOCK MARKET SECTION"""


class StockMarketHomePage(tk.Frame):  # Stock Market Home Page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Stock Market", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Sectors", width=20, command=lambda: controller.show_frame("SMSectorsPage"))
        button1.pack()
        button2 = tk.Button(self, text="Companies and Tickers", width=20,
                            command=lambda: controller.show_frame("SMCompaniesAndTickersPage"))
        button2.pack()
<<<<<<< HEAD
        button3 = tk.Button(self, text="Search Company", width=20, command=lambda: controller.show_frame("SMCompanySearchPage"))
=======
        button3 = tk.Button(self, text="Search Company", width=20,
                            command=lambda: controller.show_frame("SMSymbolLookupPage"))
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119
        button3.pack()
        button4 = tk.Button(self, text="News and Articles", width=20,
                            command=lambda: controller.show_frame("SMNewsAndArticlesPage"))
        button4.pack()
        """
        button5 = tk.Button(self, text="Saved Companies and Tickers", width=25, command=lambda: controller.show_frame("SMSavedCompaniesAndTickersPage"))
        button5.pack()
        """
        button6 = tk.Button(self, text="Exit", width=20, command=lambda: controller.show_frame("PageEight"))
        button6.pack()


class SMSectorsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Sectors", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        feature1_var = tk.IntVar()
        feature2_var = tk.IntVar()
        feature3_var = tk.IntVar()
        feature4_var = tk.IntVar()
        feature5_var = tk.IntVar()
        feature6_var = tk.IntVar()
        feature7_var = tk.IntVar()
        feature8_var = tk.IntVar()
        feature9_var = tk.IntVar()
        feature10_var = tk.IntVar()
        feature11_var = tk.IntVar()

        checkButton1 = tk.Checkbutton(self, text="Energy", variable=feature1_var)
        checkButton1.pack()
        checkButton2 = tk.Checkbutton(self, text="Materials", variable=feature2_var)
        checkButton2.pack()
        checkButton3 = tk.Checkbutton(self, text="Industrials", variable=feature3_var)
        checkButton3.pack()
        checkButton4 = tk.Checkbutton(self, text="Utilities", variable=feature4_var)
        checkButton4.pack()
        checkButton5 = tk.Checkbutton(self, text="Healthcare", variable=feature5_var)
        checkButton5.pack()
        checkButton6 = tk.Checkbutton(self, text="Financials", variable=feature6_var)
        checkButton6.pack()
        checkButton7 = tk.Checkbutton(self, text="Consumer Discretionary", variable=feature7_var)
        checkButton7.pack()
        checkButton8 = tk.Checkbutton(self, text="Consumer Staples", variable=feature8_var)
        checkButton8.pack()
        checkButton9 = tk.Checkbutton(self, text="Information Technology", variable=feature9_var)
        checkButton9.pack()
        checkButton10 = tk.Checkbutton(self, text="Communication Services", variable=feature10_var)
        checkButton10.pack()
        checkButton11 = tk.Checkbutton(self, text="Real Estate", variable=feature11_var)
        checkButton11.pack()

        confirmButton = tk.Button(self, text="Done", command=lambda: controller.show_frame("StockMarketHomePage"))
        confirmButton.pack()


# Stock Market Companies and Tickers
class SMCompaniesAndTickersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Companies and Tickers", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        doneButton = tk.Button(self, text="Done", width=10,
                               command=lambda: controller.show_frame("StockMarketHomePage"))
        doneButton.pack(side=TOP, anchor=NW)

        scroll_bar = Scrollbar(self)
        scroll_bar.pack(side=RIGHT, fill=Y)

        listBox = tk.Listbox(self, yscrollcommand=scroll_bar.set)
        listBox.config(height=500)

        generatedSymbols = getSymbols()

        for ticker in range(0, 499):
            description = generatedSymbols[ticker]['description']
            symbol = generatedSymbols[ticker]['symbol']
            listBox.insert(END, f'Name: {description}')
            listBox.insert(END, f'Symbol: {symbol}')
            listBox.insert(END, '')

        # Functions to generate different numbers of results per page
        """
        def show25(generatedSymbols):
            listBox = tk.Listbox(self, yscrollcommand=scroll_bar.set)
            listBox.config(height=500)
            for ticker in range(0, 24):
                description = generatedSymbols[ticker]['description']
                symbol = generatedSymbols[ticker]['symbol']

                listBox.insert(END, f'Name: {description}')
                listBox.insert(END, f'Symbol: {symbol}')
                listBox.insert(END, '')

        def show50(generatedSymbols):
            listBox = tk.Listbox(self, yscrollcommand=scroll_bar.set)
            listBox.config(height=500)
            for ticker in range(0, 49):
                description = generatedSymbols[ticker]['description']
                symbol = generatedSymbols[ticker]['symbol']

                listBox.insert(END, f'Name: {description}')
                listBox.insert(END, f'Symbol: {symbol}')
                listBox.insert(END, '')

        def show100(generatedSymbols):
            listBox = tk.Listbox(self, yscrollcommand=scroll_bar.set)
            listBox.config(height=500)
            for ticker in range(0, 99):
                description = generatedSymbols[ticker]['description']
                symbol = generatedSymbols[ticker]['symbol']

                listBox.insert(END, f'Name: {description}')
                listBox.insert(END, f'Symbol: {symbol}')
                listBox.insert(END, '')
        """

        # # Per Page buttons
        """
        show25Button = tk.Button(self, width=10, text='Show 25', command=lambda: show25(generatedSymbols))
        show25Button.pack(side=TOP, anchor=NW)
        show50Button = tk.Button(self, width=10, text='Show 50', command=lambda: show50(generatedSymbols))
        show50Button.pack(side=TOP, anchor=NW)
        show100Button = tk.Button(self, width=10, text='Show 100', command=lambda: show100(generatedSymbols))
        show100Button.pack(side=TOP, anchor=NW)
        """

        listBox.pack(side=TOP, fill=BOTH)
        scroll_bar.config(command=listBox.yview)

<<<<<<< HEAD
class SMCompanySearchPage(tk.Frame):
=======

class SMSymbolLookupPage(tk.Frame):
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Saved Companies and Tickers", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

<<<<<<< HEAD
        def getTicker(ticker):
            detailsRequest = f'https://finnhub.io/api/v1/stock/profile2?symbol={ticker}&token={FinnhubIOKey}'
            detailsResponse = requests.get(detailsRequest)
            detailsJSON = detailsResponse.json()
=======
        searchBoxInstructions = tk.Label(self,
                                         text="Search for your desired Companies and Tickers, separated with a comma")
        searchBoxInstructions.pack()
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119

            nameLabel = tk.Label(self, text=f'{ticker}')
            nameLabel.pack()

<<<<<<< HEAD
        searchBoxInstructions = tk.Label(self, text="Search for Companies and Tickers by Ticker")
        searchBoxInstructions.pack()
        ticker = tk.StringVar()
        searchBox = tk.Entry(self, textvariable=ticker)
        searchBox.pack()
        searchLabel = tk.Button(self, text="Search", width=7, command=partial(getTicker, ticker))
=======
        searchLabel = tk.Button(self, text="Search", width=7)
>>>>>>> 5cf816662ad34ad68932ad0318dec4efa3e74119
        searchLabel.pack()

        confirmButton = tk.Button(self, text="Done", width=7,
                                  command=lambda: controller.show_frame("StockMarketHomePage"))
        confirmButton.pack()


# Stock Market News and Articles
class SMNewsAndArticlesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="News and Articles", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        confirmButton = tk.Button(self, text="Done", command=lambda: controller.show_frame("StockMarketHomePage"))
        confirmButton.pack(side=TOP, anchor=NW)

        scroll_bar = Scrollbar(self)
        scroll_bar.pack(side=RIGHT, fill=Y)

        listBox = tk.Listbox(self, yscrollcommand=scroll_bar.set)
        listBox.config(height=500)

        def openLink(url):
            webbrowser.open_new(url)

        generatedArticles = getMarketNews()
        for article in range(len(generatedArticles)):
            imageLink = generatedArticles[article]['image']
            headline = generatedArticles[article]['headline']
            datetimeTimeStamp = generatedArticles[article]['datetime']
            summary = generatedArticles[article]['summary']
            url = generatedArticles[article]['url']

            datetime = dt.fromtimestamp(datetimeTimeStamp)

            listBox.insert(END, f'Headline: {headline}')
            listBox.insert(END, f'Date: {datetime}')
            listBox.insert(END, f'Summary: {summary}')
            listBox.insert(END, f'Link: {url}')
            listBox.insert(END, '')

            """
            articleHeadline = tk.Label(self, text=f'{headline}', anchor="e", justify=LEFT)
            articleHeadline.pack()
            articleDate = tk.Label(self, text=f'{datetime}')
            articleDate.pack()
            articleSummary = tk.Label(self, text=f'{summary}')
            articleSummary.pack()
            articleURL = tk.Label(self, text=f'{url}', fg="blue", cursor="hand2")
            articleURL.pack()
            articleURL.bind("<Button-1>", lambda e: openLink(f'{url}'))
            articleSpace = tk.Label(self, text='')
            articleSpace.pack()
            """

        listBox.pack(side=TOP, fill=BOTH)
        scroll_bar.config(command=listBox.yview)


"""
# Stock Market Saved Companies and Tickers
class SMSavedCompaniesAndTickersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Saved Companies and Tickers", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        confirmButton = tk.Button(self, text="Done", command=lambda: controller.show_frame("StockMarketHomePage"))
        confirmButton.pack()
"""
"""END OF STOCK MARKET SECTION"""


class BudgetManagerHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Budget Manager", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global there_are_existing_profiles
        global loaded_profiles
        there_are_existing_profiles, loaded_profiles = load_existing_profiles()
        if there_are_existing_profiles:
            label = tk.Label(self, text="Your current balance is:")
            label.pack(side="top", fill="x", pady=10)
            label = tk.Label(self, text=loaded_profiles["profiles"][current_profile_ID]["total_balance"])
            label.pack(side="top", fill="x", pady=10)
            label = tk.Label(self, text="Your current budget is:")
            label.pack(side="top", fill="x", pady=10)
            label = tk.Label(self, text=loaded_profiles["profiles"][current_profile_ID]["budget"])
            label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, width=18, text="Adjust total balance",
                            command=lambda: [update_BMAdjustBalance(), controller.show_frame("BMAdjustBalance")])
        button2 = tk.Button(self, width=18, text="Adjust budget",
                            command=lambda: [update_BMAdjustBudget(), controller.show_frame("BMAdjustBudget")])
        button3 = tk.Button(self, width=18, text="Enter a deposit",
                            command=lambda: [update_BMEnterDeposit(), controller.show_frame("BMEnterDeposit")])
        button4 = tk.Button(self, width=18, text="Enter an expense",
                            command=lambda: [update_BMEnterExpense(), controller.show_frame("BMEnterExpense")])
        button5 = tk.Button(self, width=18, text="View full budget history",
                            command=lambda: [update_BMBudgetHistory(), controller.show_frame("BMBudgetHistory")])
        button7 = tk.Button(self, width=18, text="Exit Budget Manager",
                            command=lambda: controller.show_frame("PageEight"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button7.pack()

        # Show a notification
        label0 = tk.Label(self, text="")
        label0.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text=self.notification())
        label1.pack(side="top", fill="x", pady=10)

        def update_BMBudgetHistory():
            app.frames["BMBudgetHistory"].destroy()
            app.frames["BMBudgetHistory"] = BMBudgetHistory(parent, controller)
            app.frames["BMBudgetHistory"].grid(row=0, column=0, sticky="nsew")

        def update_BMAdjustBalance():
            app.frames["BMAdjustBalance"].destroy()
            app.frames["BMAdjustBalance"] = BMAdjustBalance(parent, controller)
            app.frames["BMAdjustBalance"].grid(row=0, column=0, sticky="nsew")

        def update_BMAdjustBudget():
            app.frames["BMAdjustBudget"].destroy()
            app.frames["BMAdjustBudget"] = BMAdjustBudget(parent, controller)
            app.frames["BMAdjustBudget"].grid(row=0, column=0, sticky="nsew")

        def update_BMEnterDeposit():
            app.frames["BMEnterDeposit"].destroy()
            app.frames["BMEnterDeposit"] = BMEnterDeposit(parent, controller)
            app.frames["BMEnterDeposit"].grid(row=0, column=0, sticky="nsew")

        def update_BMEnterExpense():
            app.frames["BMEnterExpense"].destroy()
            app.frames["BMEnterExpense"] = BMEnterExpense(parent, controller)
            app.frames["BMEnterExpense"].grid(row=0, column=0, sticky="nsew")

    def notification(self):
        x = random.randint(1, 5)  # generate random int between 1 and 4
        print("the random number is:", x)
        if x == 1:
            if there_are_existing_profiles:
                if loaded_profiles["profiles"][current_profile_ID]["total_balance"] > 3400:
                    return "You have more money than the average American has in the bank (> $3,400)"
                else:
                    return "You have less money than the average American has in the bank (< $3,400)"
        elif x == 2:
            if there_are_existing_profiles:
                if loaded_profiles["profiles"][current_profile_ID]["budget"] > 5102:
                    return "The average american spends $5,102 in a month. Your budget is currently more than that"
                else:
                    return "The average american spends $5,102 in a month. Your budget is currently less than that"
        elif x == 3:
            return "Are you taking into consideration your retirement plan?"
        elif x == 4:
            return "Only 30% of American households have a long-term financial plan"
        else:
            return ""


class BMAdjustBalance(tk.Frame):  # Adjust balance
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Please enter your new balance")
        label1.pack()
        new_balance_var = tk.DoubleVar()
        entry = tk.Entry(self, width=15, textvariable=new_balance_var)
        entry.pack()
        button = tk.Button(self, text="Done", command=lambda: [check_valid_input(new_balance_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("BudgetManagerHomePage")])
        button1.pack()

        def check_valid_input(new_balance_var):
            try:
                balance = new_balance_var.get()
                if balance < 0:
                    print("balance is number but is negative")
                    raise ValueError('balance is number but is negative')
                balance = round(balance, 2)  # Rounds balance to 2 decimal places
                global new_balance
                new_balance = balance
                # Now update profiles.json with new balance
                with open('profiles.json', "r+") as file:
                    loaded_profiles = json.load(file)
                    loaded_profiles["profiles"][current_profile_ID]["total_balance"] = new_balance
                os.remove("profiles.json")
                with open("profiles.json", "w") as file:
                    json.dump(loaded_profiles, file, indent=2, sort_keys=False)
                update_budget_manager_home_page()
                controller.show_frame("BudgetManagerHomePage")
            except:
                print("invalid new_balance_var inputted - running except code")
                for widget in BMAdjustBalance.winfo_children(self):
                    widget.destroy()
                label1 = tk.Label(self, text="Please enter a valid balance")
                label1.pack()
                new_balance_var = tk.DoubleVar()
                entry = tk.Entry(self, width=15, textvariable=new_balance_var)
                entry.pack()
                button = tk.Button(self, text="Done", command=lambda: [check_valid_input(new_balance_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel",
                                    command=lambda: [controller.show_frame("BudgetManagerHomePage")])
                button1.pack()

        def update_budget_manager_home_page():
            app.frames["BudgetManagerHomePage"].destroy()
            app.frames["BudgetManagerHomePage"] = BudgetManagerHomePage(parent, controller)
            app.frames["BudgetManagerHomePage"].grid(row=0, column=0, sticky="nsew")


class BMAdjustBudget(tk.Frame):  # Adjust budget
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Please enter your new budget")
        label1.pack()
        new_budget_var = tk.DoubleVar()
        entry = tk.Entry(self, width=15, textvariable=new_budget_var)
        entry.pack()
        button = tk.Button(self, text="Done",
                           command=lambda: [check_valid_input(new_budget_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("BudgetManagerHomePage")])
        button1.pack()

        def update_budget_manager_home_page():  # Removes need for refresh button on PageSix
            app.frames["BudgetManagerHomePage"].destroy()
            app.frames["BudgetManagerHomePage"] = BudgetManagerHomePage(parent, controller)
            app.frames["BudgetManagerHomePage"].grid(row=0, column=0, sticky="nsew")

        def check_valid_input(new_budget_var):
            try:
                print("i will now test the .get()")
                budget = new_budget_var.get()
                print("new_budget_var succeeds the .get call")
                if budget < 0:
                    print("budget is number but is negative")
                    raise ValueError('budget is number but is negative')
                print("I got past the if statement")
                budget = round(budget, 2)  # Rounds budget to 2 decimal places
                global new_budget
                new_budget = budget
                # Now update profiles.json with new balance
                with open('profiles.json', "r+") as file:
                    loaded_profiles = json.load(file)
                    loaded_profiles["profiles"][current_profile_ID]["budget"] = new_budget
                os.remove("profiles.json")
                with open("profiles.json", "w") as file:
                    json.dump(loaded_profiles, file, indent=2, sort_keys=False)
                update_budget_manager_home_page()
                controller.show_frame("BudgetManagerHomePage")
            except:
                print("invalid new_budget_var inputted")
                for widget in BMAdjustBudget.winfo_children(self):
                    widget.destroy()
                label1 = tk.Label(self, text="Please enter a valid budget")
                label1.pack()
                new_budget_var = tk.DoubleVar()
                entry = tk.Entry(self, width=15, textvariable=new_budget_var)
                entry.pack()
                button = tk.Button(self, text="Next", command=lambda: [check_valid_input(new_budget_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel",
                                    command=lambda: [controller.show_frame("BudgetManagerHomePage")])
                button1.pack()


class BMEnterDeposit(tk.Frame):  # Enter a deposit
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="What is the deposit?")
        label1.pack()
        new_deposit_name_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_deposit_name_var)
        entry.pack()
        label2 = tk.Label(self, text="Enter in the monetary amount")
        label2.pack()
        new_deposit_value_var = tk.DoubleVar()
        entry = tk.Entry(self, width=15, textvariable=new_deposit_value_var)
        entry.pack()
        label3 = tk.Label(self, text="Enter in the date of deposit")
        label3.pack()
        new_deposit_date_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_deposit_date_var)
        entry.pack()
        button = tk.Button(self, text="Confirm",
                           command=lambda: [
                               check_valid_input(new_deposit_name_var, new_deposit_value_var, new_deposit_date_var)])
        button.pack()
        button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("BudgetManagerHomePage")])
        button1.pack()

        def check_valid_input(new_deposit_name_var, new_deposit_value_var, new_deposit_date_var):  # Checks all 3 fields
            valid_name = False
            valid_amount = False
            valid_date = False
            # First check name
            try:
                name = new_deposit_name_var.get()
                if name.isspace() or name == "":
                    print("Invalid name - it's blank")
                    raise ValueError("Invalid name - it's blank")
                valid_name = True
            except:
                print("Invalid name")
            # Second, check value
            try:
                value = new_deposit_value_var.get()
                if value < 0:
                    print("Invalid value - it's negative")
                    raise ValueError("Invalid value - it is negative")
                valid_amount = True
            except:
                print("Invalid value")
            # Third, check date (should not be empty)
            date = new_deposit_date_var.get()
            if date.isspace() or date == "":
                print("Date is blank - BAD")
            else:
                valid_date = True
            # Now check if all 3 conditions are true
            if valid_name and valid_amount and valid_date:  # All Valid!
                self.store_deposit_info(new_deposit_name_var, new_deposit_value_var, new_deposit_date_var)
                update_budget_manager_home_page()
                controller.show_frame("BudgetManagerHomePage")
            else:  # One or more invalid
                for widget in BMEnterDeposit.winfo_children(self):
                    widget.destroy()
                label = tk.Label(self, text="One or more inputs invalid - try again")
                label.pack()
                label1 = tk.Label(self, text="What is the deposit?")
                label1.pack()
                new_deposit_name_var = tk.StringVar()
                entry = tk.Entry(self, width=15, textvariable=new_deposit_name_var)
                entry.pack()
                label2 = tk.Label(self, text="Enter in the monetary amount")
                label2.pack()
                new_deposit_value_var = tk.DoubleVar()
                entry = tk.Entry(self, width=15, textvariable=new_deposit_value_var)
                entry.pack()
                label3 = tk.Label(self, text="Enter in the date of deposit")
                label3.pack()
                new_deposit_date_var = tk.StringVar()
                entry = tk.Entry(self, width=15, textvariable=new_deposit_date_var)
                entry.pack()
                button = tk.Button(self, text="Confirm",
                                   command=lambda: [check_valid_input(new_deposit_name_var, new_deposit_value_var,
                                                                      new_deposit_date_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
                button1.pack()

        def update_budget_manager_home_page():  # Removes need for refresh button on PageSix
            app.frames["BudgetManagerHomePage"].destroy()
            app.frames["BudgetManagerHomePage"] = BudgetManagerHomePage(parent, controller)
            app.frames["BudgetManagerHomePage"].grid(row=0, column=0, sticky="nsew")

    def store_deposit_info(self, new_deposit_name_var, new_deposit_value_var, new_deposit_date_var):
        deposit_name = new_deposit_name_var.get()
        print("new_deposit_name_var is:", deposit_name)
        global new_deposit_name
        new_deposit_name = deposit_name
        deposit_value = new_deposit_value_var.get()
        deposit_value = round(deposit_value, 2)
        print("new_depositvalue_var is:", deposit_value)
        global new_deposit_value
        new_deposit_value = deposit_value
        deposit_date = new_deposit_date_var.get()
        print("new_deposit_date_var is:", deposit_date)
        global new_deposit_date
        new_deposit_date = deposit_date
        new_deposit_info = [new_deposit_name, new_deposit_value, new_deposit_date]

        # Now update profiles.json with new deposit
        with open('profiles.json', "r+") as file:
            loaded_profiles = json.load(file)
            loaded_profiles["profiles"][current_profile_ID]["deposits"].append(new_deposit_info)
            loaded_profiles["profiles"][current_profile_ID]["total_balance"] += new_deposit_value
        os.remove("profiles.json")
        with open("profiles.json", "w") as file:
            json.dump(loaded_profiles, file, indent=2, sort_keys=False)


class BMEnterExpense(tk.Frame):  # Enter an expense
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="What is the expense?")
        label1.pack()
        new_expense_name_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_expense_name_var)
        entry.pack()
        label2 = tk.Label(self, text="Enter in the monetary amount")
        label2.pack()
        new_expense_value_var = tk.DoubleVar()
        entry = tk.Entry(self, width=15, textvariable=new_expense_value_var)
        entry.pack()
        label3 = tk.Label(self, text="Enter in the date of expense")
        label3.pack()
        new_expense_date_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_expense_date_var)
        entry.pack()
        button = tk.Button(self, width=12, text="Confirm",
                           command=lambda: [
                               check_valid_input(new_expense_name_var, new_expense_value_var, new_expense_date_var)])
        button.pack()
        button1 = tk.Button(self, width=12, text="Cancel",
                            command=lambda: [controller.show_frame("BudgetManagerHomePage")])
        button1.pack()

        def check_valid_input(new_expense_name_var, new_expense_value_var, new_expense_date_var):  # Checks all 3 fields
            valid_name = False
            valid_amount = False
            valid_date = False
            # First check name
            try:
                name = new_expense_name_var.get()
                if name.isspace() or name == "":
                    print("Invalid name - it's blank")
                    raise ValueError("Invalid name - it's blank")
                valid_name = True
            except:
                print("Invalid name")

            # Second, check value
            try:
                value = new_expense_value_var.get()
                if value < 0:
                    print("Invalid value - it's negative")
                    raise ValueError("Invalid value - it is negative")
                valid_amount = True
            except:
                print("Invalid value")

            # Third, check date (should not be empty)
            date = new_expense_date_var.get()
            if date.isspace() or date == "":
                print("Date is blank - BAD")
            else:
                valid_date = True

            # Now check if all 3 conditions are true
            if valid_name and valid_amount and valid_date:  # All Valid!
                self.store_expense_info(new_expense_name_var, new_expense_value_var, new_expense_date_var)
                update_budget_manager_home_page()
                controller.show_frame("BudgetManagerHomePage")
            else:  # One or more invalid
                for widget in BMEnterDeposit.winfo_children(self):
                    widget.destroy()
                label = tk.Label(self, text="One or more inputs invalid - try again")
                label.pack()
                label1 = tk.Label(self, text="What is the deposit?")
                label1.pack()
                new_depositname_var = tk.StringVar()
                entry = tk.Entry(self, width=15, textvariable=new_depositname_var)
                entry.pack()
                label2 = tk.Label(self, text="Enter in the monetary amount")
                label2.pack()
                new_depositvalue_var = tk.DoubleVar()
                entry = tk.Entry(self, width=15, textvariable=new_depositvalue_var)
                entry.pack()
                label3 = tk.Label(self, text="Enter in the date of deposit")
                label3.pack()
                new_depositdate_var = tk.StringVar()
                entry = tk.Entry(self, width=15, textvariable=new_depositdate_var)
                entry.pack()
                button = tk.Button(self, text="Confirm",
                                   command=lambda: [check_valid_input(new_depositname_var, new_depositvalue_var,
                                                                      new_depositdate_var)])
                button.pack()
                button1 = tk.Button(self, text="Cancel", command=lambda: [controller.show_frame("StartPage")])
                button1.pack()

        def update_budget_manager_home_page():  # Removes need for refresh button on PageSix
            app.frames["BudgetManagerHomePage"].destroy()
            app.frames["BudgetManagerHomePage"] = BudgetManagerHomePage(parent, controller)
            app.frames["BudgetManagerHomePage"].grid(row=0, column=0, sticky="nsew")

    def store_expense_info(self, new_expensename_var, new_expensevalue_var, new_expensedate_var):
        expensename = new_expensename_var.get()
        print("new_expensename_var is:", expensename)
        global new_expense_name
        new_expense_name = expensename

        expense_value = new_expensevalue_var.get()
        expense_value = round(expense_value, 2)
        print("new_expensevalue_var is:", expense_value)
        global new_expense_value
        new_expense_value = expense_value

        expense_date = new_expensedate_var.get()
        print("new_expensedate_var is:", expense_date)
        global new_expense_date
        new_expense_date = expense_date

        new_expense_info = [new_expense_name, new_expense_value, new_expense_date]

        # Now update profiles.json with new expense
        with open('profiles.json', "r+") as file:
            loaded_profiles = json.load(file)
            loaded_profiles["profiles"][current_profile_ID]["expenses"].append(new_expense_info)
            loaded_profiles["profiles"][current_profile_ID]["total_balance"] -= new_expense_value
            loaded_profiles["profiles"][current_profile_ID]["budget"] -= new_expense_value
        os.remove("profiles.json")
        with open("profiles.json", "w") as file:
            json.dump(loaded_profiles, file, indent=2, sort_keys=False)


class BMBudgetHistory(tk.Frame):  # Budget History
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Budget History", font=controller.title_font)
        label.pack()
        button = tk.Button(self, text="Back", command=lambda: [update_budget_manager_home_page(),
                                                               controller.show_frame("BudgetManagerHomePage")])
        button.pack()

        if there_are_existing_profiles:
            if len(loaded_profiles["profiles"][current_profile_ID]["expenses"]) < 1 and len(
                    loaded_profiles["profiles"][current_profile_ID]["deposits"]) < 1:
                print("No history to show")
                label = tk.Label(self, text="NO HISTORY TO SHOW")
                label.pack()
            else:
                self.scrollbar = Scrollbar(self, orient='vertical')

                self.list1 = Listbox(self, yscrollcommand=self.yscroll1)
                self.list1.pack(fill='y', side='left')

                self.list2 = Listbox(self, yscrollcommand=self.yscroll2)
                self.list2.pack(fill='both', side='left')

                self.list3 = Listbox(self, yscrollcommand=self.yscroll3)
                self.list3.pack(fill='both', side='left')

                self.scrollbar.config(command=self.yview)
                self.scrollbar.pack(side='right', fill='y')

                if there_are_existing_profiles:
                    # fill the listboxes with stuff
                    for x in range(len(loaded_profiles["profiles"][current_profile_ID]["expenses"])):
                        self.list1.insert('end', loaded_profiles["profiles"][current_profile_ID]["expenses"][x][0])
                        self.list2.insert('end', -loaded_profiles["profiles"][current_profile_ID]["expenses"][x][1])
                        self.list3.insert('end', loaded_profiles["profiles"][current_profile_ID]["expenses"][x][2])
                    for x in range(len(loaded_profiles["profiles"][current_profile_ID]["deposits"])):
                        self.list1.insert('end', loaded_profiles["profiles"][current_profile_ID]["deposits"][x][0])
                        self.list2.insert('end', loaded_profiles["profiles"][current_profile_ID]["deposits"][x][1])
                        self.list3.insert('end', loaded_profiles["profiles"][current_profile_ID]["deposits"][x][2])

        def update_budget_manager_home_page():  # Removes need for refresh button on PageSix
            app.frames["BudgetManagerHomePage"].destroy()
            app.frames["BudgetManagerHomePage"] = BudgetManagerHomePage(parent, controller)
            app.frames["BudgetManagerHomePage"].grid(row=0, column=0, sticky="nsew")

    def yscroll1(self, *args):
        if self.list2.yview() != self.list1.yview():
            self.list2.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll2(self, *args):
        if self.list1.yview() != self.list2.yview():
            self.list1.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yscroll3(self, *args):
        if self.list1.yview() != self.list3.yview():
            self.list3.yview_moveto(args[0])
        self.scrollbar.set(*args)

    def yview(self, *args):
        self.list1.yview(*args)
        self.list2.yview(*args)
        self.list3.yview(*args)


if __name__ == "__main__":
    app = FiMan()
    app.title('FiMan')
    app.geometry("700x500")
    app.mainloop()
