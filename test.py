import pandas as pd
import json
import os

coldat = pd.read_json("./collectionsDAT/collections.json")

farming = coldat["collections"]["RIFT"]["items"]
farming_items = []

print(coldat["collections"]["FARMING"]["items"]["INK_SACK:3"]["name"])
print(coldat["collections"]["FARMING"]["items"]["INK_SACK:3"]["maxTiers"])

for item in farming:
    farming_items.append(item)

print(farming_items)

f = open("output.txt", "w")

# for item in farming_items:
#     print(str(item))


for item in farming_items:
    farmingItem = coldat["collections"]["RIFT"]["items"][item]
    name = farmingItem["name"]
    data = {}
    if os.path.exists('./collectionsDAT/collections_key.json'):
        with open('./collectionsDAT/collections_key.json', 'r') as f:
            data = json.load(f)
    data[item] = name
    with open('./collectionsDAT/collections_key.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Key-value pair added to the file.")