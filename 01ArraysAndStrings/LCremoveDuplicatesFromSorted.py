#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
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