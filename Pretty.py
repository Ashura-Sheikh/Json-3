import json

file = open('Data.json', 'r')
Data = file.read()

obj = json.loads(Data)

for person in obj['people']: # same concept
    del person['No']

new_data = json.dumps(obj, indent=2, sort_keys = True) # printing data in json with required Data
print(new_data)
