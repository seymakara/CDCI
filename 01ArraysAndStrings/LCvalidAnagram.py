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

    def isAnagram2(self, s, t):
        alphabet = [0]*26
        for i in s:
            alphabet[ord(i) - ord(a)] += 1 # anin ascii kodu 97. 97 den 97 yi cikararak a yi listede 0. index e koymus oluyoruz. ord(b) = 98...
        for i in t:
            alphabet[ord(i) - ord(a)] -= 1
        for i in alphabet:
            if i !=0:
                return False
        return True