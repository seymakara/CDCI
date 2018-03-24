#PSEUDOCODE
# 1. count the spaces
# 2. double the spaces
# 3. add spaces to the true length of the syntax
# 4. starting at the end add %20 to the spaces
# 5. i f no space keep the original character

#

def urlify(input, num):
    spaceCount = 0
    for i in range (len(input)):
        if input[i] == " ":
            spaceCount += 1
    print spaceCount
    index = num + spaceCount * 2
    print index-1

    inputList = list(input)
    print inputList

    for i in range (len(inputList)-1, 0, -1):
        if inputList[i]==' ':
            inputList[index-1] = "0" #not working can not assign a new value to astring in python.
            inputList[index-2] = "2"
            inputList[index-3] = "%"
            index -= 3
        else:
            inputList[index-1] = input[i]
            index -=1
    newInput = ''.join(inputList)
    return newInput
            
print urlify("seyma ka ra ", 12)