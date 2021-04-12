import tkinter as tk
import json, os, webbrowser, requests
from config import FinnhubIOKey
from datetime import datetime as dt
from functools import partial
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
from landing_page import load_existing_profiles
from home_page import *
from stock_market import *

# from https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# helpful with connecting textbox to button https://codeloop.org/how-to-create-textbox-in-python-tkinter/

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

        for F in (
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

class StartPage(tk.Frame): # Welcome to FiMan
    def __init__(self, parent, controller):
        def exit_program():
            exit(0)
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to FiMan! A Financial Manager Software Application")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Register", width=8, command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        button2 = tk.Button(self, text="Login", width=8, command=lambda: controller.show_frame("PageSix"))
        button2.pack()
        button3 = tk.Button(self, text="Exit", width=8, command=lambda: exit_program())
        button3.pack()

class PageOne(tk.Frame): # Register a new profile (Enter name)
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
        label1 = tk.Label(self, text="Enter Full Name")
        label1.pack()
        new_name_var = tk.StringVar()
        entry = tk.Entry(self, width=15, textvariable=new_name_var)
        entry.pack()
        button = tk.Button(self, text="Next", command=lambda: [self.store_name(new_name_var), controller.show_frame("PageTwo")])
        button.pack()

class PageTwo(tk.Frame): # Register a new profile (Choose Features)
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
        label7 = tk.Label(self, text="- Select a sector to focus on that will filter for news that is specific to that sector")
        label7.pack()
        label8 = tk.Label(self, text="- Allow users to view a list of stocks and their recent performance")
        label8.pack()
        label9 = tk.Label(self, text="- Allows users to view a news feed regarding recent events in the general stock market")
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

        button = tk.Button(self, text="Next", command=lambda: [ self.store_details(feature1_var,feature2_var), controller.show_frame("PageThree")])
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
        button = tk.Button(self, text="Next", command=lambda: [self.print_balance(new_balance_var), controller.show_frame("PageFour")])
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
        button = tk.Button(self, text="Next", command=lambda: [self.print_balance(new_balance_var), self.write_new_profile_to_file(), controller.show_frame("PageFive")])
        button.pack()

class PageFive(tk.Frame): # Registration Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registration Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        buttonHome = tk.Button(self, text="Home", width=8, command=lambda: controller.show_frame("PageEight"))
        buttonHome.pack()
        buttonRegistration = tk.Button(self, text="Landing", width=8, command=lambda: controller.show_frame("StartPage"))
        buttonRegistration.pack()

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

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please select your profile", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global there_are_existing_profiles
        global loaded_profiles
        there_are_existing_profiles, loaded_profiles = load_existing_profiles()
        for i in range(len(loaded_profiles["profiles"])):
            # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
            button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"], command=lambda name=i: [get_profile_ID(name), controller.show_frame("PageSeven")])
            button.pack()
        button1 = tk.Button(self, text="Refresh", width=10, command=lambda: [refresh_profiles()])
        button1.pack()
        backButton = tk.Button(self, text="Back", width=10, command=lambda: controller.show_frame("StartPage"))
        backButton.pack()

class PageSeven(tk.Frame): # Login Successful
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
        button = tk.Button(self, text="Home", width=12, command=lambda: [restore_default_text(), controller.show_frame("PageEight")])
        button.pack()
        button1 = tk.Button(self, text="Profile Details", width=12, command=lambda: show_profile_details())
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
        label = tk.Label(self, text="Home")
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, textvariable=var)
        label1.pack()

        button1 = tk.Button(self, text="Budget Manager", width=17, command=lambda: controller.show_frame("PageFour"))
        button1.pack()
        button2 = tk.Button(self, text="Stock Market", width=17, command=lambda: controller.show_frame("StockMarketHomePage"))
        button2.pack()
        button3 = tk.Button(self, text="Settings", width=17, command=lambda: controller.show_frame("PageNine"))
        button3.pack()
        button4 = tk.Button(self, text="Logout", width=17, command=lambda: controller.show_frame("StartPage"))
        button4.pack()
        button5 = tk.Button(self, text="View Profile Details", width=17, command=lambda: show_profile_details())
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

        button1 = tk.Button(self, text="Change Profile Name", width=21, command=lambda: controller.show_frame("PageTen"))
        button1.pack()
        button2 = tk.Button(self, text="Change enabled features", width=21, command=lambda: controller.show_frame("PageTwelve"))
        button2.pack()
        button3 = tk.Button(self, text="Exit Settings", width=21, command=lambda: controller.show_frame("PageEight"))
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
        button = tk.Button(self, text="Next", command=lambda: [self.store_name(new_name_var), controller.show_frame("PageEleven")])
        button.pack()

class PageEleven(tk.Frame): # Name change Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Name Change Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home", command=lambda: controller.show_frame("PageEight"))
        button.pack()

class PageTwelve(tk.Frame): # Settings - Choose Enabled Features
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
            label7 = tk.Label(self, text="- Select a sector to focus on that will filter for news that is specific to that sector")
            label7.pack()
            label8 = tk.Label(self, text="- Allow users to view a list of stocks and their recent performance")
            label8.pack()
            label9 = tk.Label(self, text="- Allows users to view a news feed regarding recent events in the general stock market")
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

            button = tk.Button(self, text="Next", command=lambda: [self.store_details(feature1_var, feature2_var), controller.show_frame("PageThirteen")])
            button.pack()

class PageThirteen(tk.Frame): # Enabled Features Change Successful
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enabled Features Change Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home", command=lambda: controller.show_frame("PageEight"))
        button.pack()

"""STOCK MARKET SECTION"""

class StockMarketHomePage(tk.Frame): # Stock Market Home Page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Stock Market", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Sectors", width=20, command=lambda: controller.show_frame("SMSectorsPage"))
        button1.pack()
        button2 = tk.Button(self, text="Companies and Tickers", width=20, command=lambda: controller.show_frame("SMCompaniesAndTickersPage"))
        button2.pack()
        button3 = tk.Button(self, text="Search Company", width=20, command=lambda: controller.show_frame("SMCompanySearchPage"))
        button3.pack()
        button4 = tk.Button(self, text="News and Articles", width=20, command=lambda: controller.show_frame("SMNewsAndArticlesPage"))
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

        doneButton = tk.Button(self, text="Done", width=10, command=lambda: controller.show_frame("StockMarketHomePage"))
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

class SMCompanySearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Saved Companies and Tickers", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        def getTicker(ticker):
            detailsRequest = f'https://finnhub.io/api/v1/stock/profile2?symbol={ticker}&token={FinnhubIOKey}'
            detailsResponse = requests.get(detailsRequest)
            detailsJSON = detailsResponse.json()

            nameLabel = tk.Label(self, text=f'{ticker}')
            nameLabel.pack()

        searchBoxInstructions = tk.Label(self, text="Search for Companies and Tickers by Ticker")
        searchBoxInstructions.pack()
        ticker = tk.StringVar()
        searchBox = tk.Entry(self, textvariable=ticker)
        searchBox.pack()
        searchLabel = tk.Button(self, text="Search", width=7, command=partial(getTicker, ticker))
        searchLabel.pack()

        confirmButton = tk.Button(self, text="Done", width=7, command=lambda: controller.show_frame("StockMarketHomePage"))
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

        for article in range(0, 99):
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

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("700x500")
    app.mainloop()