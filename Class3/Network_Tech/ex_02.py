import urllib.request
import re
import collections
collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


names = list()
count = input('Enter the count: ')
position = input('Enter the position: ')
cnt = int(count)
pos = int(position)

i = 0
j = 0
urllist = list()
namelist = list()
firstit = 1
#### loop for count
while i < cnt+1:
  if i == 0:
    url = input('Enter URL - ')
    if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Kerr.html'
    #if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
  else:
     url = urllist[-1]
     #print(url)
     #print(urllist[-1])
  #print(i)
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup.find_all('a')
  title = soup.title.string
  name = title.split()
  namelist.append(name[2])
  #print(title)
  j = 0
  for tag in tags:
    ####### loop for position
    j = j + 1
    if j == pos:
       url3 = tag.get('href', None)
       urllist.append(url3)
  i = i + 1

for name in range(len(namelist)):
    print(namelist[name])

