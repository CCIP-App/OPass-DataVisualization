import sys
import os
import json
import datetime
from pytz import timezone


if len(sys.argv) < 2:
    print("Usage : python3 parseDeliverertoDayCSV.py puzzle_bucket.json")
    sys.exit()

path = sys.argv[1]

if not os.path.exists(path):
    print("File not found")
    sys.exit()

dayData = {}

with open(path) as f:
    line = f.readline()
    while line:
        data = json.loads(line)["deliverer"]
        for sponsor in data:
            date = datetime.datetime.fromtimestamp(
                int(float(sponsor["timestamp"]["$numberDouble"]))).astimezone(timezone("Asia/Taipei")).strftime('%Y-%m-%d')
            name = str(sponsor["deliverer"])
            if date not in dayData:
                dayData[date] = {}
            if name not in dayData[date]:
                dayData[date][name] = 0
            dayData[date][name] += 1
        line = f.readline()
print(dayData)

totalData = {}
for day, data in dayData.items():
    with open("output/"+day+".csv", "w") as f:
        f.write("key,count\n")
        for key, count in data.items():
            f.write("%s,%d\n" % (key, count))
            if key not in totalData:
                totalData[key] = 0
            totalData[key] += count

with open("output/total.csv", "w") as f:
    f.write("key,count\n")
    for key, count in totalData.items():
        f.write("%s,%d\n" % (key, count))