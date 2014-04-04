import os
import sys
import os.path
import logging
import time
import hashlib
import md5 
#Importing the modules 

print (time.strftime("%H:%M:%S"))
print (time.strftime("%d/%m/%Y"))
#When the program starts the user will see date and time 

print "Hello User "
print """
        
                    ,.ood888888888888boo.,
               .od888P^""            ""^Y888bo.
           .od8P''   ..oood88888888booo.    ``Y8bo.
        .odP'"  .ood8888888888888888888888boo.  "`Ybo.
      .d8'   od8'd888888888f`8888't888888888b`8bo   `Yb.
     d8'  od8^   8888888888[  `'  ]8888888888   ^8bo  `8b
   .8P  d88'     8888888888P      Y8888888888     `88b  Y8.
  d8' .d8'       `Y88888888'      `88888888P'       `8b. `8b
 .8P .88P            """"            """"            Y88. Y8.
 88  888                                              888  88
 88  888                                              888  88
 88  888.        ..                        ..        .888  88
 `8b `88b,     d8888b.od8bo.      .od8bo.d8888b     ,d88' d8'
  Y8. `Y88.    8888888888888b    d8888888888888    .88P' .8P
   `8b  Y88b.  `88888888888888  88888888888888'  .d88P  d8'
     Y8.  ^Y88bod8888888888888..8888888888888bod88P^  .8P
      `Y8.   ^Y888888888888888LS888888888888888P^   .8P'
        `^Yb.,  `^^Y8888888888888888888888P^^'  ,.dP^'
           `^Y8b..   ``^^^Y88888888P^^^'    ..d8P^'
               `^Y888bo.,            ,.od888P^'
                    "`^^Y888888888888P^^'"         
 """


def Getmenu():
        menu = raw_input("Enter the Option that you would like to do: ").lower()
#User input that can be entered in lowercase
        if menu == 'option1': #or '1':
# Decision using option 1
                Option1()
#If the user enters 1 then it will return option 1 
        elif menu == 'option2':
# Decision: if the user enters 2 or option2 
                Option2()
# Then the program will send the user to option2 
        elif menu == 'option3':
                 Option3()
        else:
                Getmenu()
#if the user doesn't enter any of the options then the program will return back to the menu 
#OPtion one is the file recursion for the virus directory.
def Option1():
        print "Scanning ......."
        
        print ""
        virusname = ''
#The virus name variable
        extension = ['sys', 'txt','exe']
# The extensions that i want to look for  using a list function
        journey = "C:\Program Files\Common Files\VMware"
# The path directory 
        for file in os.walk(journey):
# for loop that calls the file variable  in the journey variable.
                
                

                extension.append(file)
# Once the file does the walk through it will append the extention to the file.
                os.path.join

                print file
        if file in os.walk(journey):
                print "Program files"
                
# Once the file is found then the file will be printed.

                
                
                
def log(message):
# Defining the 'log' function
        file = open("C:\Users\Johnson\Documents\GitHub\antivirus\log.txt", 'r')
# The file variable is equal to the 'open' variable that calls the text file) 
        filedata = file.read()
# The variable 'filedata' calls the file variable and makes it readable
        file.close()
# Closing the file
        file = open("C:\Users\Johnson\Documents\GitHub\antivirus\log.txt", 'w')
#Opening the file and enabling the write command
# So everytime  the command runs it writes to the file.
        file.write(filedata + message)
# The file variable calls the two argumemnts
        file.close()
        
# The file has been closed.    
        
        

def Option2():
# The option2 function is defined

        foldername = "C:"
# The foldername varaible has been set
        
      
        virus = list(foldername)
# The variable 'virus'  lists all the folders in the varable  'foldername'
        shaSums = [s.split('-')[0] for s in virus]
# The varaible shaSums splits the array and then list the shaSum of the file or exe
        print virus
# Printing the list of the folder names 
        sums = raw_input
# 

        print shaSums
#Printing the Sha1 sum of  the file


def Option3():
# Defining the third Option 

        virus2 = raw_input("Search virus signature: ")
# The variable allows the user to enter an input
        if virus2 == 'search':
#the if statement calls th above variable and says if the user enters search
#then the program will print "loading and also the "SHA" hash below.
                print "Loading"
                print "5b1e068bf381c621008bfe0e1f0e0753b97b038b5f01fcad"
                               
                
               
               
        
               
                #The new variable will open the library (txt) file and read from it.
                doc = open("C:\Users\Johnson\Documents\GitHub\Antivirus\Websteriods.txt", "r")
                #When the application is being ran then the print function will call the document in the application.
                print doc.read()
                
        while True:
                
                quit = raw_input(" Would you like to close: ")
                if quit == 'yes':
                        print " Session has now terminated"
                        break 

                      

                        

                        if quit == 'No':
                                print "Re-Running Processes"
                       
                
                
                
                
def log(message):
# Defining the 'log' function
        file = open("C:\Users\Johnson\Documents\GitHub\antivirus\log.txt", 'r')
# The file variable is equal to the 'open' variable that calls the text file) 
        filedata = file.read()
# The variable 'filedata' calls the file variable and makes it readable
        file.close()
# Closing the file
        file = open("C:\Users\Johnson\Documents\GitHub\antivirus\log.txt", 'w')
#Opening the file and enabling the write command
# So everytime  the command runs it writes to the file.
        file.write(filedata + message)
# The file variable calls the two argumemnts
        file.close()
        
# The file has been closed.

"""
        Code was created by Johnson Nwamma
        If you would like to add to the code please do and email
        me at j.nwamma@wcinc.info"""
        
        
      



        
                
########################################################################
               
               
        
        
        
                      
#log('time.strftime("%H:%M:%S"))\n')
Getmenu()
Option1()
#Option2()
#md5sum()
#Option3()


