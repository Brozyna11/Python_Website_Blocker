import time 
from datetime import datetime as dt 
'''
The hosts file ("hosts.txt") is a plain-text file that contains a list of host names and their corresponding IP addresses. 
It is essentially a database of domain names that is used by the operating system for identifying and locating a host in an IP network.
'''
# location of the host files: C:\Windows\System32\drivers\etc
hosts_path = r"C:\Windows\System32\drivers\etc"
# an IP when browser will be redirected after you try to enter blocked websides
redirect = "127.0.0.1" 
website_list=["www.facebook.com","9gag.com"]

while True:
    # while loop below is checking every 5 sec if there are working hours or not in order to determine which websites should be blocked
    # if Working Hours then the code below will add the list of the websites to block to the host file 
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Working hours...")

        with open(hosts_path, 'r+') as file:
            content = file.read() # this will load whole text to the variable as a sigle string
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        # if Fun hours then program will rewrite whole host file without anything to block
        with open(hosts_path, "r+") as file:
            # this will produce a list with all lines in the file including lines with #
            content = file.readlines() 
            # move cursor to the beginning of the file
            file.seek(0) 
            for line in content:
                # program will rewrite whole file without any webstite to block
                if not any(website in line for website in website_list):
                    file.write(line)
            # deletes everything what is below cursoer
            file.truncate() 
        print("Fun hours...")
    # sleep method from time module which will run code every 5 s
    time.sleep(5) 