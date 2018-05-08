# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        return len([x for x in nums if x<target])
    
    def searchInsert2(self, nums, target):
        start = 0
        end = len(nums)-1
        while start <= end :
            mid  = (start + end) // 2
            if nums[mid]  == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid -1
        return start