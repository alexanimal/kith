
Installing dependencies
====================================
Install Python 2.7 by downloading it at http://www.python.org/getit/releases/2.7.5/

For easy installation, download the zip file to your Downloads folder and type command into terminal 

    python Downloads/kith/setup.py

If there is trouble installing,

Selenium
-------------------
Install selenium by typing the command 

    sudo pip install -U selenium

Fuzzywuzzy
-----------------
Download the ZIP file at http://github.com/seatgeek/fuzzywuzzy.git#egg=fuzzywuzzy

Extract the ZIP file into your Downloads folder, and type the command

    python Downloads/fuzzywuzzy-master/setup.py install
    
or type in the command

    sudo pip install -e git+git://github.com/seatgeek/fuzzywuzzy.git#egg=fuzzywuzzy

Installation Test
----------------------
After all that, type into terminal

    python Downloads/kith/kith_test.py

If you get a pass message, you have installed everything correctly

Program Instructions
=====================================
Edit the user_info.txt file in the kith folder in your Downloads folder

It should look something like this when you are done,

Fill out the form like this:
```
Email:
test@email.com
First Name:
Hugh
Last Name:
Jass
Address Line 1:
546 Fuck Off Circle
Address Line 2:
**can be left blank**
City:
This City
ZIP Code:
11111 **must be 5 numbers**
State:
California **enter the full state name**
Phone Number:
1234567890
Credit Card Number:
0000000000000000 **must be 16 numbers**
Credit Card Expiration Month:
05 **must be 2 numbers**
Credit Card Expiration Year:
2016 *must be full year*
Credit Card Security Code:
123 **must be 3 numbers**
Shoe Size:
6.5
```
Running the Program
--------------------
type into the terminal 

    python Downloads/kith/kith-v2.py
    
you will get a menu screen that has the options 1-4
```
You Should Complete these Steps in Order
Type Item Selection Number, then Hit Enter
1. Test Links On Site
2. Set Fuzz Ratio
3. Buy Item
4. Program Test
Type 'quit' to exit.
```
type 1

the prompt will ask you to put in your item information
```
Item Name w/ dashes (ie: asics-gel-lyte-5-volcano):
```

type something like **asics-gel-lyte-V-volcano**

you will get the menu again, type 2

you will again come back to the menu, type 3

you will get a prompt that asks you to enter the shoe keywords,

enter the same thing you did before **asics-gel-lyte-V-volcano**

Testing the Program
----------------------
If you wish to test the program and make sure it works before hand,

make sure your user_info.txt file is filled out,

try it on a product already on the site, type 4 in the menu

You will get a prompt for the site url: type gazelleindoordeeppetrol-black


