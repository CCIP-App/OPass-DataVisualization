import sys
import os
import json

if len(sys.argv) < 2:
    print("Usage : python3 toCSV.py attendee.json")
    sys.exit()

path = sys.argv[1]

if not os.path.exists(path):
    print("File not found")
    sys.exit()

attendees = []

with open(path) as f:
   line = f.readline()
   while line:
       attendees.append(json.loads(line))
       line = f.readline()

outPath = "output/" + path + ".csv"

def checkUsed(data,scenario):
    if scenario not in data["scenario"]:
        return("NONE")
    else:
        if "used" in data["scenario"][scenario]:
            return("USED")
        else:
            return("NOTUSED")

with open(outPath,"w") as f:
    f.write("role,name,day1checkin,day2checkin,kit,vipkit,welcome_party" + "\n")
    for attendee in attendees:
        data = []
        data.append(attendee["role"])
        data.append(attendee["user_id"])
        data.append(checkUsed(attendee,"day1checkin"))
        data.append(checkUsed(attendee,"day2checkin"))
        data.append(checkUsed(attendee,"kit"))
        data.append(checkUsed(attendee,"vipkit"))
        data.append(checkUsed(attendee,"welcome_party"))
        f.write(",".join(data) + "\n")
        print(data)