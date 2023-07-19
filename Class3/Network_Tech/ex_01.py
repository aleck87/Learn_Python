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

url = input('Enter URL - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

nums = list()
sum = 0
count = 0

# retreive all of the anchor tags
tags = soup.find_all('tr')
for tag in tags:
   if tag.find('span'):
    tstr  = str(tag)
    sp_str = tstr
    count = re.findall('[0-9]+', sp_str)
    #print(sp_str)
    nums = nums + count
for i in range(len(nums)):
  sum = sum + int(nums[i])

print(sum)