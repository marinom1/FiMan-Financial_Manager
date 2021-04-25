# FiMan (Financial Manager)

## Introduction
People love money. People love saving money. People don’t love losing money. The problem is that there are so many apps and different tools to manage your finances! Therefore, there needs to be a tool that people can use to keep track and manage all your life’s earnings, spending, and savings without having to jump from app to app or website to website. Our solution is to create FiMan - ONE app where you can manage all your finances without any hassle. It has blazing fast responsiveness and contains many different useful features that users will find easy to use, including a balance tracker, a budget manager, a live stock news tracker, and budget help notifications.

## Functions
1. Create a New Profile
	* The system shall allow users to create a new profile with their name.
	* The system shall allow users to edit their personal information.
	* The system shall allow users to re-login to their user profile upon exiting application.
2.  Manage Budget
	* The system shall allow users to set the total amount of money they currently possess.
	* The system shall allow users to set a target limit that cannot be exceeded.
	* The system shall allow users to view notifications that help or advise them regarding their budget.
	* The system shall allow users to add or remove recurring expenses like daily, weekly, monthly, yearly, etc.
3. Stock Market
	* The system shall allow users to select a sector to focus on that will filter for news that is specific to that sector.
	* The system shall allow users to view a list of stocks and see their recent performance.
	* The system shall allow users to view a news feed regarding recent events in the stock market.

## Getting Started
### Installation and Setup
These instructions are designed for running this project on Windows; other operating systems may vary in set-up. 
1. Run and install Python and Pycharm Community from their respective websites.
	* Python (https://www.python.org/downloads/)
	* PyCharm Community (https://www.jetbrains.com/pycharm/download/#section=windows)
2. Download the ZIP archive of FiMan's project files from the GitHub repository.
3. Extract the ZIP to a new folder.
4. Once PyCharm is installed and running, go to File > Open and select the folder that you extracted the ZIP into.
	* If PyCharm gives you any errors or warnings regarding a missing interpreter, you may need to reinstall Python or reopen the project.
5. Go to File > Settings (CTRL+ALT+S) and select Project: [insert folder name]. 
6. Go to Python Interpreter. Here, you should see a list of packages that came with PyCharm (or packages you have, if it is a preexisting PyCharm install).
7. On the bottom of this window, click the Install icon (+).
8. Search for and select the package "requests". Click "Install Package" at the bottom of the window.
### Run
1. To run FiMan, all you need to do is right-click on "landing_page_gui.py" and select "Run". 
	* Within a few moments, the program window should appear. If it does not appear, check to see if it is running on your taskbar.
2. From here, you should then be able to register your profile and utilize the different functions in FiMan.
3. If you happen to encounter any issues or errors regarding the FinnhubIOKey, PolygonIOKey or NewsAPIKey, you may need to retreive new API keys from the following websites:
	* https://finnhub.io/
	* https://polygon.io/
	* https://newsapi.org/
4. To retrieve and replace these keys, simply click the buttons and follow the instructions on the respective websites. Once you have your new keys, you will want to edit your "config.py" file included in the project to remove the old keys and replace them with the new ones. 

## Demo video

Upload your demo video to youtube and put a link here. Basically, the video content is very much like the quick live demo of your product with the followings:
1. Introduction
2. How to run the app
3. Quick walkthrough of all the functions and their sub functions of your app one by one

Please make it short and interesting!

Sample: https://www.youtube.com/watch?v=Pr-JMqTkdEM

How to record your screen: https://www.techradar.com/how-to/record-your-screen

## Contributors

* Michael Marino (marinom1@wit.edu), Team Leader, Developer, Tester
* Ian Seto (setoi@wit.edu), Developer, Tester
* Mike Depietro (depietrom@wit.edu), Developer, Tester
