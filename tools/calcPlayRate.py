import sys
import os
import json
import datetime
from pytz import timezone


if len(sys.argv) < 3:
    print("Usage : python3 calcPlayRate.py attendee.json puzzle_bucket.json")
    sys.exit()

attendeePath = sys.argv[1]
puzzlePath = sys.argv[2]

if not os.path.exists(attendeePath) or not os.path.exists(puzzlePath):
    print("File not found")
    sys.exit()

puzzleCount = 0
attendeeChecked = 0


def checkUsed(data, scenario):
    if scenario not in data["scenario"]:
        return(True)
    else:
        if "used" in data["scenario"][scenario]:
            return(True)
        else:
            return(False)


with open(attendeePath) as f:
   line = f.readline()
   while line:
        toCheckField = ["day1checkin", "day2checkin"]
        checked = False
        for field in toCheckField:
            if checkUsed(json.loads(line), field):
                checked = True
        if checkUsed:
            attendeeChecked += 1
        line = f.readline()


with open(puzzlePath) as f:
   line = f.readline()
   while line:
        if len(json.loads(line)["deliverer"]) > 0:
            puzzleCount += 1
        line = f.readline()

print("Attendee Check In : %d" % (attendeeChecked))
print("Puzzle Played : %d" % (puzzleCount))
print("Rate: %d%%" % (float(puzzleCount) / float(attendeeChecked) * float(100)))