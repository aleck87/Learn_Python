#import xml.etree.ElementTree as ET
#data = '''
#<person>
#  <name>Deepak</name>
#  <phone type="intl">
#    +49 1734136564
#  </phone>
#  <email hide="yes"/>
#</person>'''

#tree = ET.fromstring(data)
#print('Name', tree.find('name').text)
#print('Atrr', tree.find('email').get('hide'))

import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)

print(stuff)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print(item)
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))


