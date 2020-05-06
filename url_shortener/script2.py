# URL Shortener - Python Project

import pyshorteners

numUrls = int(input("Enter the number of URLs you want to shorten = "))
listUrls=[]

for i in range(numUrls):
    url = input("Enter the URL of website you want to block = ")
    listUrls.append(url)

for i in range(numUrls):
    print (listUrls[i]+" - > ",end="")
    print (pyshorteners.Shortener().tinyurl.short(listUrls[i]))
