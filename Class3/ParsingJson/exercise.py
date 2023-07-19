import json

data = '''
{
  "note":"This file contains the sample data for testing",
  "comments":[
    {
      "name":"Romina",
      "count":97
    },
    {
      "name":"Laurie",
      "count":97
    },
    {
      "name":"Bayli",
      "count":90
    }
    ]
}'''

j = json.loads(data)

print(j["note"])
print(j["comments"][0]["name"])
print(j["comments"][0]["count"])
print(len(j["comments"]))