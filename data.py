import string
import json
import csv
header = ['key','value']
 # Opening JSON file
jsonfile = open('data.json')

data = json.load(jsonfile)
print(data)
with open('data.csv','w',encoding='UTF-8',newline='') as f:
     writer = csv.writer(f)
     writer.writerow(header)
     writer.writerow(data)
for key, values in data.items():
          dict = {"key": key, "values": values}
          writer.writerow(key)
          writer.writerow(values)
for item in data.items():      
        writer.writerow(item)