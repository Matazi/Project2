import json, csv


csvFpath = 'volcanos.csv'
jsonFpath = 'volcanos2.json'

map = {}
with open(csvFpath) as cfile:
    csvRead = csv.DictReader(cfile)
    for rows in csvRead:
        id = int(rows['volcano_number'])
        map[id] = rows
with open(jsonFpath, 'w') as jFile:
    jFile.write(json.dumps(map, indent=4))
