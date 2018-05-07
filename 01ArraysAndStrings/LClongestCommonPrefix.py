# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"

class Solution(object):
    
    def minStringLen(self, strs):
        minStr = ""
        if len(strs) != 0:
            minStr = strs[0]
            for i in range (1, len(strs)):
                if len(strs[i]) <= len(minStr):
                    minStr = strs[i]
        return len(minStr)
    
    def longestCommonPrefix(self, strs):
        shortest_len = self.minStringLen(strs)
        res = ""
        for i in range (shortest_len):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != current:
                    return res
            res += current
        return res