# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        greaterNumDict = {}
        stack = []
        res = []
        
        for num in nums:
            if len(stack) == 0:
                stack.append(num)
            elif num <= stack[-1]:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    greaterNumDict[stack.pop()] = num # you need to pop the peek otherwise it can be added to dict multiple times if there are two or more greater item than the peek.
                stack.append(num)
                
        for num in findNums:
            if num in greaterNumDict:
                res.append(greaterNumDict[num])
            else:
                res.append(-1)
        return res
            
        