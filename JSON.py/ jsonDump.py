import json

data = {}
data['clients'] = []

data['clients'].append({
    'first_name':'Theodoric',
    'last_name':'Rivers',
    'age':36,
    'amount':1.11})

with open('data.json','w') as file:
    json.dump(data, file, indent = 4)

print(data) 