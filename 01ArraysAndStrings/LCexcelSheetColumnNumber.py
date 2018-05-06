# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28


class Solution(object):
    def titleToNumber(self, s):
        res = 0 
        for l in s:
            res = res * 26 + (ord(l) - ord("A") +1)
        return res