# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

class Solution(object):
    def isIsomorphic(self, s, t):
      
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], []) + [i] #you should keep their order in array because the order of characters should be preserved.

        for i in range(len(t)):
            d2[t[i]] = d2.get(t[i], []) + [i]
            
        if sorted(d1.values()) == sorted(d2.values()):
            return True
        
        return False