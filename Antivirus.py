import os 
import sys 
import os.path

def Getmenu(menu, option):
        while True:
        #While loop
                menu = raw_input("Enter the Option that you would like to do: ").lower()
        #User interface that can be entered in lowercase 
                if option in "Option 1, Option2, Option3". split(" "):
        #If statement, if the user doesn't enter the following stated above then.
                        return menu
        #Return the menu, which is the user interface.

def Option1(recursion):
     class recursion:
         maindir = 'C:\Windows XP Professional\Windows XP Professional'
    #main directory. This is where the virus is held.
         extension = ['txt','log','exe']
    # The extentions that i want antivirus to find.
         discovered = {j: [] for j in extension}
    #The dict contains a  for loop and will continue finding all the extention s that are mentioned above
         excluide = ['PDF','docs','Mp3']
    #This list will exclude following suffixes
         logs = "Viruslogs.log"
    #The recursion bit of the Antivirus will produce a log of the directories and files the program visited.
         print ('Antivirus is scanning in %s' % os.path.realpath(maindir))
    #Once the scan is initalised the antivirus will print out a string with the pathname embedded.

         for dirpath, dirnames, files in os.walk(maindir):
    #For statement, will produce a tree for the progam to walk with. "os.walk" 
            for kdir in exclude:
    #Removing the directories that are contained in exclude variable
                    if kdir in dirnames:
    #Directory names must include the appropriate prefixes.
                            dirnames.remove(kdir)
    
         for title in files:
    #For loop through the titles of  the files in the current directory 
                ext = title.lower().rsplit('.',1)[-1]
    #Using a '.' the name will be spilt and contain the apporiate extension

                if ext in extention:
                        gathered[ext].append(os.path.join(dirpath, dirnames))

         titlehead = 'Search viruslog from file that was found in {}\n\n'.format(os.path.realpath(maindir))
         virusbody = ''

         for find in discovered:
             virusbody += "<< Results with extensions '%s'>>" % find
             virusbody += '\n\n%s\n\n' % '\n'.join(found[find])

            
            
            

                        

        
        
                
                
                                
                
                
