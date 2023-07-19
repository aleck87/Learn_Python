import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import collections
collections.Callable = collections.abc.Callable

import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
html = urllib.request.urlopen(url, context=ctx).read()

data = ET.fromstring(html)
clist = data.findall('comments/comment')
print('user count:', len(clist))

numlst = list()
sum = 0
for item in clist:
    #name = item.find('name').text
    num = item.find('count').text
    sum = sum + int(num)
    numlst.append(num)
print(sum)