class Solution(object):
    def moveZeroes(self, nums):
        index_of_0 = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                # nums[index_of_0], nums[i] = nums[i], nums[index_of_0] #burda i ve index_of_0 ayni olcagi icin aslinda swap etmiyor. this is a pythonic swap
                temp = nums[index_of_0] # swap algorithm 
                nums[index_of_0] = nums[i]
                nums[i] = temp
                index_of_0 += 1