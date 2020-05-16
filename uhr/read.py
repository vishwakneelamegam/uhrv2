import json

files = open("med.txt","r+")
readFile = files.readlines()
clears = []
print(len(readFile))
files.close()
for data in readFile:
    clears.append(data.strip("\n").lower())
dictionary = {}
dictionary["main"] = []
count = 0
for op in clears:
    vec = []
    temp = {}
    for data in clears:
        if op == data:
           vec.append(1)
        else:
           vec.append(0)
    temp["vector"] = vec
    temp["name"] = op
    dictionary["main"].append(temp)
    count += 1
    print(count)
with open('medicalVector.json', 'w') as outfile:
    json.dump(dictionary, outfile)
