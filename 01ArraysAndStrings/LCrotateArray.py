#Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]

class Solution2:
    def rotate(self, nums, k):
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1