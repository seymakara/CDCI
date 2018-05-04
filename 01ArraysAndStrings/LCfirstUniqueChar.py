#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Examples:
# s = "leetcode"
# return 0.
# s = "loveleetcode",
# return 2.


class Solution(object):
    def firstUniqChar(self, s):
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            elif char not in dict:
                dict[char] = 1
            
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1