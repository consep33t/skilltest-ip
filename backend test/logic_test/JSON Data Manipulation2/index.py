import json

with open('data2.json') as file:
    inventory = json.load(file)

# 1. mencari item di ruang rapat
meeting_room_items = []
for item in inventory:
    if item['placement']['name'] == 'Meeting Room':
        meeting_room_items.append(item['name'])
print('Item di ruang rapat:', meeting_room_items)

# 2. menemukan semua perangkat elektronik
electronic_items = []
for item in inventory:
    if item['type'] == 'electronic':
        electronic_items.append(item['name'])
print('Perangkat elektronik:', electronic_items)

# 3. menemukan semua furnitur
furniture_items = []
for item in inventory:
    if item['type'] == 'furniture':
        furniture_items.append(item['name'])
print('Furnitur:', furniture_items)

# 4. menemukan semua item dengan warna coklat
brown_items = []
for item in inventory:
    if 'brown' in item['tags']:
        brown_items.append(item['name'])
print('Item berwarna coklat:', brown_items)
