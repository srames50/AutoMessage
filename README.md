# AutoMessage README
This code uses the Selenium WebDriver library to automate the process of sending a message on Google Chat. It opens a specific direct link to a chat, types a message with the current hour and hits the send button.

#Requirements
Python 3.x
Selenium WebDriver library
ChromeDriver executable for your version of Google Chrome
Google Chrome web browser installed on your machine

#Installation
Install Python 3.x from the official website: https://www.python.org/downloads/
Install the Selenium WebDriver library by running pip install selenium in your terminal/command prompt.
Download the ChromeDriver executable for your version of Google Chrome from https://sites.google.com/a/chromium.org/chromedriver/downloads and place it in a directory on your machine.
Modify the PATH variable in the code to point to the location of the ChromeDriver executable on your machine.

#Usage
Open the terminal/command prompt and navigate to the directory containing the code.
Run the command python <filename.py> to execute the code.
The code will open a new Chrome tab with saved login info, then attach functions to it using the ChromeDriver executable.
The code will then open a direct link to a specific chat in Google Chat and type a message with the current hour.
The message will be sent automatically and the program will exit.
Note: This code is specific to the author's use case and may need to be modified for your specific use case.
