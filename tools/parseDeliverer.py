import sys
import os
import json

if len(sys.argv) < 2:
    print("Usage : python3 parseDeliverer.py puzzle_bucket.json")
    sys.exit()

path = sys.argv[1]

if not os.path.exists(path):
    print("File not found")
    sys.exit()

sortByTimestamp = {}
sponsors = []

with open(path) as f:
    line = f.readline()
    while line:
        data = json.loads(line)["deliverer"]
        for sponsor in data:
            time = int(float(sponsor["timestamp"]["$numberDouble"]))
            name = str(sponsor["deliverer"])
            if time not in sortByTimestamp:
                sortByTimestamp[time] = {}
            if name not in sortByTimestamp[time]:
                sortByTimestamp[time][name] = 0
            if name not in sponsors:
                sponsors.append(name)
            sortByTimestamp[time][name] += 1
        line = f.readline()

outData = []
for key, value in sortByTimestamp.items():
    outData.append({"time": key, "data": value})

def getTime(el):
    return(el["time"])

outData.sort(key=getTime)

with open("output/sortByTime.json", "w") as f:
    f.write(json.dumps({
        "fields": sponsors,
        "data": outData
    }))
    f.close()
