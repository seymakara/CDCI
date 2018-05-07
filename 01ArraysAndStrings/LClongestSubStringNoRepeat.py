# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0 # keeps the starting point of the longest substring
        dict = {}
        maxLength = 0
        for i in range(len(s)):
            # you should also check if starting point is smaller than the index of the last repeating char in the dictionary.
            # e.g. the first element (s[0]) can repeat at the end of the string, in that case starting point becomes 1 again.
            if s[i] in dict and start <= dict[s[i]]:  
                start = dict[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1) # you should add one, because you start from 0. Otherwise for the first char maxlength would be 0
            
            dict[s[i]] = i # equalize key to the index
        return maxLength