# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if not ransomNote and not magazine:
            return True
        
        dictMag = {}
        for i in range(len(magazine)):
            if magazine[i] not in dictMag:
                dictMag[magazine[i]] = 1
            else:
                dictMag[magazine[i]] += 1
                
        dictNote = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in dictNote:
                dictNote[ransomNote[i]] = 1
            else:
                dictNote[ransomNote[i]] += 1
                
        for key in dictNote:
            if key not in dictMag or dic2[key] > dictMag[key]:
                return False
        return True