# URL Shortener - Python Project

from __future__ import with_statement

import contextlib
import sys

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def shorten(url):
    requestUrl = 'http://tinyurl.com/api-create.php?url='+url
    with contextlib.closing(urlopen(requestUrl)) as response:
        return response.read().decode('utf-8')

numUrls = int(input("Enter the number of URLs you want to shorten = "))
listUrls=[]

for i in range(numUrls):
    url = input("Enter a URL to shorten: ")
    listUrls.append(url)

for i in range(numUrls):
    print (listUrls[i]+" - > ",end="")
    print (shorten(listUrls[i]))

