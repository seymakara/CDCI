# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

def longestPalindrome(self, s):
        ctmap = {}
        for c in s:
            if c not in ctmap:
                ctmap[c] = 1
            else:
                ctmap[c] += 1

        length = 0
        singleCharFound = 0
        for key in ctmap:
            if ctmap[key] % 2 == 0:
                length += ctmap[key]
            else:
                length += ctmap[key] - 1
                singleCharFound = 1

        return length + singleCharFound