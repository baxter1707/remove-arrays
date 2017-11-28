
###List of data (names) that you are working with.
##index 2
names = ["Alex","Mary","Steve","John","Seinfeld","Alan","Jane"]

## App that removes the following names: Steve and Alan

##index 1         #2       5
namesToRemove = ["Steve","Alan"]
indexToDelete = []


for index1 in range(0, len(namesToRemove)):
    for index2 in range(0, len(names)):
        #print(names[index2])
        if namesToRemove[index1].lower() == names[index2].lower():
            indexToDelete.append(index2)
            print(index2)



print(indexToDelete)
print(names)
for index3 in range(len(namesToRemove)-1,-1,-1):
    del names[indexToDelete[index3]]
print(names)
