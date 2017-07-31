#!/usr/bin/python
import operator

def compare(s1, s2):
    return int(s2["PERCENT"] - s1["PERCENT"])

studentList = [
    {"Name":"A1", "PHY":76, "CHE":67, "MTH":47},
    {"Name":"A2", "PHY":56, "CHE":87, "MTH":87},
    {"Name":"A3", "PHY":86, "CHE":38, "MTH":97},
    {"Name":"A4", "PHY":26, "CHE":49, "MTH":72},
    {"Name":"A5", "PHY":79, "CHE":44, "MTH":77},
]

subjectAverage = {"PHY":0, "CHE":0, "MTH":0}

for student in studentList:
    percentMarks = ((student["PHY"] + student["CHE"] + student["MTH"])/300.0)*100
    student["PERCENT"] = percentMarks
    subjectAverage["PHY"] += student["PHY"]
    subjectAverage["CHE"] += student["CHE"]
    subjectAverage["MTH"] += student["MTH"]

studentList = sorted(studentList, cmp=compare)

for subject in subjectAverage:
    subjectAverage[subject] = subjectAverage[subject] / len(studentList)
    print subject, subjectAverage[subject]

i = 1
for student in studentList:
    print "Rank: " + str(i) + " " + student["Name"] + " Percentage = " + str(student["PERCENT"])
    i += 1

sortedSubAvg = sorted(subjectAverage, key=operator.itemgetter(1), reverse=True)

print sortedSubAvg