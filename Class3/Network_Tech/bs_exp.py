import urllib.request, urllib.parse, urllib.error

import collections
collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup

url = input('Entier URL - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retreive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
