# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

class Solution(object):
    def wordPattern(self, pattern, str):
        d1 = {}
        d2 = {}
        string = str.split(" ")
        
        for i in range(len(pattern)):
            
            if pattern[i] not in d1:
                d1[pattern[i]] = [i]
            else:
                d1[pattern[i]] += [i]
                
        for i in range(len(string)):
            if string[i] not in d2:
                d2[string[i]] = [i]
                
            else:
                d2[string[i]] += [i]
        
        if sorted(d1.values()) == sorted(d2.values()):
            return True
        
        return False