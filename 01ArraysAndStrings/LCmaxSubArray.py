class Solution(object):
    def maxSubArray(self, nums):

        if len(nums) == 0:
            return 0
        
        currentSum = maxSum = nums[0]
        
        for num in nums[1:]:
            currentSum = max(num, num + currentSum)
            maxSum = max(currentSum, maxSum)
        return maxSum