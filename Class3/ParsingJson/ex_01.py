import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_42.json'
html = urllib.request.urlopen(url, context=ctx).read()

sum = 0
j = json.loads(html)
#print('User count:', len(j))#
#print(j["note"])
#print(j["comments"][0]["name"])
#print(j["comments"][0]["count"])
print('Total number of objects', len(j["comments"]))

for i in range(len(j["comments"])):
    sum = sum + j["comments"][i]["count"]

print(sum)