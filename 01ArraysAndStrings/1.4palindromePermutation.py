# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# 1. put them in a hash map
# 2. increment i for duplicates
# 3. loop through the hashmap
# 4. Return false if there is more than 1 odd value

#time complexity = O(n)

def PalindromePermutation(input):
    newDict = {}
    for i in input:
        if i not in newDict:
            newDict[i] = 1
        elif i in newDict:
            newDict[i] +=1
    countOdd = 0
    for key in newDict:
        if newDict[key] % 2 == 1:
            countOdd += 1
    if countOdd > 1:
        return False 
    return True 

print PalindromePermutation("tactcoapapa..")
