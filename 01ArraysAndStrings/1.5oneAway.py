# if length of the strings are same, check for replace
    # for replace, loop through the string, if not same increment the count
    # if the count is bigger than 1 return false
    # else return true
# if different check for insert and removal(they are basicly same, just switch sides) (assuming string2 is longer)
    # loop through the string. 
    # if characters are different check for the index number
        # if index numbers are same increment the index number of string2 (because it is the longer one)
        # if index numbers are different return false
    # if characters are are same increment both indexes

def oneEdit(string1, string2):
    if len(string1) == len(string2):
        return oneReplace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return oneInsert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return oneInsert(string2, string1)
    else:
        return False

def oneReplace(string1, string2):
    diffCount = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            diffCount += 1
    if diffCount > 1:
        return False
    return True

def oneInsert(string1, string2):
    index1 = 0
    index2 = 0
    while index1 < len(string1) and index2 < len(string2):
        if string1[index1] != string2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

print oneEdit("pele", "pale")

