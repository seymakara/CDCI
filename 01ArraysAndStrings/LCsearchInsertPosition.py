# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        return len([x for x in nums if x<target])
        index = 0
        for num in nums:
            if num <= target:
                index += 1
        return index