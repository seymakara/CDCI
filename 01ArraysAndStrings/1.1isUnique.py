#time complexity: O(n^2)
#space complexity: O(1)
def isUnique(input):
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if input[j] == input[i]:
                return False
    return True

print isUnique("watere")

#-----------------------------------------------------------------

# time complexity: O(n) (using hashmap)

#PSUEDOCODE
# 1. create an empty dictionary
# 2. loop all elements of the array
# 3. for each element, check if item exists in the dictionary. if yes return false
# 4. if no, put the item in dictionary

# n2 ile olan algoritmalarin cogu hashmap kullanilarak n e dusurulebilir.

def isUniqueHash(input):
    if len(input) > 128:
        return False #this works with ASCII which has 128 characters not with Unicode.3

    newDict = {}
    for i in range (len(input)):
        if input[i] in newDict: 
            return False
        else:
            newDict[input[i]] = 1
    return True

print isUniqueHash("water")