# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        for num in nums:
            index = abs(num) -1 # -1 because the list is from 1 to n
            nums[index] = - abs(nums[index]) #if item appears twice, we use its absolute value, to make it negative again
            
        for i in range(len(nums)):
            if nums[i] > 0: # if it isn't turned into a neg number, this means the number refering their index (index = abs(num) -1 is) not in the list. So these are the missing numbers
            
                res.append(i + 1)
        return res
                
        