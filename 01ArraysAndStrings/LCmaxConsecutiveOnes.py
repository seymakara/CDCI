# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        counter = 0
        res = 0
        for i in nums:
            if i == 1:
                counter +=1
                res = max(res, counter)
            else:
                counter = 0
        return res