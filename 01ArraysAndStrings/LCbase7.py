# Given an integer, return its base 7 string representation.

# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"

class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        
        n = abs(num)
        res = ''
        
        while n > 0:
            res = str(n%7) + res
            n /= 7
        return res if num > 0 else '-' + res