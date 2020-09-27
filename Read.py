import json # Reading through json file

file = open('Data.json', 'r')
Data = file.read()

obj = json.loads(Data)
print(type(obj['people']))

for person in obj['people']: # Deleting the No.
    del person['No']
    #print(person['name'], person['mail'], person['has_license'])

new_data = json.dumps(obj) # creating a new data set
print(type(new_data))
print(new_data)
