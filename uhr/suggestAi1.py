#for square root function
import math
#for json
import json

#-------------------------------------------------------------------------
#COSINE-SIMILARITY
#-------------------------------------------------------------------------

#read the repository or data in xl sheet
dataList = []
def readRepo():
    try:
        files = open("med.txt","r+")
        readFile = files.readlines()
        files.close()
        for data in readFile:
             dataList.append(data.strip("\n"))
        return dataList
    except Exception as e:
        print(str(e))
        return False

#removes the duplicate element in list
def remove(duplicate):
    final_list = [] 
    for num in duplicate:
        if num not in final_list: 
            final_list.append(num)
    final_list.sort()
    return final_list 

testList = remove(readRepo())

#document list
with open('medicalVector.json', 'r') as openfile:
    listData = json.load(openfile)
print(listData)
listOfData = listData["main"]

#clear given input
def cleanInput(inputList):
    try:
        testList1 = testList[:]
        for pos in range(len(testList1)):
            if testList1[pos] in inputList:
                testList1[pos] = inputList.count(testList1[pos])
            else:
                testList1[pos] = 0
        return testList1
    except Exception as e:
        print(str(e))
        return str(e)
    
#cosine similarity function
def cosineSimilarity(vec1,vec2):
    try:
        count = 0
        for i in range(len(vec1)):
            count += vec1[i] * vec2[i]
        return count / float(math.sqrt(sum(vec1)) * math.sqrt(sum(vec2)))
    except Exception as e:
        return str(e)

#cosine distance
def cosineDistance(value):
    try:
        return float(1 - value)
    except Exception as e:
        return str(e)

#returns the correct output
def understand(ipList,tokens):
    try:
        returnList = []
        sortedIp = (sorted(ipList,key = lambda x:x["val"]))
        print(sortedIp)
        for d in sortedIp:
            error = 0
            splitData = d["name"].split(" ")
            for data in splitData:
                if data in tokens:
                    tokens.pop(tokens.index(data))
                else:
                    error += 1
            if error == 0:
                returnList.append(d["name"])
        return returnList
    except:
        return False

#returns the predicted value
def returnSuggest(textInput):
    try:
        error = 0
        dictionary = {}
        
        measureList3 = []
        measureList2 = []
        measureList1 = []
        val = 0
        tokens = textInput.split(" ")
        for data in listOfData:
            store = {}
            val = cosineDistance(cosineSimilarity(cleanInput(tokens),data["vector"]))
            try:
                if val <= 0.9 and data["name"] not in measureList3:
                    
                    store["name"] = data["name"]
                    store["val"] = val
                    measureList3.append(store)
            except:
                error += 1
        for data in measureList3:
            if textInput.find(data["name"]) != -1 :
                measureList1.append(data)
        dictionary["suggestion"] = understand(measureList1,tokens)
        return dictionary
    except Exception as e:
        dictionary["worktype"] = "cannot understand"
        return dictionary
