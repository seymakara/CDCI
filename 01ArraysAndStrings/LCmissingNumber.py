#Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array

class Solution(object):
    def missingNumber(self, nums):
        length = len(nums)
        sum = (length*(length+1))/2 # listenin uzunlugu bize son rakami verir, cunku zaten listede eksik bir rakam var.
        for num in nums:
            sum -= num
        return sum