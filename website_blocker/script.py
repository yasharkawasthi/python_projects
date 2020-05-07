# Website Blocker - Python Project

import time
from datetime import datetime as dt

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

numSites = int(input("Enter the number of websites you want to block = "))
listSites=[]

for i in range(numSites):
    site = input("Enter the URL of website you want to block = ")
    listSites.append(site)

startTime = int(input("Enter the starting hour to block the website (in 24 Hour Format) = "))
endTime = int(input("Enter the ending hour to block the website (in 24 Hour Format) = "))

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,startTime) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,endTime):
        print("Some Websites have been Blocked.")
        with open(hostsPath,'r+') as file:
            content = file.read()
            for website in listSites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("All Websites are Unblocked now.")
        with open(hostsPath,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in listSites):
                    file.write(line)
            file.truncate()
            
    time.sleep(60)

 
