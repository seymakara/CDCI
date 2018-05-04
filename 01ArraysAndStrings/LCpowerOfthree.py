# Given an integer, write a function to determine if it is a power of three.

class Solution(object):
    def isPowerOfThree(self, n):
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        return False