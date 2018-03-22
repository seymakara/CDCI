#PSUEDOCODE
# 1. create an empty dictionary
# 2. check if length of strings are equal, if not return false
# 3. for each element in string1, put them into dictionary and make the value 1, if exists ++
# 4. for each element in string2, check if they are in the dictionary and if yes decrease 1, if not return false

def checkPermuataion(input1, input2):
    if len(input1) != len(input2):
        return False

    newDict = {}

    for i in input1:
        if i not in newDict:
            newDict[i]=1
        else:
            newDict[i]+=1

    for i in input2:
        if i in newDict:
            newDict[i] -=1
        else:
            return False
    
    for key in newDict:
        if newDict[key] != 0:
            return False
    return True


print checkPermuataion("water", "watrr")