class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num # xor function returns 0 for the same items. if it is 0 and something else returns something else
        return result