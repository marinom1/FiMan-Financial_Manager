import tkinter as tk
from tkinter import font as tkfont
import json
import os

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
    # Creates profiles.json that contains a profiles dictionary that contains an empty array for each profile
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
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive): #If making new page, be sure to add it in here
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
                            command=lambda: controller.show_frame("PageFour"))
        button3 = tk.Button(self, text="Exit FiMan", command=lambda: exit_program())
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame): #Register a new profile (Enter name)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 1 of 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label1 = tk.Label(self, text="Please enter your name")
        label1.pack()
        name = tk.StringVar()
        textbox = tk.Entry(self, width=15, textvariable=name)
        textbox.pack()
        button = tk.Button(self, text="Next",
                           command=lambda: controller.show_frame("PageTwo"))
        button.pack()


class PageTwo(tk.Frame): #Register a new profile (Choose Features)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Step 2 of 2", font=controller.title_font)
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
        checkbutton1 = tk.Checkbutton(self, text="Budget Manager")
        checkbutton1.pack()
        checkbutton2 = tk.Checkbutton(self, text="Stock Market Tool")
        checkbutton2.pack()

        button = tk.Button(self, text="Complete Registration",
                           command=lambda: controller.show_frame("PageThree"))
        button.pack()

class PageThree(tk.Frame): #Registration Successful

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registration Successful!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageFour(tk.Frame): #Login to Existing Profile

    def __init__(self, parent, controller):
        def get_profile_ID(i):
            print("Profile ID in Login to Existing Profile is:",i)
            global current_profile_ID
            current_profile_ID = i
            print("The current_profile_ID is:", current_profile_ID)

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please select your profile", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        for i in range(len(loaded_profiles["profiles"])):
            # I set the name=i so that each button will remember what its ID is. For example profile 0 should be ID 0 and profile 1 should be ID 1
            button = tk.Button(self, text=loaded_profiles["profiles"][i]["name"],
                               command=lambda name=i: [get_profile_ID(name), controller.show_frame("PageFive")])

            button.pack()


class PageFive(tk.Frame): #Login Successful

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
        label1 = tk.Label(self, textvariable=var, font=controller.title_font)
        label1.pack()
        button = tk.Button(self, text="Go to your Home Page",
                           command=lambda: [restore_default_text(), controller.show_frame("StartPage")])
        button.pack()

        button1 = tk.Button(self, text="Click to see your profile details to make sure you logged into the right profile",
                           command=lambda: show_profile_details())
        button1.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("700x500")
    app.mainloop()


