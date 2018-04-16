class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        
        idx = 0
        for i in range (1, len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
        return idx+1