# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

class Solution(object):    
    def isAnagram(self, s, t):
        sDict = {}
        tDict = {}
        for item in s:
            sDict[item] = sDict.get(item, 0) + 1
        for item in t:
            tDict[item] = tDict.get(item, 0) + 1
        return sDict == tDict